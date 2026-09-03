"""Module for parsing Concept Descriptions."""

import logging

from basyx.aas import model

from aas_standard_parser import aas_parser

_logger = logging.getLogger(__name__)


def get_description_from_concept_description(
    concept_description: model.concept.ConceptDescription, preferred_languages: list[str] | None = None
) -> str | None:
    """Get the description from a Concept Description.

    :param concept_description: The Concept Description to extract the description from.
    :param preferred_languages: A list of preferred languages to extract the description from, in order of preference. Defaults to ["en", "de"].
    :return: The description string if found, otherwise None.
    """
    if preferred_languages is None:
        preferred_languages = ["en", "de"]

    if concept_description.description is None:
        _logger.debug(f"No description found for concept description '{concept_description.id_short}'")
        return None

    return aas_parser.extract_multi_language_object(concept_description.description, preferred_languages=preferred_languages)


def get_display_name_from_concept_description(
    concept_description: model.concept.ConceptDescription, preferred_languages: list[str] | None = None
) -> str | None:
    """Get the display name from a Concept Description.

    :param concept_description: The Concept Description to extract the display name from.
    :param preferred_languages: A list of preferred languages to extract the display name from, in order of preference. Defaults to ["en", "de"].
    :return: The display name string if found, otherwise None.
    """
    if preferred_languages is None:
        preferred_languages = ["en", "de"]

    if concept_description.display_name is None:
        _logger.debug(f"No display name found for concept description '{concept_description.id_short}'")
        return None

    return aas_parser.extract_multi_language_object(concept_description.display_name, preferred_languages=preferred_languages)
