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


def test_parse_concept_description_with_value_list():
    cd_dict =        {
            "displayName": [
                {
                    "language": "en",
                    "text": "Category"
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
                        "dataType": "STRING",
                        "definition": [
                            {
                                "language": "en",
                                "text": "Category, the part belongs to. Based on VDA 4993."
                            }
                        ],
                        "modelType": "DataSpecificationIec61360",
                        "preferredName": [
                            {
                                "language": "en",
                                "text": "Category"
                            }
                        ],
                        "shortName": [
                            {
                                "language": "en",
                                "text": "category"
                            }
                        ],
                        "valueList": {
                            "valueReferencePairs": [
                                {
                                    "value": "Body & Structure",
                                    "valueId": {
                                        "keys": [
                                            {
                                                "type": "GlobalReference",
                                                "value": "urn:samm:io.catenax.digital_engineering_master_data:1.0.0#CategoryCharacteristic:_BodyStructure40898ebe"
                                            }
                                        ],
                                        "type": "ExternalReference"
                                    }
                                },
                                {
                                    "value": "Interior",
                                    "valueId": {
                                        "keys": [
                                            {
                                                "type": "GlobalReference",
                                                "value": "urn:samm:io.catenax.digital_engineering_master_data:1.0.0#CategoryCharacteristic:_Interior25b5c8ed"
                                            }
                                        ],
                                        "type": "ExternalReference"
                                    }
                                },
                                {
                                    "value": "Exterior",
                                    "valueId": {
                                        "keys": [
                                            {
                                                "type": "GlobalReference",
                                                "value": "urn:samm:io.catenax.digital_engineering_master_data:1.0.0#CategoryCharacteristic:_Exteriorcd41a1f4"
                                            }
                                        ],
                                        "type": "ExternalReference"
                                    }
                                },
                                {
                                    "value": "Electrical & Electronics",
                                    "valueId": {
                                        "keys": [
                                            {
                                                "type": "GlobalReference",
                                                "value": "urn:samm:io.catenax.digital_engineering_master_data:1.0.0#CategoryCharacteristic:_ElectricalElectronicsed6f222a"
                                            }
                                        ],
                                        "type": "ExternalReference"
                                    }
                                },
                                {
                                    "value": "Powertrain & Drivetrain",
                                    "valueId": {
                                        "keys": [
                                            {
                                                "type": "GlobalReference",
                                                "value": "urn:samm:io.catenax.digital_engineering_master_data:1.0.0#CategoryCharacteristic:_PowertrainDrivetrainf2249172"
                                            }
                                        ],
                                        "type": "ExternalReference"
                                    }
                                },
                                {
                                    "value": "Chassis & Brake Systems",
                                    "valueId": {
                                        "keys": [
                                            {
                                                "type": "GlobalReference",
                                                "value": "urn:samm:io.catenax.digital_engineering_master_data:1.0.0#CategoryCharacteristic:_ChassisBrakeSystemsf45be4fe"
                                            }
                                        ],
                                        "type": "ExternalReference"
                                    }
                                },
                                {
                                    "value": "Thermal Management & HVAC",
                                    "valueId": {
                                        "keys": [
                                            {
                                                "type": "GlobalReference",
                                                "value": "urn:samm:io.catenax.digital_engineering_master_data:1.0.0#CategoryCharacteristic:_ThermalManagementHVACa369773f"
                                            }
                                        ],
                                        "type": "ExternalReference"
                                    }
                                },
                                {
                                    "value": "Fasteners & Connectors",
                                    "valueId": {
                                        "keys": [
                                            {
                                                "type": "GlobalReference",
                                                "value": "urn:samm:io.catenax.digital_engineering_master_data:1.0.0#CategoryCharacteristic:_FastenersConnectorsdcc30007"
                                            }
                                        ],
                                        "type": "ExternalReference"
                                    }
                                },
                                {
                                    "value": "Software & Embedded Systems",
                                    "valueId": {
                                        "keys": [
                                            {
                                                "type": "GlobalReference",
                                                "value": "urn:samm:io.catenax.digital_engineering_master_data:1.0.0#CategoryCharacteristic:_SoftwareEmbeddedSystems1e332480"
                                            }
                                        ],
                                        "type": "ExternalReference"
                                    }
                                },
                                {
                                    "value": "Testing & Auxiliary Equipment",
                                    "valueId": {
                                        "keys": [
                                            {
                                                "type": "GlobalReference",
                                                "value": "urn:samm:io.catenax.digital_engineering_master_data:1.0.0#CategoryCharacteristic:_TestingAuxiliaryEquipment5dab6184"
                                            }
                                        ],
                                        "type": "ExternalReference"
                                    }
                                }
                            ]
                        }
                    }
                }
            ],
            "id": "urn:samm:io.catenax.digital_engineering_master_data:1.0.0#category",
            "idShort": "category",
            "modelType": "ConceptDescription"
    }

    cd_data = concept_description_parser.parse_concept_description_from_dict(cd_dict)
    value_list = cd_data.data_specification_content[0].value_list
    assert len(value_list) == 10
    assert any(
        item.value == "Body & Structure"
        and item.reference_value
        == "urn:samm:io.catenax.digital_engineering_master_data:1.0.0#CategoryCharacteristic:_BodyStructure40898ebe"
        for item in value_list
    )
