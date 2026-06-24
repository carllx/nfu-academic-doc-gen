# How To: Read Edgelist 3

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read edgelist 3

## Prerequisites

**Required Modules:**
- `io`
- `pytest`
- `networkx`
- `networkx.algorithms`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign s = b"# comment line\n1 2 {'weight':2.0}\n# comment line\n2 3 {'weight':3.0}\n"

```python
s = b"# comment line\n1 2 {'weight':2.0}\n# comment line\n2 3 {'weight':3.0}\n"
```

**Verification:**
```python
assert edges_equal(G.edges(), [(1, 2), (2, 3)])
```

### Step 2: Assign bytesIO = io.BytesIO(...)

```python
bytesIO = io.BytesIO(s)
```

**Verification:**
```python
assert edges_equal(G.edges(data=True), [(1, 2, {'weight': 2.0}), (2, 3, {'weight': 3.0})])
```

### Step 3: Assign G = bipartite.read_edgelist(...)

```python
G = bipartite.read_edgelist(bytesIO, nodetype=int, data=False)
```

**Verification:**
```python
assert edges_equal(G.edges(), [(1, 2), (2, 3)])
```

### Step 4: Assign bytesIO = io.BytesIO(...)

```python
bytesIO = io.BytesIO(s)
```

### Step 5: Assign G = bipartite.read_edgelist(...)

```python
G = bipartite.read_edgelist(bytesIO, nodetype=int, data=True)
```

**Verification:**
```python
assert edges_equal(G.edges(data=True), [(1, 2, {'weight': 2.0}), (2, 3, {'weight': 3.0})])
```


## Complete Example

```python
# Workflow
s = b"# comment line\n1 2 {'weight':2.0}\n# comment line\n2 3 {'weight':3.0}\n"
bytesIO = io.BytesIO(s)
G = bipartite.read_edgelist(bytesIO, nodetype=int, data=False)
assert edges_equal(G.edges(), [(1, 2), (2, 3)])
bytesIO = io.BytesIO(s)
G = bipartite.read_edgelist(bytesIO, nodetype=int, data=True)
assert edges_equal(G.edges(data=True), [(1, 2, {'weight': 2.0}), (2, 3, {'weight': 3.0})])
```

## Next Steps


---

*Source: test_edgelist.py:40 | Complexity: Intermediate | Last updated: 2026-06-02*