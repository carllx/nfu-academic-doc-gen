# How To: Noncomparable Nodes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test noncomparable nodes

## Prerequisites

**Required Modules:**
- `importlib.resources`
- `random`
- `struct`
- `pytest`
- `networkx`
- `networkx.algorithms`
- `networkx.generators`


## Step-by-Step Guide

### Step 1: Assign node1 = object(...)

```python
node1 = object()
```

**Verification:**
```python
assert gm.is_isomorphic()
```

### Step 2: Assign node2 = object(...)

```python
node2 = object()
```

**Verification:**
```python
assert gm.subgraph_is_monomorphic()
```

### Step 3: Assign node3 = object(...)

```python
node3 = object()
```

**Verification:**
```python
assert dgm.is_isomorphic()
```

### Step 4: Assign G = nx.path_graph(...)

```python
G = nx.path_graph([node1, node2, node3])
```

**Verification:**
```python
assert dgm.subgraph_is_monomorphic()
```

### Step 5: Assign gm = iso.GraphMatcher(...)

```python
gm = iso.GraphMatcher(G, G)
```

**Verification:**
```python
assert gm.is_isomorphic()
```

### Step 6: Assign G = nx.path_graph(...)

```python
G = nx.path_graph([node1, node2, node3], create_using=nx.DiGraph)
```

### Step 7: Assign H = nx.path_graph(...)

```python
H = nx.path_graph([node3, node2, node1], create_using=nx.DiGraph)
```

### Step 8: Assign dgm = iso.DiGraphMatcher(...)

```python
dgm = iso.DiGraphMatcher(G, H)
```

**Verification:**
```python
assert dgm.is_isomorphic()
```


## Complete Example

```python
# Workflow
node1 = object()
node2 = object()
node3 = object()
G = nx.path_graph([node1, node2, node3])
gm = iso.GraphMatcher(G, G)
assert gm.is_isomorphic()
assert gm.subgraph_is_monomorphic()
G = nx.path_graph([node1, node2, node3], create_using=nx.DiGraph)
H = nx.path_graph([node3, node2, node1], create_using=nx.DiGraph)
dgm = iso.DiGraphMatcher(G, H)
assert dgm.is_isomorphic()
assert dgm.subgraph_is_monomorphic()
```

## Next Steps


---

*Source: test_isomorphvf2.py:415 | Complexity: Advanced | Last updated: 2026-06-02*