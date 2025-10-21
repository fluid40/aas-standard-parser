import pytest
from basyx.aas import model

import aas_standard_parser.aimc_parser as aimc_parser
from aas_standard_parser.utils import create_submodel_from_file


@pytest.fixture(scope="module")
def aimc_submodel() -> model.Property:
    # create a Submodel
    return create_submodel_from_file("tests/test_data/aimc_submodel.json")


def test_001_get_mapping_configuration_root_element(aimc_submodel: model.submodel):
    root_element = aimc_parser.get_mapping_configuration_root_element(aimc_submodel)

    assert root_element is not None
    assert root_element.id_short == "MappingConfigurations"


def test_002_get_mapping_configuration_elements(aimc_submodel: model.submodel):
    configuration_elements = aimc_parser.get_mapping_configuration_elements(
        aimc_submodel
    )

    assert configuration_elements is not None
    assert len(configuration_elements) == 1
    assert isinstance(configuration_elements[0], model.SubmodelElementCollection)


def test_003_parse_mapping_configurations(aimc_submodel: model.submodel):
    mapping_configurations = aimc_parser.parse_mapping_configurations(aimc_submodel)

    assert mapping_configurations is not None
    assert len(mapping_configurations.configurations) == 1
    assert len(mapping_configurations.aid_submodel_ids) == 1

    configuration = mapping_configurations.configurations[0]
    assert configuration.aid_submodel_id is not None
    assert configuration.aid_submodel_id in mapping_configurations.aid_submodel_ids

def test_003a_parse_mapping_configurations_interface_ref(aimc_submodel: model.submodel  ):
    mapping_configurations = aimc_parser.parse_mapping_configurations(aimc_submodel)
    configuration = mapping_configurations.configurations[0]

    assert configuration.interface_reference is not None

def test_003b_parse_mapping_configurations_relations_aid(aimc_submodel: model.submodel  ):
    mapping_configurations = aimc_parser.parse_mapping_configurations(aimc_submodel)
    configuration = mapping_configurations.configurations[0]

    assert len(configuration.source_sink_relations) > 0

    relation = configuration.source_sink_relations[0]
    assert relation is not None
    assert relation.aid_submodel_id == configuration.aid_submodel_id
    assert relation.aid_submodel_id in mapping_configurations.aid_submodel_ids

    assert relation.property_name is not None
    assert relation.property_name == "HandlingC"


def test_003c_parse_mapping_configurations_relations(aimc_submodel: model.submodel  ):
    mapping_configurations = aimc_parser.parse_mapping_configurations(aimc_submodel)
    configuration = mapping_configurations.configurations[0]

    assert len(configuration.source_sink_relations) > 0

    relation = configuration.source_sink_relations[0]
    assert relation is not None
    assert relation.source is not None
    assert relation.sink is not None

    assert isinstance(relation.source, model.ExternalReference)
    assert isinstance(relation.sink, model.ExternalReference)
