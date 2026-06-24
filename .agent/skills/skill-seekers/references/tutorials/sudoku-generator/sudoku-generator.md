# How To: Sudoku Generator

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: Generate Sudoku graphs of various sizes and verify their properties.

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `networkx`

**Setup Required:**
```python
# Fixtures: n
```

## Step-by-Step Guide

### Step 1: 'Generate Sudoku graphs of various sizes and verify their properties.'

```python
'Generate Sudoku graphs of various sizes and verify their properties.'
```

**Verification:**
```python
assert not G.is_directed()
```

### Step 2: Assign G = nx.sudoku_graph(...)

```python
G = nx.sudoku_graph(n)
```

**Verification:**
```python
assert not G.is_multigraph()
```

### Step 3: Assign expected_nodes = value

```python
expected_nodes = n ** 4
```

**Verification:**
```python
assert G.number_of_nodes() == expected_nodes
```

### Step 4: Assign expected_degree = value

```python
expected_degree = (n - 1) * (3 * n + 1)
```

**Verification:**
```python
assert G.number_of_edges() == expected_edges
```

### Step 5: Assign expected_edges = value

```python
expected_edges = expected_nodes * expected_degree // 2
```

**Verification:**
```python
assert all((d == expected_degree for _, d in G.degree))
```


## Complete Example

```python
# Setup
# Fixtures: n

# Workflow
'Generate Sudoku graphs of various sizes and verify their properties.'
G = nx.sudoku_graph(n)
expected_nodes = n ** 4
expected_degree = (n - 1) * (3 * n + 1)
expected_edges = expected_nodes * expected_degree // 2
assert not G.is_directed()
assert not G.is_multigraph()
assert G.number_of_nodes() == expected_nodes
assert G.number_of_edges() == expected_edges
assert all((d == expected_degree for _, d in G.degree))
if n == 2:
    assert sorted(G.neighbors(6)) == [2, 3, 4, 5, 7, 10, 14]
elif n == 3:
    assert sorted(G.neighbors(42)) == [6, 15, 24, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 44, 51, 52, 53, 60, 69, 78]
elif n == 4:
    assert sorted(G.neighbors(0)) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 32, 33, 34, 35, 48, 49, 50, 51, 64, 80, 96, 112, 128, 144, 160, 176, 192, 208, 224, 240]
```

## Next Steps


---

*Source: test_sudoku.py:14 | Complexity: Intermediate | Last updated: 2026-06-02*