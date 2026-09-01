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


def _parse_node(node: str, json_content: dict) -> list[dict]:
    if not json_content or not isinstance(json_content, dict) or node not in json_content:
        return []

    content_list = json_content[node]

    if not content_list or not isinstance(content_list, list):
        return []

    return content_list
