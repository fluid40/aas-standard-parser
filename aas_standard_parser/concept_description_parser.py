"""Module for parsing AAS."""

import logging

from basyx.aas import model

_logger = logging.getLogger(__name__)


def get_description_from_concept_description(concept_description: model.concept.ConceptDescription, language: str = "en") -> str | None:
    """Get the description from a Concept Description.

    :param concept_description: The Concept Description to extract the description from.
    :param language: The language code for the description.
    :return: The description string if found, otherwise None.
    """
    if concept_description.description is None:
        _logger.debug(f"No description found for concept description {concept_description.id_short}")
        return None

    keys = concept_description.description.keys()

    if keys is None or len(keys) == 0:
        _logger.debug(f"No description keys found for concept description {concept_description.id_short}")
        return None

    if language not in keys:
        _logger.debug(f"Description for language '{language}' not found in concept description {concept_description.id_short}")
        return None

    return concept_description.description.get(language)


def get_display_name_from_concept_description(concept_description: model.concept.ConceptDescription, language: str = "en") -> str | None:
    """Get the display name from a Concept Description.

    :param concept_description: The Concept Description to extract the display name from.
    :param language: The language code for the display name.
    :return: The display name string if found, otherwise None.
    """
    if concept_description.display_name is None:
        _logger.debug(f"No display name found for concept description {concept_description.id_short}")
        return None

    keys = concept_description.display_name.keys()

    if keys is None or len(keys) == 0:
        _logger.debug(f"No display name keys found for concept description {concept_description.id_short}")
        return None

    if language not in keys:
        _logger.debug(f"Display name for language '{language}' not found in concept description {concept_description.id_short}")
        return None

    return concept_description.display_name.get(language)
