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

### Core Parsing Capabilities

#### **AAS Parser**

* ✅ Extract submodel IDs from Asset Administration Shell structures
* ✅ Validate and retrieve references from AAS to submodels
* ✅ Handle and process AAS metadata and configuration

#### **Submodel Parser**

* ✅ Retrieve submodel elements using idShort paths (dot-separated notation)
* ✅ Support for hierarchical navigation through nested submodel element collections
* ✅ Access SubmodelElementList items by index (e.g.,       `Element[0]`)
* ✅ Extract semantic ID values from submodels
* ✅ Parse complex nested structures with SubmodelElementCollections and Lists

#### **AID Parser** (Asset Interface Descriptions)

* ✅ Parse endpoint metadata and base addresses from interface descriptions
* ✅ Extract and map properties with href attributes
* ✅ Support for hierarchical property traversal with nested key paths
* ✅ Protocol binding configuration extraction:
  + HTTP protocol bindings with method names and custom headers
  + Extensible architecture for additional protocol support
* ✅ Authentication details handling:
  + Basic authentication (username/password)
  + No authentication scenarios
  + Version-aware authentication parsing
* ✅ Interface serialization and deserialization

#### **AIMC Parser** (Asset Interfaces Mapping Configuration)

* ✅ Extract mapping configurations from AIMC submodels
* ✅ Parse source-sink relations and reference properties
* ✅ Handle mapping configuration elements and their hierarchies
* ✅ Support for complex mapping scenarios between interfaces
* ✅ Mapping configuration metadata processing

### Helper Modules

* ✅ **Collection Helpers**: Search and filter submodel elements by:
  + Semantic ID matching
  + idShort names
  + Supplemental semantic IDs
  + Nested collection traversal

* ✅ **Reference Helpers**: Work with references and semantic identifiers:
  + Construct idShort paths from reference structures
  + Extract values from reference keys
  + Handle reference key types and hierarchies

* ✅ **Utilities**: General-purpose functions:
  + Load submodels from JSON files
  + Support for various file formats
  + Error handling and validation

---

## 📚 Resources

📘 [Documentation](https://fluid40.github.io/aas-standard-parser/)

📝 [Changelog](docs/CHANGELOG.md)

🤖 [GitHub Releases](https://github.com/fluid40/aas-standard-parser/releases)

📦 [Pypi Packages](https://pypi.org/project/aas-standard-parser/)

📜 [MIT License](https://github.com/fluid40/aas-standard-parser/blob/main/LICENSE)

---
