# How To: Cycle Graph

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cycle graph

## Prerequisites

**Required Modules:**
- `itertools`
- `typing`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.cycle_graph(...)

```python
G = nx.cycle_graph(4)
```

**Verification:**
```python
assert edges_equal(G.edges(), [(0, 1), (0, 3), (1, 2), (2, 3)])
```

### Step 2: Assign mG = nx.cycle_graph(...)

```python
mG = nx.cycle_graph(4, create_using=nx.MultiGraph)
```

**Verification:**
```python
assert edges_equal(mG.edges(), [(0, 1), (0, 3), (1, 2), (2, 3)])
```

### Step 3: Assign G = nx.cycle_graph(...)

```python
G = nx.cycle_graph(4, create_using=nx.DiGraph)
```

**Verification:**
```python
assert not G.has_edge(2, 1)
```

### Step 4: Assign G = nx.cycle_graph(...)

```python
G = nx.cycle_graph('abc')
```

**Verification:**
```python
assert G.has_edge(1, 2)
```

### Step 5: Assign G = nx.cycle_graph(...)

```python
G = nx.cycle_graph('abcb')
```

**Verification:**
```python
assert G.is_directed()
```

### Step 6: Assign g = nx.cycle_graph(...)

```python
g = nx.cycle_graph('abc', nx.DiGraph)
```

**Verification:**
```python
assert len(G) == 3
```

### Step 7: Assign g = nx.cycle_graph(...)

```python
g = nx.cycle_graph('abcb', nx.DiGraph)
```

**Verification:**
```python
assert G.size() == 3
```


## Complete Example

```python
# Workflow
G = nx.cycle_graph(4)
assert edges_equal(G.edges(), [(0, 1), (0, 3), (1, 2), (2, 3)])
mG = nx.cycle_graph(4, create_using=nx.MultiGraph)
assert edges_equal(mG.edges(), [(0, 1), (0, 3), (1, 2), (2, 3)])
G = nx.cycle_graph(4, create_using=nx.DiGraph)
assert not G.has_edge(2, 1)
assert G.has_edge(1, 2)
assert G.is_directed()
G = nx.cycle_graph('abc')
assert len(G) == 3
assert G.size() == 3
G = nx.cycle_graph('abcb')
assert len(G) == 3
assert G.size() == 2
g = nx.cycle_graph('abc', nx.DiGraph)
assert len(g) == 3
assert g.size() == 3
assert g.is_directed()
g = nx.cycle_graph('abcb', nx.DiGraph)
assert len(g) == 3
assert g.size() == 4
```

## Next Steps


---

*Source: test_classic.py:208 | Complexity: Intermediate | Last updated: 2026-06-02*