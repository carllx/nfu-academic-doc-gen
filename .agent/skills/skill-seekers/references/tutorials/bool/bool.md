# How To: Bool

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test bool

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

### Step 1: Assign s = '<?xml version="1.0" encoding="UTF-8"?>\n<graphml xmlns="http://graphml.graphdrawing.org/xmlns"\n         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n         xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns\n         http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">\n  <key id="d0" for="node" attr.name="test" attr.type="boolean">\n    <default>false</default>\n  </key>\n  <graph id="G" edgedefault="directed">\n    <node id="n0">\n      <data key="d0">true</data>\n    </node>\n    <node id="n1"/>\n    <node id="n2">\n      <data key="d0">false</data>\n    </node>\n    <node id="n3">\n      <data key="d0">FaLsE</data>\n    </node>\n    <node id="n4">\n      <data key="d0">True</data>\n    </node>\n    <node id="n5">\n      <data key="d0">0</data>\n    </node>\n    <node id="n6">\n      <data key="d0">1</data>\n    </node>\n  </graph>\n</graphml>\n'

```python
s = '<?xml version="1.0" encoding="UTF-8"?>\n<graphml xmlns="http://graphml.graphdrawing.org/xmlns"\n         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n         xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns\n         http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">\n  <key id="d0" for="node" attr.name="test" attr.type="boolean">\n    <default>false</default>\n  </key>\n  <graph id="G" edgedefault="directed">\n    <node id="n0">\n      <data key="d0">true</data>\n    </node>\n    <node id="n1"/>\n    <node id="n2">\n      <data key="d0">false</data>\n    </node>\n    <node id="n3">\n      <data key="d0">FaLsE</data>\n    </node>\n    <node id="n4">\n      <data key="d0">True</data>\n    </node>\n    <node id="n5">\n      <data key="d0">0</data>\n    </node>\n    <node id="n6">\n      <data key="d0">1</data>\n    </node>\n  </graph>\n</graphml>\n'
```

**Verification:**
```python
assert graph.nodes['n0']['test']
```

### Step 2: Assign fh = io.BytesIO(...)

```python
fh = io.BytesIO(s.encode('UTF-8'))
```

**Verification:**
```python
assert not graph.nodes['n2']['test']
```

### Step 3: Assign G = nx.read_graphml(...)

```python
G = nx.read_graphml(fh)
```

**Verification:**
```python
assert not graph.nodes['n3']['test']
```

### Step 4: Assign H = nx.parse_graphml(...)

```python
H = nx.parse_graphml(s)
```

**Verification:**
```python
assert graph.nodes['n4']['test']
```


## Complete Example

```python
# Workflow
s = '<?xml version="1.0" encoding="UTF-8"?>\n<graphml xmlns="http://graphml.graphdrawing.org/xmlns"\n         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n         xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns\n         http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">\n  <key id="d0" for="node" attr.name="test" attr.type="boolean">\n    <default>false</default>\n  </key>\n  <graph id="G" edgedefault="directed">\n    <node id="n0">\n      <data key="d0">true</data>\n    </node>\n    <node id="n1"/>\n    <node id="n2">\n      <data key="d0">false</data>\n    </node>\n    <node id="n3">\n      <data key="d0">FaLsE</data>\n    </node>\n    <node id="n4">\n      <data key="d0">True</data>\n    </node>\n    <node id="n5">\n      <data key="d0">0</data>\n    </node>\n    <node id="n6">\n      <data key="d0">1</data>\n    </node>\n  </graph>\n</graphml>\n'
fh = io.BytesIO(s.encode('UTF-8'))
G = nx.read_graphml(fh)
H = nx.parse_graphml(s)
for graph in [G, H]:
    assert graph.nodes['n0']['test']
    assert not graph.nodes['n2']['test']
    assert not graph.nodes['n3']['test']
    assert graph.nodes['n4']['test']
    assert not graph.nodes['n5']['test']
    assert graph.nodes['n6']['test']
```

## Next Steps


---

*Source: test_graphml.py:683 | Complexity: Intermediate | Last updated: 2026-06-02*