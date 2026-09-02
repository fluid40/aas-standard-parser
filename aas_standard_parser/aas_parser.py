"""Module for parsing AAS."""

import json
import logging
from pathlib import Path

from basyx.aas import model

from aas_standard_parser.classes.env_parser_classes import EnvironmentData

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


def parse_environment_file(file_path: str) -> EnvironmentData | None:
    """Parse an environment file and return an EnvironmentData instance.

    :param file_path: The path to the environment file to parse.
    :return: An EnvironmentData instance containing the parsed data.
    """
    file = Path(file_path)
    if not file.exists():
        raise FileNotFoundError(f"Submodel structure file not found: {file}")

    try:
        with file.open("r", encoding="utf-8") as f:
            json_content = json.load(f)
    except json.JSONDecodeError as e:
        _logger.error(f"Failed to parse JSON file '{file}': {e}")
        return None

    if not json_content or not isinstance(json_content, dict):
        _logger.error(f"File '{file}' does not contain valid environment data.")
        return None

    env_content = EnvironmentData(file_name=file.name, file=file)
    env_content.submodels = _parse_node("submodels", json_content)
    env_content.concept_descriptions = _parse_node("conceptDescriptions", json_content)
    env_content.shells = _parse_node("assetAdministrationShells", json_content)

    return env_content


def get_description_from_shell(shell: model.AssetAdministrationShell, language: str = "en") -> str | None:
    """Get the description from an Asset Administration Shell.

    :param shell: The Asset Administration Shell to extract the description from.
    :param language: The language code for the description.
    :return: The description string if found, otherwise None.
    """
    if shell.description is None:
        _logger.warning(f"No description found for shell {shell.id_short}")
        return None

    keys = shell.description.keys()

    if keys is None or len(keys) == 0:
        _logger.warning(f"No description keys found for shell {shell.id_short}")
        return None

    if language not in keys:
        _logger.warning(f"Description for language '{language}' not found in shell {shell.id_short}")
        return None

    return shell.description.get(language)


def get_display_name_from_submodel(shell: model.AssetAdministrationShell, language: str = "en") -> str | None:
    """Get the display name from an Asset Administration Shell.

    :param shell: The Asset Administration Shell to extract the display name from.
    :param language: The language code for the display name.
    :return: The display name string if found, otherwise None.
    """
    if shell.display_name is None:
        _logger.warning(f"No display name found for shell {shell.id_short}")
        return None

    keys = shell.display_name.keys()

    if keys is None or len(keys) == 0:
        _logger.warning(f"No display name keys found for shell {shell.id_short}")
        return None

    if language not in keys:
        _logger.warning(f"Display name for language '{language}' not found in shell {shell.id_short}")
        return None

    return shell.display_name.get(language)


def _parse_node(node: str, json_content: dict) -> list[dict]:
    if not json_content or not isinstance(json_content, dict) or node not in json_content:
        return []

    content_list = json_content[node]

    if not content_list or not isinstance(content_list, list):
        return []

    return content_list
