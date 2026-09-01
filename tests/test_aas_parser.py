import pytest

from aas_standard_parser.aas_parser import parse_environment_file
from pathlib import Path



def test_001_parse_environment_file():
    environment_file = Path("tests/test_data/environment.json")

    env_data = parse_environment_file(environment_file)
    assert env_data is not None
    assert env_data.file_name == "environment.json"
    assert env_data.file == environment_file
    assert isinstance(env_data.submodels, list)
    assert isinstance(env_data.concept_descriptions, list)
    assert isinstance(env_data.shells, list)
    assert len(env_data.shells) == 1
    assert len(env_data.submodels) == 1
    assert len(env_data.concept_descriptions) > 0
