# 🧩 API Reference: reference_helpers.py

This module provides helper functions for working with ModelReference objects in the AAS standard parser.

## Usage

To use `reference_helpers.py`, import the module and call its functions as needed. For example, to construct an idShort path from a ModelReference:

```python
from aas_standard_parser import reference_helpers

id_short_path = construct_id_short_path_from_reference.construct_id_short_path_from_reference(reference)
# `id_short_path` is now a string representing the path from the ModelReference.
```

---

## Functions


```python
construct_id_short_path_from_reference(reference: ModelReference) -> str
```

**Parameters:**
- `reference` (`ModelReference`): The ModelReference to construct the idShort path from.

**Returns:**
- `str`: The constructed idShort path as a string.

**Description:**
Constructs a dot-separated idShort path string from the provided ModelReference, omitting the first key (typically the Identifiable root). Useful for navigating or referencing elements in a submodel structure.

---

```python
get_values_from_keys(reference: ModelReference) -> list[str]
```

**Parameters:**
- `reference` (`ModelReference`): Reference to extract values from.

**Returns:**
- `list[str]`: List of values from all keys in the reference.

**Description:**
Extracts and returns a list of all key values from the given ModelReference. This is helpful for analyzing or iterating over the reference path components.

---


```python
get_value_from_key_at_index(reference: ModelReference, index: int) -> str
```

**Parameters:**
- `reference` (`ModelReference`): Reference to extract value from.
- `index` (`int`): Index of the key to get the value from.

**Returns:**
- `str`: Value from the key at the given index.

**Description:**
Returns the value of the key at the specified index in the ModelReference. Allows direct access to a particular segment of the reference path.
---
