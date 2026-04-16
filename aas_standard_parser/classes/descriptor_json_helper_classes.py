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
