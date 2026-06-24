# How To: Example 2

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test example 2

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.generators`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

**Verification:**
```python
assert nx.is_isomorphic(H, solution)
```

### Step 2: Assign G_edges = value

```python
G_edges = [[1, 2], [1, 3], [2, 3], [3, 4], [3, 5], [4, 5]]
```

### Step 3: Call G.add_edges_from()

```python
G.add_edges_from(G_edges)
```

### Step 4: Assign H = nx.inverse_line_graph(...)

```python
H = nx.inverse_line_graph(G)
```

### Step 5: Assign solution = nx.Graph(...)

```python
solution = nx.Graph()
```

### Step 6: Assign solution_edges = value

```python
solution_edges = [('a', 'c'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('d', 'f')]
```

### Step 7: Call solution.add_edges_from()

```python
solution.add_edges_from(solution_edges)
```

**Verification:**
```python
assert nx.is_isomorphic(H, solution)
```


## Complete Example

```python
# Workflow
G = nx.Graph()
G_edges = [[1, 2], [1, 3], [2, 3], [3, 4], [3, 5], [4, 5]]
G.add_edges_from(G_edges)
H = nx.inverse_line_graph(G)
solution = nx.Graph()
solution_edges = [('a', 'c'), ('b', 'c'), ('c', 'd'), ('d', 'e'), ('d', 'f')]
solution.add_edges_from(solution_edges)
assert nx.is_isomorphic(H, solution)
```

## Next Steps


---

*Source: test_line.py:130 | Complexity: Intermediate | Last updated: 2026-06-02*