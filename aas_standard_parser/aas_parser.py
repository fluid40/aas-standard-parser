"""Module for parsing AAS in general."""

import json
import logging
from pathlib import Path

from aas_standard_parser.classes.env_parser_classes import EnvironmentData

_logger = logging.getLogger(__name__)


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
