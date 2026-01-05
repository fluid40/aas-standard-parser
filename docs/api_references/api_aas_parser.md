# 🛠️ API Reference: aas_parser.py


This module provides functions for parsing Asset Administration Shells (AAS) in the AAS standard parser.

## Usage

To use `aas_parser.py`, import the module and call its functions as needed. For example, to extract all submodel IDs from an AAS:

```python
from aas_standard_parser import aas_parser

submodel_ids = aas_parser.get_submodel_ids(shell)
# `submodel_ids` is now a list of all submodel IDs referenced in the given AAS.
```

---

## Functions

```python
get_submodel_ids(shell: model.AssetAdministrationShell) -> list[str]
```
Get all IDs from the submodels referenced in the given Asset Administration Shell (AAS).

**Parameters:**
- `shell` (`model.AssetAdministrationShell`): The Asset Administration Shell to extract submodel IDs from.

**Returns:**
- `list[str]`: A list of submodel IDs referenced in the AAS.

**Description:**
- Iterates through the submodel references in the provided AAS and collects their IDs. Skips references that do not start with the SUBMODEL key type.

---
