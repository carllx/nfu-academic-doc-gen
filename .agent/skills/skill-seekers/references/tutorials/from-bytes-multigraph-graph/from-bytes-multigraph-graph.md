# How To: From Bytes Multigraph Graph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test from bytes multigraph graph

## Prerequisites

**Required Modules:**
- `io`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign graph_data = b':An'

```python
graph_data = b':An'
```

**Verification:**
```python
assert isinstance(G, nx.Graph)
```

### Step 2: Assign G = nx.from_sparse6_bytes(...)

```python
G = nx.from_sparse6_bytes(graph_data)
```

**Verification:**
```python
assert isinstance(M, nx.MultiGraph)
```

### Step 3: Assign multigraph_data = b':Ab'

```python
multigraph_data = b':Ab'
```

### Step 4: Assign M = nx.from_sparse6_bytes(...)

```python
M = nx.from_sparse6_bytes(multigraph_data)
```

**Verification:**
```python
assert isinstance(M, nx.MultiGraph)
```


## Complete Example

```python
# Workflow
graph_data = b':An'
G = nx.from_sparse6_bytes(graph_data)
assert isinstance(G, nx.Graph)
multigraph_data = b':Ab'
M = nx.from_sparse6_bytes(multigraph_data)
assert isinstance(M, nx.MultiGraph)
```

## Next Steps


---

*Source: test_sparse6.py:50 | Complexity: Intermediate | Last updated: 2026-06-02*