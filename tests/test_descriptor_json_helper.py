import pytest
from basyx.aas import model

from aas_standard_parser import descriptor_json_helper


def test_001a_get_mapping_configuration_root_element():
    href = "http://aas-server:8075/shells/aHR0cHM6Ly9mbHVpZDQwLmRlL2lkcy9zaGVsbC81NzkzXzU0NDlfNzgzMF80MjIz"

    href_data = descriptor_json_helper.parse_endpoint_href(href)

    assert href_data is not None
    assert href_data.base_url == "http://aas-server:8075"
    assert href_data.identifier == "aHR0cHM6Ly9mbHVpZDQwLmRlL2lkcy9zaGVsbC81NzkzXzU0NDlfNzgzMF80MjIz"
    assert href_data.identifier_decoded == "https://fluid40.de/ids/shell/5793_5449_7830_4223"

def test_001b_get_mapping_configuration_root_element():
    href = "http://aas-server:8075/submodels/RW5lcmd5TW9uaXRvcmluZw"

    href_data = descriptor_json_helper.parse_endpoint_href(href)

    assert href_data is not None
    assert href_data.base_url == "http://aas-server:8075"
    assert href_data.identifier == "RW5lcmd5TW9uaXRvcmluZw"
    assert href_data.identifier_decoded == "EnergyMonitoring"

def test_002a_parse_descriptor_json():
    descriptor = {
        "description": [
            {
            "language": "en",
            "text": "The software information aspect model contains the essential information of all software components that have been implemented or flashed in an instantiated part (e.g. serialized part). "
            }
        ],
        "idShort": "SoftwareInformation",
        "id": "submodel_SoftwareInformation_20260608113026879_0",
        "semanticId": {
            "type": "ExternalReference",
            "keys": [
            {
                "type": "GlobalReference",
                "value": "urn:samm:io.catenax.software_information:1.0.0#SoftwareInformation"
            }
            ]
        },
        "endpoints": [
            {
            "protocolInformation": {
                "href": "https://engineering-app-poc.em.ag/aas-env/submodels/c3VibW9kZWxfU29mdHdhcmVJbmZvcm1hdGlvbl8yMDI2MDYwODExMzAyNjg3OV8w",
                "endpointProtocol": "https"
            },
            "interface": "SUBMODEL-3.0"
            }
        ]
        }

    descriptor_data = descriptor_json_helper.parse_descriptor(descriptor)

    assert descriptor_data is not None
    assert descriptor_data.description == {"en": "The software information aspect model contains the essential information of all software components that have been implemented or flashed in an instantiated part (e.g. serialized part). "}
    assert descriptor_data.main_description == "The software information aspect model contains the essential information of all software components that have been implemented or flashed in an instantiated part (e.g. serialized part). "
    assert descriptor_data.display_name == {}
    assert descriptor_data.id_short == "SoftwareInformation"
    assert descriptor_data.semantic_id == {
        "type": "ExternalReference",
        "keys": [
            {
                "type": "GlobalReference",
                "value": "urn:samm:io.catenax.software_information:1.0.0#SoftwareInformation"
            }
        ]
    }
    assert len(descriptor_data.endpoints) == 1
    assert descriptor_data.endpoints[0]["protocolInformation"]["href"] == "https://engineering-app-poc.em.ag/aas-env/submodels/c3VibW9kZWxfU29mdHdhcmVJbmZvcm1hdGlvbl8yMDI2MDYwODExMzAyNjg3OV8w"
    assert descriptor_data.endpoints[0]["protocolInformation"]["endpointProtocol"] == "https"
    assert descriptor_data.endpoints[0]["interface"] == "SUBMODEL-3.0"
    assert descriptor_data.main_display_name == ""

def test_002b_parse_descriptor_json():
    descriptor = {
        "assetKind": "Instance",
        "displayName": [
            {
                "language": "en",
                "text": "A2123324235"
            }
        ],
        "endpoints": [
            {
                "interface": "AAS-3.2",
                "protocolInformation": {
                    "endpointProtocol": "https",
                    "href": "https://eng-app-dev.em.ag/aas-env-go/shells/aHR0cHM6Ly93d3cuZW0uYWcvc2hlbGwvYTIxMjMzMjQyMzU"
                }
            }
        ],
        "globalAssetId": "A2123324235",
        "id": "https://www.em.ag/shell/a2123324235",
        "idShort": "A2123324235",
        "submodelDescriptors": [
            {
                "endpoints": [
                    {
                        "interface": "SUBMODEL-3.2",
                        "protocolInformation": {
                            "endpointProtocol": "https",
                            "href": "https://eng-app-dev.em.ag/aas-env-go/submodels/aHR0cHM6Ly93d3cuZW0uYWcvc2hlbGwvYTIxMjMzMjQyMzUvcGFydHR5cGVpbmZvcm1hdGlvbg"
                        }
                    }
                ],
                "id": "https://www.em.ag/shell/a2123324235/parttypeinformation"
            }
        ]
    }

    descriptor_data = descriptor_json_helper.parse_descriptor(descriptor)

    assert descriptor_data is not None
    assert descriptor_data.description == {}
    assert descriptor_data.main_description == ""
    assert descriptor_data.display_name == {"en": "A2123324235"}
    assert descriptor_data.main_display_name == "A2123324235"
    assert descriptor_data.assetKind == "Instance"
    assert descriptor_data.global_asset_id == "A2123324235"
    assert descriptor_data.id_short == "A2123324235"
    assert descriptor_data.semantic_id == {}
    assert descriptor_data.endpoints == descriptor["endpoints"]
    assert len(descriptor_data.submodels) == 1
    assert descriptor_data.submodels[0].href == "https://eng-app-dev.em.ag/aas-env-go/submodels/aHR0cHM6Ly93d3cuZW0uYWcvc2hlbGwvYTIxMjMzMjQyMzUvcGFydHR5cGVpbmZvcm1hdGlvbg"
    assert descriptor_data.submodels[0].identifier == "aHR0cHM6Ly93d3cuZW0uYWcvc2hlbGwvYTIxMjMzMjQyMzUvcGFydHR5cGVpbmZvcm1hdGlvbg"
