# AAS standard Parser

[![PyPI version](https://img.shields.io/pypi/v/aas-standard-parser.svg)](https://pypi.org/project/aas-standard-parser/)
[![License: MIT](https://img.shields.io/badge/license-MIT-%23f8a602?label=License&labelColor=%23992b2e)](LICENSE)
[![CI](https://github.com/fluid40/aas-standard-parser/actions/workflows/CI.yml/badge.svg?branch=main&cache-bust=1)](https://github.com/fluid40/aas-standard-parser/actions)

This project provides tools for parsing and handling Asset Administration Shell (AAS) standard submodels, with a focus on AID and AIMC submodels. It enables:

* Extraction, interpretation, and mapping of submodel elements and their properties
* Working with references, semantic IDs, and submodel element collections
* Representation and processing of mapping configurations and source-sink relations
* Structured and colored logging, including log file management

These components enable efficient parsing, transformation, and analysis of AAS submodels in Python-based workflows.

**Notes:**

* Most functions in this project utilize the [python aas sdk framework](https://github.com/aas-core-works/aas-core3.0-python) for parsing and handling AAS submodels, ensuring compatibility with the official AAS data models and structures.

* [AAS standard Parser](#aas-standard-parser)
  + [🚀 Features](#-features)
  + [📚 Resources](#-resources)

---

## 🚀 Features

### Comprehensive AAS Submodel Parsing

* ✅ Parse and extract data from AAS structures, with specialized support for AID and AIMC submodels
* ✅ Navigate hierarchical submodel elements using intuitive dot-separated paths and indexed access
* ✅ Extract endpoint metadata, interface properties, authentication details, and mapping configurations

### Core Parsers

* ✅ **AAS Parser**: Retrieve submodel IDs and references from Asset Administration Shell structures
* ✅ **Submodel Parser**: Access nested elements by idShort path with support for SubmodelElementLists and Collections
* ✅ **AID Parser**: Extract interface descriptions, properties, protocol bindings, and authentication details
* ✅ **AIMC Parser**: Parse mapping configurations and source-sink relations between interfaces

### Utility Functions

* ✅ Collection and reference helpers for semantic ID matching, filtering, and key extraction
* ✅ Load and validate submodels from JSON files with error handling
* ✅ Structured JSON logging with colored console output

---

## 📚 Resources

📘 [Documentation](https://fluid40.github.io/aas-standard-parser/)

📝 [Changelog](docs/CHANGELOG.md)

🤖 [GitHub Releases](https://github.com/fluid40/aas-standard-parser/releases)

📦 [Pypi Packages](https://pypi.org/project/aas-standard-parser/)

📜 [MIT License](https://github.com/fluid40/aas-standard-parser/blob/main/LICENSE)

---
