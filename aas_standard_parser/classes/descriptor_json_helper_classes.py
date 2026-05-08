"""Helper classes for descriptor JSON parsing."""


class EndPointHrefData:
    """Class to represent an endpoint href data structure."""

    def __init__(self, href: str):
        """Initialize the EndPointHrefData with the given href."""
        self.href: str = href
        self.base_url: str = ""
        self.identifier: str = ""
        self.identifier_encoded: str = ""
        self.tag: str = ""


class DescriptorData:
    """Class to represent the descriptor data structure."""

    def __init__(self, identifier: str):
        """Initialize the DescriptorData with the given descriptor data."""
        self.identifier: str = identifier
        self.endpoints: list[dict] = []
        self.description: dict = {}
        self.display_name: dict = {}
        self.assetKind = ""
        self.id_short = ""
        self.semantic_id = ""
        self.supplementary_semantic_ids: list[str] = []
