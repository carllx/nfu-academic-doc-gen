# How To: Optimal Edit Paths

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test optimal edit paths

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.similarity`
- `networkx.generators.classic`


## Step-by-Step Guide

### Step 1: Assign G1 = path_graph(...)

```python
G1 = path_graph(3)
```

**Verification:**
```python
assert cost == 1
```

### Step 2: Assign G2 = cycle_graph(...)

```python
G2 = cycle_graph(3)
```

**Verification:**
```python
assert len(paths) == 6
```

### Step 3: Assign unknown = optimal_edit_paths(...)

```python
paths, cost = optimal_edit_paths(G1, G2)
```

**Verification:**
```python
assert {canonical(*p) for p in paths} == {canonical(*p) for p in expected_paths}
```

### Step 4: Assign expected_paths = value

```python
expected_paths = [([(0, 0), (1, 1), (2, 2)], [((0, 1), (0, 1)), ((1, 2), (1, 2)), (None, (0, 2))]), ([(0, 0), (1, 2), (2, 1)], [((0, 1), (0, 2)), ((1, 2), (1, 2)), (None, (0, 1))]), ([(0, 1), (1, 0), (2, 2)], [((0, 1), (0, 1)), ((1, 2), (0, 2)), (None, (1, 2))]), ([(0, 1), (1, 2), (2, 0)], [((0, 1), (1, 2)), ((1, 2), (0, 2)), (None, (0, 1))]), ([(0, 2), (1, 0), (2, 1)], [((0, 1), (0, 2)), ((1, 2), (0, 1)), (None, (1, 2))]), ([(0, 2), (1, 1), (2, 0)], [((0, 1), (1, 2)), ((1, 2), (0, 1)), (None, (0, 2))])]
```

**Verification:**
```python
assert {canonical(*p) for p in paths} == {canonical(*p) for p in expected_paths}
```


## Complete Example

```python
# Workflow
G1 = path_graph(3)
G2 = cycle_graph(3)
paths, cost = optimal_edit_paths(G1, G2)
assert cost == 1
assert len(paths) == 6

def canonical(vertex_path, edge_path):
    return (tuple(sorted(vertex_path)), tuple(sorted(edge_path, key=lambda x: (None in x, x))))
expected_paths = [([(0, 0), (1, 1), (2, 2)], [((0, 1), (0, 1)), ((1, 2), (1, 2)), (None, (0, 2))]), ([(0, 0), (1, 2), (2, 1)], [((0, 1), (0, 2)), ((1, 2), (1, 2)), (None, (0, 1))]), ([(0, 1), (1, 0), (2, 2)], [((0, 1), (0, 1)), ((1, 2), (0, 2)), (None, (1, 2))]), ([(0, 1), (1, 2), (2, 0)], [((0, 1), (1, 2)), ((1, 2), (0, 2)), (None, (0, 1))]), ([(0, 2), (1, 0), (2, 1)], [((0, 1), (0, 2)), ((1, 2), (0, 1)), (None, (1, 2))]), ([(0, 2), (1, 1), (2, 0)], [((0, 1), (1, 2)), ((1, 2), (0, 1)), (None, (0, 2))])]
assert {canonical(*p) for p in paths} == {canonical(*p) for p in expected_paths}
```

## Next Steps


---

*Source: test_similarity.py:231 | Complexity: Intermediate | Last updated: 2026-06-02*