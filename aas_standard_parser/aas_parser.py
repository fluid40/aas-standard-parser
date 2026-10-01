"""Module for parsing AAS in general."""

import json
import logging
from pathlib import Path
from typing import Any

from aas_standard_parser.classes.env_parser_classes import EnvironmentData

_logger = logging.getLogger(__name__)


def extract_multi_language_dict(multi_language_dict: dict, preferred_languages: list[str] | None = None) -> str | None:
    """Extract a readable text from BaSyx multilingual text/name containers.

    :param multi_language_dict: A dictionary containing multilingual text with language codes as keys.
    :param preferred_languages: A list of preferred languages to extract the text from, in order of preference. Defaults to ["en", "de"].
    :return: The extracted text in the preferred language, or the first available text if none of the preferred languages are found, or None if no text is available.
    """
    if preferred_languages is None:
        preferred_languages = ["en", "de"]

    if multi_language_dict is None:
        return None

    if len(multi_language_dict) == 0:
        return None

    for language in preferred_languages:
        try:
            text = multi_language_dict.get(language)
        except AttributeError:
            text = None
        if text:
            return str(text)

    try:
        first_value = next(iter(multi_language_dict.values()))
    except (AttributeError, StopIteration):
        first_value = None

    return str(first_value) if first_value else None


def extract_multi_language_object(multi_language_object: Any, preferred_languages: list[str] | None = None) -> str | None:
    """Extract a readable text from BaSyx multilingual text/name containers.

    :param multi_language_dict: A dictionary containing multilingual text with language codes as keys.
    :param preferred_languages: A list of preferred languages to extract the text from, in order of preference. Defaults to ["en", "de"].
    :return: The extracted text in the preferred language, or the first available text if none of the preferred languages are found, or None if no text is available.
    """
    if preferred_languages is None:
        preferred_languages = ["en", "de"]

    if multi_language_object is None:
        return None

    keys = multi_language_object.keys()

    if not keys or len(keys) == 0:
        return None

    for language in preferred_languages:
        if language in keys:
            return str(multi_language_object.get(language))

    return str(multi_language_object.get(next(iter(keys)))) if keys else None


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
