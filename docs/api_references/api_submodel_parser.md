# 🔎 API Reference: submodel_parser.py

This module provides functions for parsing and traversing submodels in the AAS standard parser.

## Usage

To use `submodel_parser.py`, import the module and call its functions as needed. For example, to retrieve a submodel element by its idShort path:

```python
from aas_standard_parser import submodel_parser

submodel_element = submodel_parser.get_submodel_element_by_id_short_path(submodel, 'Element1.Element2[0].Element3')
# Now you can work with the `submodel_element` as needed.
```

---

## Functions

```python
get_submodel_element_by_id_short_path(submodel: model.Submodel, id_short_path: str) -> model.SubmodelElement
```
Retrieve a specific submodel element from the submodel at a specific idShort path.

**Parameters:**
- `submodel` (`model.Submodel`): The submodel to search within.
- `id_short_path` (`str`): IdShort path to the submodel element (dot-separated), e.g., "Element1.Element2[0].Element3".

**Returns:**
- `model.SubmodelElement` or `None`: The found submodel element, or None if not found.

**Description:**
- Traverses the submodel structure using the provided dot-separated idShort path. Supports indexed access for lists, e.g., "Element1.Element2[0].Element3". Returns None if any part of the path does not exist or an index is out of range.

---
