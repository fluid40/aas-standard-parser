"""Module for parsing submodels."""

import logging

from basyx.aas import model

from aas_standard_parser import aas_parser

_logger = logging.getLogger(__name__)


def get_description_from_submodel(submodel: model.Submodel, preferred_languages: list[str] | None = None) -> str | None:
    """Get the description from a Submodel.

    :param submodel: The Submodel to extract the description from.
    :param preferred_languages: A list of preferred languages to extract the description from, in order of preference. Defaults to ["en", "de"].
    :return: The description string if found, otherwise None.
    """
    if preferred_languages is None:
        preferred_languages = ["en", "de"]

    if submodel.description is None:
        _logger.debug(f"No description found for concept description '{submodel.id_short}'")
        return None

    return aas_parser.extract_multi_language_object(submodel.description, preferred_languages=preferred_languages)


def get_display_name_from_submodel(submodel: model.Submodel, preferred_languages: list[str] | None = None) -> str | None:
    """Get the display name from a Submodel.

    :param submodel: The Submodel to extract the display name from.
    :param preferred_languages: A list of preferred languages to extract the display name from, in order of preference. Defaults to ["en", "de"].
    :return: The display name string if found, otherwise None.
    """
    if preferred_languages is None:
        preferred_languages = ["en", "de"]

    if submodel.display_name is None:
        _logger.debug(f"No display name found for submodel '{submodel.id_short}'")
        return None

    return aas_parser.extract_multi_language_object(submodel.display_name, preferred_languages=preferred_languages)


def get_submodel_element_by_id_short_path(submodel: model.Submodel, id_short_path: str) -> model.SubmodelElement:
    """Retrieve a specific submodel element from the submodel at a specific idShort path.

    :param submodel: The submodel to search within.
    :param id_short_path: IdShort path to the submodel element (dot-separated), e.g., "Element1.Element2[0].Element3".
    :return: The found submodel element or None if not found.
    """
    # Split the path by '.' and traverse the structure
    parts = id_short_path.split(".")
    current_elements = submodel.submodel_element
    part_index = 0
    for part in parts:
        part_index += 1
        # Handle indexed access like "Element[0]" for SubmodelElementLists
        if "[" in part and "]" in part:
            # Split SubmodelElementList name and index
            base, idx = part[:-1].split("[")
            idx = int(idx)
            # Find the SubmodelElementList in the current elements
            submodel_element = next((el for el in current_elements if el.id_short == base), None)

            if not submodel_element or not (isinstance(submodel_element, (model.SubmodelElementList, model.SubmodelElementCollection))):
                _logger.debug(f"Submodel element '{base}' not found or is not a collection/list in current {current_elements}.")
                return None

            # Check if index is within range
            if idx >= len(submodel_element.value):
                _logger.debug(f"Index '{idx}' out of range for element '{base}' with length {len(submodel_element.value)}.")
                return None

            # get the element by its index from SubmodelElementList
            submodel_element = submodel_element.value[idx]

        else:
            # Find the SubmodelElement in the current SubmodelElementCollection
            submodel_element = next((el for el in current_elements if el.id_short == part), None)

        if not submodel_element:
            _logger.debug(f"Submodel element '{part}' not found in current {current_elements}.")
            return None

        # If we've reached the last part, return the found element
        if part_index == len(parts):
            return submodel_element

        # If the found element is a collection or list, continue traversing
        if isinstance(submodel_element, (model.SubmodelElementCollection, model.SubmodelElementList)):
            current_elements = submodel_element.value
        else:
            return submodel_element

    return submodel_element


def get_semantic_id_value_from_submodel(submodel: model.Submodel, index: int = 0) -> str | None:
    """Get the semantic ID from a submodel.

    :param submodel: The submodel to extract the semantic ID from.
    :param index: The index of the semantic ID key to retrieve.
    :return: The semantic ID string if found, otherwise None.
    """
    if submodel.semantic_id is None or index >= len(submodel.semantic_id.key):
        _logger.warning(f"No semantic ID found for submodel '{submodel.id_short}'")
        return None

    return submodel.semantic_id.key[index].value
