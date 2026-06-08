"""Helper classes for descriptor JSON parsing."""


class EndPointHrefData:
    """Class to represent an endpoint href data structure."""

    def __init__(self, href: str):
        """Initialize the EndPointHrefData with the given href."""
        self.href: str = href
        self.base_url: str = ""
        self.identifier: str = ""
        self.identifier_decoded: str = ""
        self.tag: str = ""


class DescriptorData:
    """Class to represent the descriptor data structure."""

    def __init__(self, identifier_decoded: str):
        """Initialize the DescriptorData with the given descriptor data."""
        self.identifier_decoded: str = identifier_decoded
        self.identifier: str = ""
        self.endpoints: list[dict] = []
        self.hrefs: list[str] = []
        self.hrefs_data: list[dict[str, EndPointHrefData]] = []
        self.description: dict = {}
        self.main_description: str = ""
        self.display_name: dict = {}
        self.main_display_name: str = ""
        self.assetKind = ""
        self.id_short = ""
        self.semantic_id = ""
        self.supplementary_semantic_ids: list[str] = []
