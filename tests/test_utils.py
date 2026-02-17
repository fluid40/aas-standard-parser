import pytest
from aas_standard_parser import utils

def test_001a_decode_base_64():
    encoded = "RW5lcmd5TW9uaXRvcmluZw"

    decoded = utils.decode_base_64(encoded)
    assert decoded == "EnergyMonitoring"
    new_encoded = utils.encode_base_64(decoded)
    assert new_encoded == encoded


def test_001b_decode_base_64():
    encoded = "aHR0cHM6Ly9mbHVpZDQwLmRlL2lkcy9zbS8xNTE1XzUzMDZfNzYyNF81MzY3"

    decoded = utils.decode_base_64(encoded)
    assert decoded == "https://fluid40.de/ids/sm/1515_5306_7624_5367"
    new_encoded = utils.encode_base_64(decoded)
    assert new_encoded == encoded

def test_002a_encode_base_64():
    decoded = "EnergyMonitoring"

    encoded = utils.encode_base_64(decoded)
    assert encoded == "RW5lcmd5TW9uaXRvcmluZw"
    new_decoded = utils.decode_base_64(encoded)
    assert new_decoded == decoded

def test_002b_encode_base_64():
    decoded = "https://fluid40.de/ids/sm/1515_5306_7624_5367"

    encoded = utils.encode_base_64(decoded)
    assert encoded == "aHR0cHM6Ly9mbHVpZDQwLmRlL2lkcy9zbS8xNTE1XzUzMDZfNzYyNF81MzY3"
    new_decoded = utils.decode_base_64(encoded)
    assert new_decoded == decoded

def test_003_decode_with_padding():
    """Test decoding base64 strings with padding"""
    encoded_with_padding = "RW5lcmd5TW9uaXRvcmluZw"
    decoded = utils.decode_base_64(encoded_with_padding)
    assert decoded == "EnergyMonitoring"

def test_004_empty_string():
    """Test encoding and decoding empty string"""
    decoded = ""
    encoded = utils.encode_base_64(decoded)
    assert encoded == ""
    new_decoded = utils.decode_base_64(encoded)
    assert new_decoded == decoded

def test_005_special_characters():
    """Test encoding and decoding strings with special characters"""
    decoded = "Hello@World#123!"
    encoded = utils.encode_base_64(decoded)
    new_decoded = utils.decode_base_64(encoded)
    assert new_decoded == decoded

def test_006_unicode_characters():
    """Test encoding and decoding unicode strings"""
    decoded = "Hällo Wörld 你好"
    encoded = utils.encode_base_64(decoded)
    new_decoded = utils.decode_base_64(encoded)
    assert new_decoded == decoded

def test_007_single_padding():
    """Test decoding with single padding character"""
    encoded = "SGVsbG8="
    decoded = utils.decode_base_64(encoded)
    assert decoded == "Hello"

def test_008_roundtrip_consistency():
    """Test that encode then decode returns original string"""
    test_strings = ["test", "123", "special@#$", "a", ""]
    for test_str in test_strings:
        encoded = utils.encode_base_64(test_str)
        decoded = utils.decode_base_64(encoded)
        assert decoded == test_str
