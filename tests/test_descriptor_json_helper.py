import pytest
from basyx.aas import model

from aas_standard_parser.descriptor_json_helper import parse_endpoint_href


@pytest.fixture(scope="module")
def href() -> model.Property:
    # create a Submodel
    return "http://aas-server:8075/shells/aHR0cHM6Ly9mbHVpZDQwLmRlL2lkcy9zaGVsbC81NzkzXzU0NDlfNzgzMF80MjIz"

def test_001_get_mapping_configuration_root_element(href: str):
    href_data = parse_endpoint_href(href)

    assert href_data is not None
    assert href_data.base_url == "http://aas-server:8075"
    assert href_data.identifier == "aHR0cHM6Ly9mbHVpZDQwLmRlL2lkcy9zaGVsbC81NzkzXzU0NDlfNzgzMF80MjIz"
    assert href_data.identifier_encoded == "https://fluid40.de/ids/shell/5793_5449_7830_4223"
