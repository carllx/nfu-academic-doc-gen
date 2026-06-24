# How To: Cache Reset

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cache reset

## Prerequisites

**Required Modules:**
- `gc`
- `pickle`
- `platform`
- `weakref`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = self.K3.copy(...)

```python
G = self.K3.copy()
```

**Verification:**
```python
assert id(G.adj) == id(old_adj)
```

### Step 2: Assign old_adj = value

```python
old_adj = G.adj
```

**Verification:**
```python
assert id(G.adj) != id(old_adj)
```

### Step 3: Assign G._adj = value

```python
G._adj = {}
```

**Verification:**
```python
assert id(G.nodes) == id(old_nodes)
```

### Step 4: Assign old_nodes = value

```python
old_nodes = G.nodes
```

**Verification:**
```python
assert id(G.nodes) != id(old_nodes)
```

### Step 5: Assign G._node = value

```python
G._node = {}
```

**Verification:**
```python
assert id(G.nodes) != id(old_nodes)
```


## Complete Example

```python
# Workflow
G = self.K3.copy()
old_adj = G.adj
assert id(G.adj) == id(old_adj)
G._adj = {}
assert id(G.adj) != id(old_adj)
old_nodes = G.nodes
assert id(G.nodes) == id(old_nodes)
G._node = {}
assert id(G.nodes) != id(old_nodes)
```

## Next Steps


---

*Source: test_graph.py:194 | Complexity: Intermediate | Last updated: 2026-06-02*