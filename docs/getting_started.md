# 🚀 Getting Started

This guide will walk you through installing and using `aas-standard-parser` .

- [🚀 Getting Started](#-getting-started)
  - [Overview](#overview)
    - [Available Parsers](#available-parsers)
    - [Available Helpers](#available-helpers)
  - [Installation](#installation)
  - [Usage](#usage)
    - [AAS Parser](#aas-parser)
    - [Submodel Parser](#submodel-parser)
    - [AID Parser](#aid-parser)
    - [AIMC Parser](#aimc-parser)
    - [Collection Helpers](#collection-helpers)
    - [Reference Helpers](#reference-helpers)
    - [Submodel JSON Helper](#submodel-json-helper)
    - [Descriptor JSON Helper](#descriptor-json-helper)
    - [Utilities](#utilities)

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

## Usage

The examples below use the parser modules directly. In most workflows, you start by loading a submodel JSON file into a BaSyx `Submodel` object and then pass that object to one of the parser functions.

### AAS Parser

This module provides functions for parsing Asset Administration Shells (AAS) in the AAS standard parser.
For the full list of available methods and signatures, see:
* [AAS Parser Implementation API reference](https://fluid40.github.io/aas-standard-parser/namespaceaas__standard__parser_1_1aas__parser.html)

Example: Use the AAS parser to extract referenced submodel IDs from an Asset Administration Shell.

```python
from aas_standard_parser.aas_parser import get_submodel_ids

submodel_ids = get_submodel_ids(shell)
print(submodel_ids)
```

Typical result:

```python
[
  "https://example.com/submodels/aid",
  "https://example.com/submodels/aimc",
]
```

### Submodel Parser

This module provides functions for parsing and traversing submodels in the AAS standard parser.
For the full list of available methods and signatures, see:
* [Submodel Parser Implementation API reference](https://fluid40.github.io/aas-standard-parser/namespaceaas__standard__parser_1_1submodel__parser.html)

Example: Use the submodel parser to navigate nested elements by `idShort` path.

```python
from aas_standard_parser.submodel_parser import get_submodel_element_by_id_short_path

element = get_submodel_element_by_id_short_path(
  aid_submodel,
  "Interface_MQTT.InteractionMetadata.properties.AxisData.properties.HandlingC",
)

if element is not None:
  print(element.id_short)
```

Indexed access for `SubmodelElementList` values is also supported:

```python
item = get_submodel_element_by_id_short_path(submodel, "SomeList[0].NestedElement")
```

### AID Parser

This module provides functions for parsing AID submodels in the AAS standard parser.
For the full list of available methods and signatures, see:
* [AID Parser Implementation API reference](https://fluid40.github.io/aas-standard-parser/namespaceaas__standard__parser_1_1aid__parser.html)

Example: Use `AIDParser` to extract endpoint metadata, property mappings, and security information from an Asset Interface Description.

```python
from aas_standard_parser.aid_parser import AIDParser
from aas_standard_parser.collection_helpers import find_by_id_short

parser = AIDParser()
aid_interface = find_by_id_short(aid_submodel.submodel_element, "Interface_MQTT")

base_url = parser.parse_base(aid_interface)
print(base_url)

properties = parser.parse_properties(aid_interface)
for path, details in properties.items():
  print(path, details.href, details.keys)

security = parser.parse_security(aid_interface)
print(type(security).__name__)
```

Typical `parse_properties()` output maps each property path to its endpoint path and payload keys:

```python
for path, details in properties.items():
  print(f"{path} -> href={details.href}, keys={details.keys}")
```

### AIMC Parser

This module provides functions for parsing AIMC submodels in the AAS standard parser.
For the full list of available methods and signatures, see:
* [AIMC Parser Implementation API reference](https://fluid40.github.io/aas-standard-parser/namespaceaas__standard__parser_1_1aimc__parser.html)

Example: Use the AIMC parser to read mapping configurations and source-sink relations.

```python
from aas_standard_parser.aimc_parser import (
  get_mapping_configuration_elements,
  get_mapping_configuration_root_element,
  parse_mapping_configurations,
)

root = get_mapping_configuration_root_element(aimc_submodel)
print(root.id_short)

elements = get_mapping_configuration_elements(aimc_submodel)
print(len(elements))

mapping_configurations = parse_mapping_configurations(aimc_submodel)
print(mapping_configurations.aid_submodel_ids)

for configuration in mapping_configurations.configurations:
  print(configuration.aid_submodel_id)
  print(configuration.interface_reference.value.key[0].value)
  for relation in configuration.source_sink_relations:
    print(relation.source_properties.property_name, relation.sink_properties.property_name)
```

### Collection Helpers

This module provides functions for parsing and handling submodel element collections in the AAS standard parser.
For the full list of available methods and signatures, see:
* [Collection Helpers Implementation API reference](https://fluid40.github.io/aas-standard-parser/namespaceaas__standard__parser_1_1collection__helpers.html)

Example: Use the collection helpers to search `SubmodelElementCollection` and `SubmodelElementList` content by semantic ID, supplemental semantic ID, or `idShort` .

```python
from aas_standard_parser.collection_helpers import (
  contains_supplemental_semantic_id,
  find_all_by_in_semantic_id,
  find_all_by_semantic_id,
  find_by_id_short,
  find_by_in_semantic_id,
  find_by_semantic_id,
  find_by_supplemental_semantic_id,
)

interface = find_by_id_short(aid_submodel.submodel_element, "Interface_MQTT")
endpoint_metadata = find_by_semantic_id(
  interface.value,
  "https://admin-shell.io/idta/AssetInterfacesDescription/1/0/EndpointMetadata",
)
interaction_metadata = find_by_in_semantic_id(interface.value, "InteractionMetadata")
properties = find_all_by_semantic_id(
  interaction_metadata.value,
  "https://www.w3.org/2019/wot/td#PropertyAffordance",
)
collections = find_all_by_in_semantic_id(interface.value, "PropertyDefinition")
security_scheme = find_by_supplemental_semantic_id(interface.value, "https://example.com/custom-semantic-id")

if endpoint_metadata is not None:
  print(contains_supplemental_semantic_id(endpoint_metadata, "https://example.com/custom-semantic-id"))
```

### Reference Helpers

This module provides functions for parsing and handling references in the AAS standard parser.
For the full list of available methods and signatures, see:
* [Reference Helpers Implementation API reference](https://fluid40.github.io/aas-standard-parser/namespaceaas__standard__parser_1_1reference__helpers.html)

Example: Use the reference helpers to derive readable paths and inspect key values from AAS references.

```python
from aas_standard_parser.reference_helpers import (
  construct_id_short_path_from_reference,
  get_value_from_key_at_index,
  get_values_from_keys,
)

reference = configuration.interface_reference.value

path = construct_id_short_path_from_reference(reference)
all_values = get_values_from_keys(reference)
first_value = get_value_from_key_at_index(reference, 0)

print(path)
print(all_values)
print(first_value)
```

### Submodel JSON Helper

This module provides functions for parsing and handling submodels as JSON structures in the AAS standard parser.
For the full list of available methods and signatures, see:
* [Submodel JSON Helper Implementation API reference](https://fluid40.github.io/aas-standard-parser/namespaceaas__standard__parser_1_1submodel__json__helper.html)

Example: Use the JSON helper if you need to inspect raw JSON dictionaries before converting them into BaSyx objects.

```python
import json

from aas_standard_parser.submodel_json_helper import get_value_from_semantic_id_by_index

with open("tests/test_data/aid_submodel.json", encoding="utf-8") as file:
  aid_data = json.load(file)

semantic_id = get_value_from_semantic_id_by_index(aid_data)
print(semantic_id)
```

### Descriptor JSON Helper

This module provides functions for parsing and handling descriptors as JSON structures in the AAS standard parser.
For the full list of available methods and signatures, see:
* [Descriptor JSON Helper Implementation API reference](https://fluid40.github.io/aas-standard-parser/namespaceaas__standard__parser_1_1descriptor__json__helper.html)

Example: Use the descriptor helper to inspect descriptor endpoints and parse encoded shell or submodel URLs.

```python
from aas_standard_parser.descriptor_json_helper import (
  get_endpoint_by_index,
  get_endpoint_href_by_index,
  get_endpoint_hrefs,
  get_endpoint_protocol_information_by_index,
  get_endpoints,
  parse_endpoint_href,
)

descriptor = {
  "endpoints": [
    {
      "protocolInformation": {
        "href": "http://aas-server:8075/submodels/RW5lcmd5TW9uaXRvcmluZw"
      }
    }
  ]
}

print(get_endpoints(descriptor))
print(get_endpoint_by_index(descriptor, 0))
print(get_endpoint_protocol_information_by_index(descriptor, 0))
print(get_endpoint_href_by_index(descriptor, 0))
print(get_endpoint_hrefs(descriptor))

href_data = parse_endpoint_href(get_endpoint_href_by_index(descriptor, 0))
print(href_data.base_url)
print(href_data.identifier)
print(href_data.identifier_encoded)
```

### Utilities

This module provides general utility functions for the AAS standard parser.
For the full list of available methods and signatures, see:
* [Utilities Implementation API reference](https://fluid40.github.io/aas-standard-parser/namespaceaas__standard__parser_1_1utils.html)

Example: Decode and encode submodel IDs.

```python
from aas_standard_parser.utils import create_submodel_from_file, decode_base_64, encode_base_64

submodel = create_submodel_from_file("tests/test_data/aimc_submodel.json")

encoded = encode_base_64("EnergyMonitoring")
decoded = decode_base_64(encoded)

print(submodel.id)
print(encoded)
print(decoded)
```

Example: Create a submodel object from a JSON file.

```python
from aas_standard_parser.utils import create_submodel_from_file

aid_submodel = create_submodel_from_file("tests/test_data/aid_submodel.json")
aimc_submodel = create_submodel_from_file("tests/test_data/aimc_submodel.json")
```

If you are working with AAS descriptors, `encode_base_64()` and `decode_base_64()` are useful for converting between readable identifiers and encoded URL fragments.
