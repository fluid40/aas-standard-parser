"""Module for parsing AAS in general."""

from typing import Any


def parse_multi_language_object(multi_language_object: Any, preferred_languages: list[str] | None = None) -> str:
    """Extract a readable text from BaSyx multilingual text/name containers.

    :param multi_language_object: A dictionary containing multilingual text with language codes as keys.
    :param preferred_languages: A list of preferred languages to extract the text from, in order of preference. Defaults to ["en", "de"].
    :return: The extracted text in the preferred language, or the first available text if none of the preferred languages are found, or an empty string if no text is available.
    """
    if preferred_languages is None:
        preferred_languages = ["en", "de"]

    if multi_language_object is None:
        return ""

    keys = multi_language_object.keys()

    if not keys or len(keys) == 0:
        return ""

    for language in preferred_languages:
        if language in keys:
            return str(multi_language_object.get(language))

    return str(multi_language_object.get(next(iter(keys)))) if keys else ""


def parse_multi_language_list(multi_language_list: list[dict], preferred_languages: list[str] | None = None) -> str:
    """Extract a readable text from BaSyx multilingual text/language dictionaries.

    :param multi_language_list: A list of dictionaries containing multilingual text with language codes as keys.
    :param preferred_languages: A list of preferred languages to extract the text from, in order of preference. Defaults to ["en", "de"].
    :return: The extracted text in the preferred language, or the first available text if none of the preferred languages are found, or an empty string if no text is available.
    """
    if preferred_languages is None:
        preferred_languages = ["en", "de"]

    if multi_language_list is None or len(multi_language_list) == 0:
        return ""

    for language in preferred_languages:
        for multi_language_dict in multi_language_list:
            value = multi_language_dict.get("language", "")
            text = multi_language_dict.get("text", "") if value == language else ""

            if text:
                return str(text)

    for multi_language_dict in multi_language_list:
        try:
            text = multi_language_dict.get("text", "")
        except AttributeError:
            text = ""

        if text:
            return str(text)

    return ""


def parse_multi_language_dict(multi_language_dict: dict, preferred_languages: list[str] | None = None) -> str:
    """Extract a readable text from BaSyx multilingual text/name containers.

    :param multi_language_dict: A dictionary containing multilingual text with language codes as keys.
    :param preferred_languages: A list of preferred languages to extract the text from, in order of preference. Defaults to ["en", "de"].
    :return: The extracted text in the preferred language, or the first available text if none of the preferred languages are found, or None if no text is available.
    """
    if preferred_languages is None:
        preferred_languages = ["en", "de"]

    if multi_language_dict is None:
        return ""

    for language in preferred_languages:
        try:
            text = multi_language_dict.get(language)
        except AttributeError:
            text = ""
        if text:
            return str(text)

    try:
        first_value = next(iter(multi_language_dict.values()))
    except (AttributeError, StopIteration):
        first_value = ""

    return str(first_value) if first_value else ""
