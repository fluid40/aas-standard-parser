# 🛠️ API Reference: utils.py

This module provides utility functions for the AAS standard parser.

## Usage

To use `utils.py`, simply import the module and call its functions as needed. For example, to load a submodel from a JSON file:

```python
from aas_standard_parser import utils

submodel = utils.create_submodel_from_file('path/to/your/submodel.json')
# Now you can work with the `submodel` object as defined by the AAS Python SDK.
```

---

## Functions

```python
create_submodel_from_file(file_path: str) -> model.Submodel
```
Loads a Submodel structure from a given JSON file and converts it into a model.Submodel object from the python SDK framework.

**Parameters:**
- `file_path` (str): Path to the JSON file containing the Submodel structure.

**Returns:**
- `model.Submodel`: A model.Submodel object representing the loaded Submodel structure.

**Raises:**
- `FileNotFoundError`: If the specified file does not exist.

**Description:**
Reads the specified JSON file, parses its contents, and constructs a `model.Submodel` object using the data. This function abstracts away file handling and parsing logic, allowing users to easily instantiate submodels from JSON definitions compatible with the AAS Python SDK.

---
