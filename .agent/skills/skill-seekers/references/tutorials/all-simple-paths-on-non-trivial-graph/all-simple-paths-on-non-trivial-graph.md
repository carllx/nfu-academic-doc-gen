# How To: All Simple Paths On Non Trivial Graph

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: you may need to draw this graph to make sure it is reasonable

## Prerequisites

**Required Modules:**
- `random`
- `pytest`
- `networkx`
- `networkx`
- `networkx.algorithms.simple_paths`
- `networkx.utils`
- `itertools`
- `itertools`


## Step-by-Step Guide

### Step 1: 'you may need to draw this graph to make sure it is reasonable'

```python
'you may need to draw this graph to make sure it is reasonable'
```

**Verification:**
```python
assert {tuple(p) for p in paths} == {(1, 2), (1, 3, 4, 2), (1, 5, 4, 2), (1, 3), (1, 2, 3), (1, 5, 4, 3), (1, 5, 4, 2, 3)}
```

### Step 2: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(5, create_using=nx.DiGraph())
```

**Verification:**
```python
assert {tuple(p) for p in paths} == {(1, 2), (1, 3, 4, 2), (1, 5, 4, 2), (1, 3), (1, 2, 3), (1, 5, 4, 3)}
```

### Step 3: Call G.add_edges_from()

```python
G.add_edges_from([(0, 5), (1, 5), (1, 3), (5, 4), (4, 2), (4, 3)])
```

**Verification:**
```python
assert {tuple(p) for p in paths} == {(1, 2), (1, 3), (1, 2, 3)}
```

### Step 4: Assign paths = nx.all_simple_paths(...)

```python
paths = nx.all_simple_paths(G, 1, [2, 3])
```

**Verification:**
```python
assert {tuple(p) for p in paths} == {(1, 2), (1, 3, 4, 2), (1, 5, 4, 2), (1, 3), (1, 2, 3), (1, 5, 4, 3), (1, 5, 4, 2, 3)}
```

### Step 5: Assign paths = nx.all_simple_paths(...)

```python
paths = nx.all_simple_paths(G, 1, [2, 3], cutoff=3)
```

**Verification:**
```python
assert {tuple(p) for p in paths} == {(1, 2), (1, 3, 4, 2), (1, 5, 4, 2), (1, 3), (1, 2, 3), (1, 5, 4, 3)}
```

### Step 6: Assign paths = nx.all_simple_paths(...)

```python
paths = nx.all_simple_paths(G, 1, [2, 3], cutoff=2)
```

**Verification:**
```python
assert {tuple(p) for p in paths} == {(1, 2), (1, 3), (1, 2, 3)}
```


## Complete Example

```python
# Workflow
'you may need to draw this graph to make sure it is reasonable'
G = nx.path_graph(5, create_using=nx.DiGraph())
G.add_edges_from([(0, 5), (1, 5), (1, 3), (5, 4), (4, 2), (4, 3)])
paths = nx.all_simple_paths(G, 1, [2, 3])
assert {tuple(p) for p in paths} == {(1, 2), (1, 3, 4, 2), (1, 5, 4, 2), (1, 3), (1, 2, 3), (1, 5, 4, 3), (1, 5, 4, 2, 3)}
paths = nx.all_simple_paths(G, 1, [2, 3], cutoff=3)
assert {tuple(p) for p in paths} == {(1, 2), (1, 3, 4, 2), (1, 5, 4, 2), (1, 3), (1, 2, 3), (1, 5, 4, 3)}
paths = nx.all_simple_paths(G, 1, [2, 3], cutoff=2)
assert {tuple(p) for p in paths} == {(1, 2), (1, 3), (1, 2, 3)}
```

## Next Steps


---

*Source: test_simple_paths.py:154 | Complexity: Intermediate | Last updated: 2026-06-02*