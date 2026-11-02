import pytest
from basyx.aas.model import MultiLanguageTextType

from aas_standard_parser import multi_language_parser


def test_parse_multi_language_text_type():
    value = MultiLanguageTextType({"de": "Hallo", "en": "Hello"})

    assert multi_language_parser.parse_multi_language_object(value) == "Hello"


@pytest.mark.parametrize(
    ("value", "preferred_languages", "expected"),
    [
        ({"de": "Hallo", "en": "Hello"}, None, "Hello"),
        ({"en": "Hello", "fr": "Bonjour"}, ["fr", "en"], "Bonjour"),
        ({"fr": "Bonjour", "es": "Hola"}, None, "Bonjour"),
        (None, None, ""),
        ({}, None, ""),
    ],
)
def test_parse_multi_language_object(value, preferred_languages, expected):
    assert multi_language_parser.parse_multi_language_object(value, preferred_languages) == expected


@pytest.mark.parametrize(
    ("value", "preferred_languages", "expected"),
    [
        ({"de": "Hallo", "en": "Hello"}, None, "Hello"),
        ({"en": "Hello", "fr": "Bonjour"}, ["fr", "en"], "Bonjour"),
        ({"fr": "Bonjour", "es": "Hola"}, None, "Bonjour"),
        (None, None, ""),
        ({}, None, ""),
    ],
)
def test_parse_multi_language_dict(value, preferred_languages, expected):
    assert multi_language_parser.parse_multi_language_dict(value, preferred_languages) == expected


@pytest.mark.parametrize(
    ("value", "preferred_languages", "expected"),
    [
        (
            [
                {"language": "de", "text": "Hallo"},
                {"language": "en", "text": "Hello"},
            ],
            None,
            "Hello",
        ),
        (
            [
                {"language": "en", "text": "Hello"},
                {"language": "fr", "text": "Bonjour"},
            ],
            ["fr", "en"],
            "Bonjour",
        ),
        ([{"language": "fr", "text": "Bonjour"}], None, "Bonjour"),
        ([{"language": "fr", "text": ""}], None, ""),
        (None, None, ""),
        ([], None, ""),
    ],
)
def test_parse_multi_language_list(value, preferred_languages, expected):
    assert multi_language_parser.parse_multi_language_list(value, preferred_languages) == expected
