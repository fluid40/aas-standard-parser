"""Module for parsing descriptor JSON data."""

import logging

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
