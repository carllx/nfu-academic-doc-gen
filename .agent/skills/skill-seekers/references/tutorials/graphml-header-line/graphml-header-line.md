# How To: Graphml Header Line

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test graphml header line

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

### Step 1: Assign good = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n<graphml xmlns="http://graphml.graphdrawing.org/xmlns"\n         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n         xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns\n         http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">\n  <key id="d0" for="node" attr.name="test" attr.type="boolean">\n    <default>false</default>\n  </key>\n  <graph id="G">\n    <node id="n0">\n      <data key="d0">true</data>\n    </node>\n  </graph>\n</graphml>\n'

```python
good = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n<graphml xmlns="http://graphml.graphdrawing.org/xmlns"\n         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n         xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns\n         http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">\n  <key id="d0" for="node" attr.name="test" attr.type="boolean">\n    <default>false</default>\n  </key>\n  <graph id="G">\n    <node id="n0">\n      <data key="d0">true</data>\n    </node>\n  </graph>\n</graphml>\n'
```

**Verification:**
```python
assert graph.nodes['n0']['test']
```

### Step 2: Assign bad = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n<graphml>\n  <key id="d0" for="node" attr.name="test" attr.type="boolean">\n    <default>false</default>\n  </key>\n  <graph id="G">\n    <node id="n0">\n      <data key="d0">true</data>\n    </node>\n  </graph>\n</graphml>\n'

```python
bad = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n<graphml>\n  <key id="d0" for="node" attr.name="test" attr.type="boolean">\n    <default>false</default>\n  </key>\n  <graph id="G">\n    <node id="n0">\n      <data key="d0">true</data>\n    </node>\n  </graph>\n</graphml>\n'
```

### Step 3: Assign ugly = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n<graphml xmlns="https://ghghgh">\n  <key id="d0" for="node" attr.name="test" attr.type="boolean">\n    <default>false</default>\n  </key>\n  <graph id="G">\n    <node id="n0">\n      <data key="d0">true</data>\n    </node>\n  </graph>\n</graphml>\n'

```python
ugly = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n<graphml xmlns="https://ghghgh">\n  <key id="d0" for="node" attr.name="test" attr.type="boolean">\n    <default>false</default>\n  </key>\n  <graph id="G">\n    <node id="n0">\n      <data key="d0">true</data>\n    </node>\n  </graph>\n</graphml>\n'
```

### Step 4: Assign fh = io.BytesIO(...)

```python
fh = io.BytesIO(ugly.encode('UTF-8'))
```

### Step 5: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, nx.read_graphml, fh)
```

### Step 6: Call pytest.raises()

```python
pytest.raises(nx.NetworkXError, nx.parse_graphml, ugly)
```

### Step 7: Assign fh = io.BytesIO(...)

```python
fh = io.BytesIO(s.encode('UTF-8'))
```

### Step 8: Assign G = nx.read_graphml(...)

```python
G = nx.read_graphml(fh)
```

### Step 9: Assign H = nx.parse_graphml(...)

```python
H = nx.parse_graphml(s)
```

**Verification:**
```python
assert graph.nodes['n0']['test']
```


## Complete Example

```python
# Workflow
good = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n<graphml xmlns="http://graphml.graphdrawing.org/xmlns"\n         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n         xsi:schemaLocation="http://graphml.graphdrawing.org/xmlns\n         http://graphml.graphdrawing.org/xmlns/1.0/graphml.xsd">\n  <key id="d0" for="node" attr.name="test" attr.type="boolean">\n    <default>false</default>\n  </key>\n  <graph id="G">\n    <node id="n0">\n      <data key="d0">true</data>\n    </node>\n  </graph>\n</graphml>\n'
bad = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n<graphml>\n  <key id="d0" for="node" attr.name="test" attr.type="boolean">\n    <default>false</default>\n  </key>\n  <graph id="G">\n    <node id="n0">\n      <data key="d0">true</data>\n    </node>\n  </graph>\n</graphml>\n'
ugly = '<?xml version="1.0" encoding="UTF-8" standalone="no"?>\n<graphml xmlns="https://ghghgh">\n  <key id="d0" for="node" attr.name="test" attr.type="boolean">\n    <default>false</default>\n  </key>\n  <graph id="G">\n    <node id="n0">\n      <data key="d0">true</data>\n    </node>\n  </graph>\n</graphml>\n'
for s in (good, bad):
    fh = io.BytesIO(s.encode('UTF-8'))
    G = nx.read_graphml(fh)
    H = nx.parse_graphml(s)
    for graph in [G, H]:
        assert graph.nodes['n0']['test']
fh = io.BytesIO(ugly.encode('UTF-8'))
pytest.raises(nx.NetworkXError, nx.read_graphml, fh)
pytest.raises(nx.NetworkXError, nx.parse_graphml, ugly)
```

## Next Steps


---

*Source: test_graphml.py:726 | Complexity: Advanced | Last updated: 2026-06-02*