# How To: Write Read Attribute Numeric Type Graphml

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test write read attribute numeric type graphml

## Prerequisites

**Required Modules:**
- `io`
- `pytest`
- `networkx`
- `networkx.readwrite.graphml`
- `networkx.utils`
- `xml.etree.ElementTree`
- `xml.etree.ElementTree`
- `xml.etree.ElementTree`
- `xml.etree.ElementTree`
- `json`
- `lxml.etree`


## Step-by-Step Guide

### Step 1: Assign G = value

```python
G = self.attribute_numeric_type_graph
```

**Verification:**
```python
assert nodes_equal(G.nodes(), H.nodes())
```

### Step 2: Assign fh = io.BytesIO(...)

```python
fh = io.BytesIO()
```

**Verification:**
```python
assert edges_equal(G.edges(), H.edges(), directed=True)
```

### Step 3: Call self.writer()

```python
self.writer(G, fh, infer_numeric_types=True)
```

**Verification:**
```python
assert edges_equal(G.edges(data=True), H.edges(data=True), directed=True)
```

### Step 4: Call fh.seek()

```python
fh.seek(0)
```

**Verification:**
```python
assert len(children) == 3
```

### Step 5: Assign H = nx.read_graphml(...)

```python
H = nx.read_graphml(fh)
```

**Verification:**
```python
assert len(keys) == 2
```

### Step 6: Call fh.seek()

```python
fh.seek(0)
```

**Verification:**
```python
assert ('attr.type', 'double') in keys[0]
```

### Step 7: Call self.attribute_numeric_type_fh.seek()

```python
self.attribute_numeric_type_fh.seek(0)
```

**Verification:**
```python
assert ('attr.type', 'double') in keys[1]
```

### Step 8: Assign xml = parse(...)

```python
xml = parse(fh)
```

### Step 9: Assign children = list(...)

```python
children = list(xml.getroot())
```

**Verification:**
```python
assert len(children) == 3
```

### Step 10: Assign keys = value

```python
keys = [child.items() for child in children[:2]]
```

**Verification:**
```python
assert len(keys) == 2
```


## Complete Example

```python
# Workflow
from xml.etree.ElementTree import parse
G = self.attribute_numeric_type_graph
fh = io.BytesIO()
self.writer(G, fh, infer_numeric_types=True)
fh.seek(0)
H = nx.read_graphml(fh)
fh.seek(0)
assert nodes_equal(G.nodes(), H.nodes())
assert edges_equal(G.edges(), H.edges(), directed=True)
assert edges_equal(G.edges(data=True), H.edges(data=True), directed=True)
self.attribute_numeric_type_fh.seek(0)
xml = parse(fh)
children = list(xml.getroot())
assert len(children) == 3
keys = [child.items() for child in children[:2]]
assert len(keys) == 2
assert ('attr.type', 'double') in keys[0]
assert ('attr.type', 'double') in keys[1]
```

## Next Steps


---

*Source: test_graphml.py:1185 | Complexity: Advanced | Last updated: 2026-06-02*