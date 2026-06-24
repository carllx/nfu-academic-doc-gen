# How To: Biconnected Components1

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test biconnected components1

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign edges = value

```python
edges = [(0, 1), (0, 5), (0, 6), (0, 14), (1, 5), (1, 6), (1, 14), (2, 4), (2, 10), (3, 4), (3, 15), (4, 6), (4, 7), (4, 10), (5, 14), (6, 14), (7, 9), (8, 9), (8, 12), (8, 13), (10, 15), (11, 12), (11, 13), (12, 13)]
```

**Verification:**
```python
assert pts == {4, 6, 7, 8, 9}
```

### Step 2: Assign G = nx.Graph(...)

```python
G = nx.Graph(edges)
```

**Verification:**
```python
assert_components_edges_equal(comps, answer)
```

### Step 3: Assign pts = set(...)

```python
pts = set(nx.articulation_points(G))
```

**Verification:**
```python
assert pts == {4, 6, 7, 8, 9}
```

### Step 4: Assign comps = list(...)

```python
comps = list(nx.biconnected_component_edges(G))
```

### Step 5: Assign answer = value

```python
answer = [[(3, 4), (15, 3), (10, 15), (10, 4), (2, 10), (4, 2)], [(13, 12), (13, 8), (11, 13), (12, 11), (8, 12)], [(9, 8)], [(7, 9)], [(4, 7)], [(6, 4)], [(14, 0), (5, 1), (5, 0), (14, 5), (14, 1), (6, 14), (6, 0), (1, 6), (0, 1)]]
```

### Step 6: Call assert_components_edges_equal()

```python
assert_components_edges_equal(comps, answer)
```


## Complete Example

```python
# Workflow
edges = [(0, 1), (0, 5), (0, 6), (0, 14), (1, 5), (1, 6), (1, 14), (2, 4), (2, 10), (3, 4), (3, 15), (4, 6), (4, 7), (4, 10), (5, 14), (6, 14), (7, 9), (8, 9), (8, 12), (8, 13), (10, 15), (11, 12), (11, 13), (12, 13)]
G = nx.Graph(edges)
pts = set(nx.articulation_points(G))
assert pts == {4, 6, 7, 8, 9}
comps = list(nx.biconnected_component_edges(G))
answer = [[(3, 4), (15, 3), (10, 15), (10, 4), (2, 10), (4, 2)], [(13, 12), (13, 8), (11, 13), (12, 11), (8, 12)], [(9, 8)], [(7, 9)], [(4, 7)], [(6, 4)], [(14, 0), (5, 1), (5, 0), (14, 5), (14, 1), (6, 14), (6, 0), (1, 6), (0, 1)]]
assert_components_edges_equal(comps, answer)
```

## Next Steps


---

*Source: test_biconnected.py:80 | Complexity: Intermediate | Last updated: 2026-06-02*