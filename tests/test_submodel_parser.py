import pytest
from basyx.aas import model

from aas_standard_parser.classes.aimc_parser_classes import MappingConfiguration, SourceSinkRelation, ReferenceProperties
import aas_standard_parser.submodel_parser as submodel_parser
from aas_standard_parser.utils import create_submodel_from_file


@pytest.fixture(scope="module")
def aimc_submodel() -> model.Submodel:
    # create a Submodel
    return create_submodel_from_file("tests/test_data/aimc_submodel.json")

def test_001a_get_description_from_submodel(aimc_submodel: model.Submodel):
    description = submodel_parser.get_description_from_submodel(aimc_submodel)

    assert description is not None
    assert description == 'This Submodel specifies an information model for describing the mapping of interface(s) of an asset service or asset-related service already described in an Asset Interfaces Description (AID) Submodel.'

def test_001b_get_description_from_submodel(aimc_submodel: model.Submodel):
    description = submodel_parser.get_description_from_submodel(aimc_submodel, "de")

    assert description is None

def test_002a_get_display_name_from_submodel(aimc_submodel: model.Submodel):
    display_name = submodel_parser.get_display_name_from_submodel(aimc_submodel)

    assert display_name is not None
    assert display_name == 'AIMC Submodel.'

def test_002b_get_display_name_from_submodel(aimc_submodel: model.Submodel):
    display_name = submodel_parser.get_display_name_from_submodel(aimc_submodel, "de")

    assert display_name is None
