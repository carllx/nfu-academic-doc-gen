# How To: Read Multiline Adjlist 1

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read multiline adjlist 1

## Prerequisites

**Required Modules:**
- `io`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign s = b'# comment line\n1 2\n# comment line\n2\n3\n'

```python
s = b'# comment line\n1 2\n# comment line\n2\n3\n'
```

**Verification:**
```python
assert graphs_equal(G, nx.Graph(adj))
```

### Step 2: Assign bytesIO = io.BytesIO(...)

```python
bytesIO = io.BytesIO(s)
```

### Step 3: Assign G = nx.read_multiline_adjlist(...)

```python
G = nx.read_multiline_adjlist(bytesIO)
```

### Step 4: Assign adj = value

```python
adj = {'1': {'3': {}, '2': {}}, '3': {'1': {}}, '2': {'1': {}}}
```

**Verification:**
```python
assert graphs_equal(G, nx.Graph(adj))
```


## Complete Example

```python
# Workflow
s = b'# comment line\n1 2\n# comment line\n2\n3\n'
bytesIO = io.BytesIO(s)
G = nx.read_multiline_adjlist(bytesIO)
adj = {'1': {'3': {}, '2': {}}, '3': {'1': {}}, '2': {'1': {}}}
assert graphs_equal(G, nx.Graph(adj))
```

## Next Steps


---

*Source: test_adjlist.py:117 | Complexity: Intermediate | Last updated: 2026-06-02*