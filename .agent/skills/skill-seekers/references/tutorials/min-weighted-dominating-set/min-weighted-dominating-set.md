# How To: Min Weighted Dominating Set

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test min weighted dominating set

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx.algorithms.approximation`


## Step-by-Step Guide

### Step 1: Assign graph = nx.Graph(...)

```python
graph = nx.Graph()
```

**Verification:**
```python
assert len(neighbors & dom_set) > 0, 'Non dominating set found!'
```

### Step 2: Call graph.add_edge()

```python
graph.add_edge(1, 2)
```

### Step 3: Call graph.add_edge()

```python
graph.add_edge(1, 5)
```

### Step 4: Call graph.add_edge()

```python
graph.add_edge(2, 3)
```

### Step 5: Call graph.add_edge()

```python
graph.add_edge(2, 5)
```

### Step 6: Call graph.add_edge()

```python
graph.add_edge(3, 4)
```

### Step 7: Call graph.add_edge()

```python
graph.add_edge(3, 6)
```

### Step 8: Call graph.add_edge()

```python
graph.add_edge(5, 6)
```

### Step 9: Assign vertices = value

```python
vertices = {1, 2, 3, 4, 5, 6}
```

### Step 10: Assign dom_set = min_weighted_dominating_set(...)

```python
dom_set = min_weighted_dominating_set(graph)
```

### Step 11: Assign neighbors = set(...)

```python
neighbors = set(graph.neighbors(vertex))
```

**Verification:**
```python
assert len(neighbors & dom_set) > 0, 'Non dominating set found!'
```


## Complete Example

```python
# Workflow
graph = nx.Graph()
graph.add_edge(1, 2)
graph.add_edge(1, 5)
graph.add_edge(2, 3)
graph.add_edge(2, 5)
graph.add_edge(3, 4)
graph.add_edge(3, 6)
graph.add_edge(5, 6)
vertices = {1, 2, 3, 4, 5, 6}
dom_set = min_weighted_dominating_set(graph)
for vertex in vertices - dom_set:
    neighbors = set(graph.neighbors(vertex))
    assert len(neighbors & dom_set) > 0, 'Non dominating set found!'
```

## Next Steps


---

*Source: test_dominating_set.py:11 | Complexity: Advanced | Last updated: 2026-06-02*