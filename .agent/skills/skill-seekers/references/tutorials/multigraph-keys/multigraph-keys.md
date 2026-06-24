# How To: Multigraph Keys

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multigraph keys

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

### Step 1: Assign s = '<?xml version="1.0" encoding="UTF-8"?>\n<graphml xmlns="http://graphml.graphdrawing.org/xmlns"\n         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n         xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns\n         http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">\n  <graph id="G" edgedefault="directed">\n    <node id="n0"/>\n    <node id="n1"/>\n    <edge id="e0" source="n0" target="n1"/>\n    <edge id="e1" source="n0" target="n1"/>\n  </graph>\n</graphml>\n'

```python
s = '<?xml version="1.0" encoding="UTF-8"?>\n<graphml xmlns="http://graphml.graphdrawing.org/xmlns"\n         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n         xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns\n         http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">\n  <graph id="G" edgedefault="directed">\n    <node id="n0"/>\n    <node id="n1"/>\n    <edge id="e0" source="n0" target="n1"/>\n    <edge id="e1" source="n0" target="n1"/>\n  </graph>\n</graphml>\n'
```

**Verification:**
```python
assert sorted(G.edges(keys=True)) == expected
```

### Step 2: Assign fh = io.BytesIO(...)

```python
fh = io.BytesIO(s.encode('UTF-8'))
```

**Verification:**
```python
assert sorted(H.edges(keys=True)) == expected
```

### Step 3: Assign G = nx.read_graphml(...)

```python
G = nx.read_graphml(fh)
```

### Step 4: Assign expected = value

```python
expected = [('n0', 'n1', 'e0'), ('n0', 'n1', 'e1')]
```

**Verification:**
```python
assert sorted(G.edges(keys=True)) == expected
```

### Step 5: Call fh.seek()

```python
fh.seek(0)
```

### Step 6: Assign H = nx.parse_graphml(...)

```python
H = nx.parse_graphml(s)
```

**Verification:**
```python
assert sorted(H.edges(keys=True)) == expected
```


## Complete Example

```python
# Workflow
s = '<?xml version="1.0" encoding="UTF-8"?>\n<graphml xmlns="http://graphml.graphdrawing.org/xmlns"\n         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n         xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns\n         http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">\n  <graph id="G" edgedefault="directed">\n    <node id="n0"/>\n    <node id="n1"/>\n    <edge id="e0" source="n0" target="n1"/>\n    <edge id="e1" source="n0" target="n1"/>\n  </graph>\n</graphml>\n'
fh = io.BytesIO(s.encode('UTF-8'))
G = nx.read_graphml(fh)
expected = [('n0', 'n1', 'e0'), ('n0', 'n1', 'e1')]
assert sorted(G.edges(keys=True)) == expected
fh.seek(0)
H = nx.parse_graphml(s)
assert sorted(H.edges(keys=True)) == expected
```

## Next Steps


---

*Source: test_graphml.py:487 | Complexity: Intermediate | Last updated: 2026-06-02*