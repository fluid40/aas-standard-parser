import pytest
from basyx.aas import model

from aas_standard_parser import concept_description_parser


def test_001a_parse_concept_description_from_dict():
    cd_dict = {
        "displayName": [
            {
                "language": "en",
                "text": "Calculated Weight"
            }
        ],
        "description": [
            {
                "language": "en",
                "text": "Mass of the part, typically in kilograms. Calculated out of all belonging 3D-models"
            }
        ],
        "embeddedDataSpecifications": [
            {
                "dataSpecification": {
                    "keys": [
                        {
                            "type": "GlobalReference",
                            "value": "https://admin-shell.io/DataSpecificationTemplates/DataSpecificationIec61360/3/0"
                        }
                    ],
                    "type": "ExternalReference"
                },
                "dataSpecificationContent": {
                    "dataType": "REAL_MEASURE",
                    "definition": [
                        {
                            "language": "en",
                            "text": "Mass of the part, typically in kilograms. Calculated out of all belonging 3D-models"
                        }
                    ],
                    "modelType": "DataSpecificationIec61360",
                    "preferredName": [
                        {
                            "language": "en",
                            "text": "Calculated Weight"
                        }
                    ],
                    "shortName": [
                        {
                            "language": "en",
                            "text": "calculatedWeight"
                        }
                    ],
                    "unit": "kilogram"
                }
            }
        ],
        "id": "urn:samm:io.catenax.digital_engineering_master_data:1.0.0#calculatedWeight",
        "idShort": "calculatedWeight",
        "modelType": "ConceptDescription"
    }

    cd_data = concept_description_parser.parse_concept_description_from_dict(cd_dict)
    assert cd_data.main_display_name == "Calculated Weight"
    assert cd_data.main_description == "Mass of the part, typically in kilograms. Calculated out of all belonging 3D-models"
    assert cd_data.data_specification_content[0].unit == "kilogram"
    assert cd_data.data_specification_content[0].data_type == {"name": "REAL_MEASURE"}
    assert cd_data.data_specification_content[0].definition == "Mass of the part, typically in kilograms. Calculated out of all belonging 3D-models"
    assert cd_data.data_specification_content[0].preferred_name == "Calculated Weight"
    assert cd_data.data_specification_content[0].short_name == "calculatedWeight"
    assert cd_data.data_specification_content[0].unit_id == ""
    assert cd_data.data_specification_content[0].value == ""
    assert cd_data.data_specification_content[0].value_format == ""
    assert cd_data.data_specification_content[0].value_list == []
    assert cd_data.data_specification_content[0].symbol == ""


