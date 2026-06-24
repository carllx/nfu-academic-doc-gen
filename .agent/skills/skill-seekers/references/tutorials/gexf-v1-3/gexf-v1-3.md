# How To: Gexf V1 3

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: 'Basic graph' example from https://gexf.net/schema.html

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `io`
- `time`
- `pytest`
- `networkx`
- `math`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: "'Basic graph' example from https://gexf.net/schema.html"

```python
"'Basic graph' example from https://gexf.net/schema.html"
```

**Verification:**
```python
assert nx.utils.graphs_equal(G, expected)
```

### Step 2: Assign data = '<?xml version="1.0" encoding="UTF-8"?>\n<gexf xmlns="http://gexf.net/1.3" version="1.3">\n    <graph mode="static" defaultedgetype="directed">\n        <nodes>\n            <node id="0" label="Hello" />\n            <node id="1" label="Word" />\n        </nodes>\n        <edges>\n            <edge source="0" target="1" />\n        </edges>\n    </graph>\n</gexf>\n'

```python
data = '<?xml version="1.0" encoding="UTF-8"?>\n<gexf xmlns="http://gexf.net/1.3" version="1.3">\n    <graph mode="static" defaultedgetype="directed">\n        <nodes>\n            <node id="0" label="Hello" />\n            <node id="1" label="Word" />\n        </nodes>\n        <edges>\n            <edge source="0" target="1" />\n        </edges>\n    </graph>\n</gexf>\n'
```

**Verification:**
```python
assert nx.utils.graphs_equal(G, expected)
```

### Step 3: Assign expected = nx.DiGraph(...)

```python
expected = nx.DiGraph([('0', '1')])
```

### Step 4: Call nx.set_node_attributes()

```python
nx.set_node_attributes(expected, {'0': 'Hello', '1': 'Word'}, name='label')
```

### Step 5: Assign expected.graph = value

```python
expected.graph = {'mode': 'static', 'edge_default': {}}
```

### Step 6: Assign G = nx.read_gexf(...)

```python
G = nx.read_gexf(fname, version='1.3')
```

**Verification:**
```python
assert nx.utils.graphs_equal(G, expected)
```

### Step 7: Assign G = nx.read_gexf(...)

```python
G = nx.read_gexf(fname)
```

**Verification:**
```python
assert nx.utils.graphs_equal(G, expected)
```

### Step 8: Call fh.write()

```python
fh.write(data)
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
"'Basic graph' example from https://gexf.net/schema.html"
data = '<?xml version="1.0" encoding="UTF-8"?>\n<gexf xmlns="http://gexf.net/1.3" version="1.3">\n    <graph mode="static" defaultedgetype="directed">\n        <nodes>\n            <node id="0" label="Hello" />\n            <node id="1" label="Word" />\n        </nodes>\n        <edges>\n            <edge source="0" target="1" />\n        </edges>\n    </graph>\n</gexf>\n'
with open((fname := (tmp_path / 'basic.gexf')), 'w') as fh:
    fh.write(data)
expected = nx.DiGraph([('0', '1')])
nx.set_node_attributes(expected, {'0': 'Hello', '1': 'Word'}, name='label')
expected.graph = {'mode': 'static', 'edge_default': {}}
G = nx.read_gexf(fname, version='1.3')
assert nx.utils.graphs_equal(G, expected)
G = nx.read_gexf(fname)
assert nx.utils.graphs_equal(G, expected)
```

## Next Steps


---

*Source: test_gexf.py:9 | Complexity: Advanced | Last updated: 2026-06-02*