from pathlib import Path


class EnvironmentData:
    """Class representing environment data containing submodels, concept descriptions, and shells."""

    file_name: str
    file: Path

    submodels: list[dict]
    concept_descriptions: list[dict]
    shells: list[dict]

    def __init__(self, file_name: str, file: Path):
        """Initialize an EnvironmentData instance.

        :param file_name: The name of the file containing the environment data.
        :param file: The path to the file containing the environment data.
        """
        self.submodels = []
        self.concept_descriptions = []
        self.shells = []
        self.file_name = file_name
        self.file = file
