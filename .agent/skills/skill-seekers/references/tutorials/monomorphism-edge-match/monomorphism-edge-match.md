# How To: Monomorphism Edge Match

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test monomorphism edge match

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

### Step 1: Assign G = nx.DiGraph(...)

```python
G = nx.DiGraph()
```

**Verification:**
```python
assert gm.subgraph_is_monomorphic()
```

### Step 2: Call G.add_node()

```python
G.add_node(1)
```

**Verification:**
```python
assert not gm.subgraph_is_monomorphic()
```

### Step 3: Call G.add_node()

```python
G.add_node(2)
```

### Step 4: Call G.add_edge()

```python
G.add_edge(1, 2, label='A')
```

### Step 5: Call G.add_edge()

```python
G.add_edge(2, 1, label='B')
```

### Step 6: Call G.add_edge()

```python
G.add_edge(2, 2, label='C')
```

### Step 7: Assign SG = nx.DiGraph(...)

```python
SG = nx.DiGraph()
```

### Step 8: Call SG.add_node()

```python
SG.add_node(5)
```

### Step 9: Call SG.add_node()

```python
SG.add_node(6)
```

### Step 10: Call SG.add_edge()

```python
SG.add_edge(5, 6, label='A')
```

### Step 11: Assign gm = iso.DiGraphMatcher(...)

```python
gm = iso.DiGraphMatcher(G, SG, edge_match=iso.categorical_edge_match('label', None))
```

**Verification:**
```python
assert gm.subgraph_is_monomorphic()
```

### Step 12: Assign unknown = None

```python
G.edges[1, 2]['label'] = None
```

**Verification:**
```python
assert not gm.subgraph_is_monomorphic()
```


## Complete Example

```python
# Workflow
G = nx.DiGraph()
G.add_node(1)
G.add_node(2)
G.add_edge(1, 2, label='A')
G.add_edge(2, 1, label='B')
G.add_edge(2, 2, label='C')
SG = nx.DiGraph()
SG.add_node(5)
SG.add_node(6)
SG.add_edge(5, 6, label='A')
gm = iso.DiGraphMatcher(G, SG, edge_match=iso.categorical_edge_match('label', None))
assert gm.subgraph_is_monomorphic()
G.edges[1, 2]['label'] = None
assert not gm.subgraph_is_monomorphic()
```

## Next Steps


---

*Source: test_isomorphvf2.py:434 | Complexity: Advanced | Last updated: 2026-06-02*