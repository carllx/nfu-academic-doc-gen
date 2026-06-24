# How To: Long Attribute Type

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test long attribute type

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

### Step 1: Assign s = '<?xml version=\'1.0\' encoding=\'utf-8\'?>\n<graphml xmlns="http://graphml.graphdrawing.org/xmlns"\n         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n         xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns\n         http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">\n  <key attr.name="cudfversion" attr.type="long" for="node" id="d6" />\n  <graph edgedefault="directed">\n    <node id="n1">\n      <data key="d6">4284</data>\n    </node>\n  </graph>\n</graphml>'

```python
s = '<?xml version=\'1.0\' encoding=\'utf-8\'?>\n<graphml xmlns="http://graphml.graphdrawing.org/xmlns"\n         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n         xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns\n         http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">\n  <key attr.name="cudfversion" attr.type="long" for="node" id="d6" />\n  <graph edgedefault="directed">\n    <node id="n1">\n      <data key="d6">4284</data>\n    </node>\n  </graph>\n</graphml>'
```

**Verification:**
```python
assert sorted(G.nodes(data=True)) == expected
```

### Step 2: Assign fh = io.BytesIO(...)

```python
fh = io.BytesIO(s.encode('UTF-8'))
```

**Verification:**
```python
assert sorted(H.nodes(data=True)) == expected
```

### Step 3: Assign G = nx.read_graphml(...)

```python
G = nx.read_graphml(fh)
```

### Step 4: Assign expected = value

```python
expected = [('n1', {'cudfversion': 4284})]
```

**Verification:**
```python
assert sorted(G.nodes(data=True)) == expected
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
assert sorted(H.nodes(data=True)) == expected
```


## Complete Example

```python
# Workflow
s = '<?xml version=\'1.0\' encoding=\'utf-8\'?>\n<graphml xmlns="http://graphml.graphdrawing.org/xmlns"\n         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n         xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns\n         http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">\n  <key attr.name="cudfversion" attr.type="long" for="node" id="d6" />\n  <graph edgedefault="directed">\n    <node id="n1">\n      <data key="d6">4284</data>\n    </node>\n  </graph>\n</graphml>'
fh = io.BytesIO(s.encode('UTF-8'))
G = nx.read_graphml(fh)
expected = [('n1', {'cudfversion': 4284})]
assert sorted(G.nodes(data=True)) == expected
fh.seek(0)
H = nx.parse_graphml(s)
assert sorted(H.nodes(data=True)) == expected
```

## Next Steps


---

*Source: test_graphml.py:1069 | Complexity: Intermediate | Last updated: 2026-06-02*