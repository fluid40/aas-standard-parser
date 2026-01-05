"""Utility functions for AAS standard parser."""

import json
from pathlib import Path

from aas_http_client import sdk_tools
from basyx.aas import model


def create_submodel_from_file(file_path: str) -> model.Submodel:
    """Loads a Submodel structure from a given JSON file and converts it into a model.Submodel object from the python SDK framework.

    :param file_path: Path to the JSON file containing the Submodel structure.
    :return: A model.Submodel object representing the loaded Submodel structure.
    """
    file = Path(file_path)
    if not file.exists():
        raise FileNotFoundError(f"Submodel structure file not found: {file}")

    template_data = {}

    # Load the template JSON file
    with file.open("r", encoding="utf-8") as f:
        template_data = json.load(f)

    # Load the template JSON into a Submodel object
    return sdk_tools.convert_to_object(template_data)
