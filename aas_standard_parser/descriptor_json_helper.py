"""Module for parsing descriptor JSON data."""

import logging

from aas_standard_parser.classes.descriptor_json_helper_classes import EndPointHrefData
from aas_standard_parser.utils import decode_base_64, encode_base_64

logger = logging.getLogger(__name__)


def get_endpoint_href_by_index(descriptor_data: dict, endpoint_index: int = 0) -> str | None:
    """Get the href from a descriptor's endpoints.

    :param descriptor_data: The descriptor data containing endpoints.
    :param endpoint_index: The index of the endpoint to extract the href from.
    :return: The href string if found, otherwise None.
    """
    endpoints = get_endpoint_hrefs(descriptor_data)

    if not endpoints or len(endpoints) == 0:
        logger.warning(f"No endpoints found in descriptor {descriptor_data}")
        return None

    if endpoint_index >= len(endpoints):
        logger.warning(f"Endpoint index {endpoint_index} out of range for descriptor {descriptor_data}")
        return None

    return endpoints[endpoint_index]


def get_endpoint_hrefs(descriptor_data: dict) -> list[str]:
    """Get all hrefs from a descriptor's endpoints.

    :param descriptor_data: The descriptor data containing endpoints.
    :return: A list of href strings extracted from the endpoints.
    """
    return [endpoint.get("protocolInformation", {}).get("href", "") for endpoint in descriptor_data.get("endpoints", [])]


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
    href_data.identifier_encoded = encode_base_64(identifier)

    return href_data
