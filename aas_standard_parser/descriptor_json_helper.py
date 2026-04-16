"""Module for parsing descriptor JSON data."""

import logging

from aas_standard_parser.classes.descriptor_json_helper_classes import EndPointHrefData
from aas_standard_parser.utils import decode_base_64

logger = logging.getLogger(__name__)


def get_endpoints(descriptor_data: dict) -> list[dict]:
    """Get all endpoints from a descriptor.

    :param descriptor_data: The descriptor data containing endpoints.
    :return: A list of endpoint dictionaries extracted from the descriptor.
    """
    return descriptor_data.get("endpoints", [])


def get_endpoint_by_index(descriptor_data: dict, endpoint_index: int = 0) -> dict | None:
    """Get the endpoint from a descriptor's endpoints by index.

    :param descriptor_data: The descriptor data containing endpoints.
    :param endpoint_index: The index of the endpoint to extract.
    :return: The endpoint dictionary if found, otherwise None.
    """
    endpoints = get_endpoints(descriptor_data)

    if not endpoints or len(endpoints) == 0:
        logger.warning(f"No endpoints found in descriptor {descriptor_data}")
        return None

    if endpoint_index >= len(endpoints):
        logger.warning(f"Endpoint index {endpoint_index} out of range for descriptor {descriptor_data}")
        return None

    return endpoints[endpoint_index]


def get_endpoint_protocol_information_by_index(descriptor_data: dict, endpoint_index: int = 0) -> dict | None:
    """Get the protocol information from a descriptor's endpoints by index.

    :param descriptor_data: The descriptor data containing endpoints.
    :param endpoint_index: The index of the endpoint to extract the protocol information from.
    :return: The protocol information dictionary if found, otherwise None.
    """
    endpoint = get_endpoint_by_index(descriptor_data, endpoint_index)

    if endpoint is None:
        logger.warning(f"Endpoint at index {endpoint_index} not found in descriptor {descriptor_data}")
        return None

    return endpoint.get("protocolInformation", {})


def get_endpoint_href_by_index(descriptor_data: dict, endpoint_index: int = 0) -> str | None:
    """Get the href from a descriptor's endpoints.

    :param descriptor_data: The descriptor data containing endpoints.
    :param endpoint_index: The index of the endpoint to extract the href from.
    :return: The href string if found, otherwise None.
    """
    protocol_info = get_endpoint_protocol_information_by_index(descriptor_data, endpoint_index)

    if not protocol_info:
        logger.warning(f"No protocol information found for endpoint at index {endpoint_index} in descriptor {descriptor_data}")
        return None

    return protocol_info.get("href", "")


def get_endpoint_hrefs(descriptor_data: dict) -> list[str]:
    """Get all hrefs from a descriptor's endpoints.

    :param descriptor_data: The descriptor data containing endpoints.
    :return: A list of href strings extracted from the endpoints.
    """
    endpoints = get_endpoints(descriptor_data)

    return [endpoint.get("protocolInformation", {}).get("href", "") for endpoint in endpoints]


def parse_endpoint_href(href: str) -> EndPointHrefData | None:
    """Parse the endpoint href into its components.

    :param href: The href string to parse.
    :return: An EndPointHrefData object containing parsed components.
    """
    if "shells/" not in href and "submodels/" not in href:
        logger.warning(f"Invalid href format: {href}")
        return None

    split_str = ""
    if "/shells/" in href:
        split_str = "/shells/"
    elif "/submodels/" in href:
        split_str = "/submodels/"

    base_url: str = href.split(split_str, maxsplit=1)[0]
    identifier: str = href.split(split_str)[1]

    href_data = EndPointHrefData(href)
    href_data.base_url = base_url
    href_data.identifier = identifier
    try:
        href_data.identifier_encoded = decode_base_64(identifier)
    except Exception as e:
        logger.error(f"Failed to decode identifier '{identifier}' from href '{href}': {e}")

    return href_data
