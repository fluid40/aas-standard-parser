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

def test_002_parse_descriptor_json():
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
