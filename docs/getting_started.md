# 🚀 Getting Started

This guide will walk you through installing and using `aas-standard-parser` .

- [🚀 Getting Started](#-getting-started)
  - [Overview](#overview)
  - [Installation](#installation)

---

## Overview

**aas-standard-parser** is a Python library for parsing and handling Asset Administration Shell (AAS) standard submodels. It provides a comprehensive set of parsers and utility helpers to extract, interpret, and work with AAS structures.

### Available Parsers

* **AAS Parser**: Extract submodel IDs and references from Asset Administration Shell structures
* **Submodel Parser**: Navigate and retrieve submodel elements using intuitive dot-separated paths with support for nested collections and indexed access
* **AID Parser**: Parse Asset Interface Description (AID) submodels to extract interface metadata, properties, protocol bindings, and authentication details
* **AIMC Parser**: Extract and process Asset Interface Mapping Configuration (AIMC) submodels, including mapping configurations and source-sink relations

### Available Helpers

* **Collection Helpers**: Work with submodel element collections, filter by semantic ID, and extract keys from collections
* **Reference Helpers**: Handle AAS references, semantic IDs, and validate reference structures
* **JSON Helpers**: Load and validate submodels from JSON files with structured error handling
* **Utility Functions**: General-purpose utilities for logging, validation, and data transformation

The library leverages the [python aas sdk framework](https://github.com/aas-core-works/aas-core3.0-python) to ensure compatibility with official AAS data models and structures.

## Installation

Prerequisites:

* Python 3.10 or newer

Install via pip:

```bash
pip install aas-standard-parser
```

---
