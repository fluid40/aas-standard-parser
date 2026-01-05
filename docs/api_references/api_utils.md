# 🛠️ API Reference: utils.py


This module provides utility functions for the AAS standard parser.

---

## Functions

### create_submodel_from_file(file_path: str) -> model.Submodel

Creates a Submodel from a given file path.

**Parameters:**
- `file_path` (str): Path to the file containing the submodel data (JSON format).

**Returns:**
- `model.Submodel`: The created Submodel object.

**Raises:**
- `FileNotFoundError`: If the specified file does not exist.

**Description:**
- Loads a submodel from a JSON file and converts it into a `model.Submodel` object using the AAS HTTP client SDK tools.

---
