# How To: Unicode Node

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unicode node

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `codecs`
- `io`
- `math`
- `ast`
- `contextlib`
- `textwrap`
- `pytest`
- `networkx`
- `networkx.readwrite.gml`
- `numpy`

**Setup Required:**
```python
# Fixtures: tmp_path
```

## Step-by-Step Guide

### Step 1: Assign node = value

```python
node = 'node' + chr(169)
```

**Verification:**
```python
assert data == answer
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 3: Call G.add_node()

```python
G.add_node(node)
```

### Step 4: Assign answer = 'graph [\n  node [\n    id 0\n    label "node&#169;"\n  ]\n]'

```python
answer = 'graph [\n  node [\n    id 0\n    label "node&#169;"\n  ]\n]'
```

**Verification:**
```python
assert data == answer
```

### Step 5: Call nx.write_gml()

```python
nx.write_gml(G, fobj)
```

### Step 6: Call fobj.seek()

```python
fobj.seek(0)
```

### Step 7: Assign data = fobj.read.strip.decode(...)

```python
data = fobj.read().strip().decode('ascii')
```


## Complete Example

```python
# Setup
# Fixtures: tmp_path

# Workflow
node = 'node' + chr(169)
G = nx.Graph()
G.add_node(node)
with open(tmp_path / 'test.gml', 'w+b') as fobj:
    nx.write_gml(G, fobj)
    fobj.seek(0)
    data = fobj.read().strip().decode('ascii')
answer = 'graph [\n  node [\n    id 0\n    label "node&#169;"\n  ]\n]'
assert data == answer
```

## Next Steps


---

*Source: test_gml.py:255 | Complexity: Intermediate | Last updated: 2026-06-02*