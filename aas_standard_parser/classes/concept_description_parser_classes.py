"""Helper classes for concept description parsing."""


class DataSpecificationContent:
    """Class to represent a data specification content structure."""

    value: str
    value_format: str
    value_list: list
    symbol: str
    definition: str
    data_type: dict
    model_type: str
    short_name: str
    unit: str
    unit_id: str
    preferred_name: str

    def __init__(self):
        """Initialize the data specification content with default values."""
        self.value = ""
        self.value_format = ""
        self.value_list = []
        self.symbol = ""
        self.definition = ""
        self.data_type = {}
        self.model_type = ""
        self.short_name = ""
        self.unit = ""
        self.unit_id = ""
        self.preferred_name = ""


class ConceptDescriptionData:
    """Class to represent a concept description data structure."""

    main_display_name: str
    main_description: str
    display_name: dict
    description: dict
    id: str
    id_short: str
    data_specification_content: list[DataSpecificationContent]

    def __init__(self, id: str, id_short: str):
        """Initialize the concept description data with ID and short ID."""
        self.main_display_name = ""
        self.main_description = ""
        self.display_name = {}
        self.description = {}
        self.id = id
        self.id_short = id_short
        self.data_specification_content = []
