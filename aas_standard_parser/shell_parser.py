"""Module for parsing Shells."""

import logging

from basyx.aas import model

from aas_standard_parser import aas_parser

_logger = logging.getLogger(__name__)


def get_submodel_ids(shell: model.AssetAdministrationShell) -> list[str]:
    """Get all IDs from the submodels referenced in the given AAS.

    :param shell: The Asset Administration Shell to extract submodel IDs from.
    :return: A list of submodel IDs referenced in the AAS.
    """
    submodel_ids = []
    for submodel in shell.submodel:
        if len(submodel.key) < 1 or submodel.key[0].type != model.KeyTypes.SUBMODEL:
            _logger.warning(f"Submodel reference {submodel} does not start with SUBMODEL key type.")
            continue

        submodel_ids.append(submodel.key[0].value)

    return submodel_ids


def get_description_from_shell(shell: model.AssetAdministrationShell, preferred_languages: list[str] | None = None) -> str | None:
    """Get the description from an Asset Administration Shell.

    :param shell: The Asset Administration Shell to extract the description from.
    :param preferred_languages: A list of preferred languages to extract the description from, in order of preference. Defaults to ["en", "de"].
    :return: The description string if found, otherwise None.
    """
    if preferred_languages is None:
        preferred_languages = ["en", "de"]

    if shell.description is None:
        _logger.debug(f"No description found for shell '{shell.id_short}'")
        return None

    return aas_parser.extract_multi_language_object(shell.description, preferred_languages=preferred_languages)


def get_display_name_from_shell(shell: model.AssetAdministrationShell, preferred_languages: list[str] | None = None) -> str | None:
    """Get the display name from an Asset Administration Shell.

    :param shell: The Asset Administration Shell to extract the display name from.
    :param preferred_languages: A list of preferred languages to extract the display name from, in order of preference. Defaults to ["en", "de"].
    :return: The display name string if found, otherwise None.
    """
    if preferred_languages is None:
        preferred_languages = ["en", "de"]

    if shell.display_name is None:
        _logger.debug(f"No display name found for shell '{shell.id_short}'")
        return None

    return aas_parser.extract_multi_language_object(shell.display_name, preferred_languages=preferred_languages)
