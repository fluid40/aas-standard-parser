"""Module for parsing Concept Descriptions."""

import logging

from basyx.aas import model

from aas_standard_parser import multi_language_parser, reference_helpers, utils
from aas_standard_parser.classes.concept_description_parser_classes import ConceptDescriptionData, DataSpecificationContent

_logger = logging.getLogger(__name__)


def parse_concept_description(
    concept_description: model.concept.ConceptDescription, preferred_languages: list[str] | None = None
) -> ConceptDescriptionData:
    """Parse a Concept Description into a ConceptDescriptionData containing its display name and description.

    :param concept_description: The Concept Description to parse.
    :param preferred_languages: A list of preferred languages to extract the display name and description from, in order of preference. Defaults to ["en", "de"].
    :return: A ConceptDescriptionData with attributes "display_name" and "description" if found.
    """
    display_name = get_display_name_from_concept_description(concept_description, preferred_languages=preferred_languages)
    description = get_description_from_concept_description(concept_description, preferred_languages=preferred_languages)

    concept_description_data = ConceptDescriptionData(concept_description.id, concept_description.id_short)
    concept_description_data.main_display_name = display_name if display_name is not None else ""
    concept_description_data.main_description = description if description is not None else ""
    concept_description_data.display_name = multi_language_parser.parse_multi_language_object_to_dict(concept_description.display_name)
    concept_description_data.description = multi_language_parser.parse_multi_language_object_to_dict(concept_description.description)

    data_specification = concept_description.embedded_data_specifications

    for embedded_data_spec in data_specification:
        data_spec_content = DataSpecificationContent()
        content = embedded_data_spec.data_specification_content

        if not isinstance(content, model.DataSpecificationIEC61360):
            continue

        ice_content: model.DataSpecificationIEC61360 = content

        data_spec_content.unit = ice_content.unit if ice_content.unit is not None else ""
        data_spec_content.unit_id = ice_content.unit_id.key[0].value if ice_content.unit_id is not None else ""
        data_spec_content.value = content.value if content.value is not None else ""
        data_spec_content.value_format = content.value_format if content.value_format is not None else ""
        data_spec_content.value_list = list(content.value_list) if content.value_list is not None else []
        data_spec_content.symbol = content.symbol if content.symbol is not None else ""
        data_spec_content.definition = multi_language_parser.parse_multi_language_object(content.definition) if content.definition is not None else ""

        data_spec_content.data_type = {"name": content.data_type.name} if content.data_type is not None else {}
        data_spec_content.short_name = multi_language_parser.parse_multi_language_object(content.short_name) if content.short_name is not None else ""
        data_spec_content.preferred_name = (
            multi_language_parser.parse_multi_language_object(content.preferred_name) if content.preferred_name is not None else ""
        )
        # Populate the data_spec_content with relevant information from content if needed
        concept_description_data.data_specification_content.append(data_spec_content)

    return concept_description_data


def parse_concept_description_from_dict(concept_description_dict: dict, preferred_languages: list[str] | None = None) -> ConceptDescriptionData:
    """Parse a Concept Description from a dictionary into a ConceptDescriptionData containing its display name and description.

    :param concept_description_dict: The dictionary representing the Concept Description to parse.
    :param preferred_languages: A list of preferred languages to extract the display name and description from, in order of preference. Defaults to ["en", "de"].
    :return: A ConceptDescriptionData with attributes "display_name" and "description" if found.
    """
    concept_description: model.concept.ConceptDescription = utils.convert_to_object(concept_description_dict)

    if not concept_description:
        raise ValueError("Failed to convert dictionary to ConceptDescription object.")

    return parse_concept_description(concept_description, preferred_languages=preferred_languages)


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

    return multi_language_parser.parse_multi_language_object(concept_description.description, preferred_languages=preferred_languages)


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

    return multi_language_parser.parse_multi_language_object(concept_description.display_name, preferred_languages=preferred_languages)
