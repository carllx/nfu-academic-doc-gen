# How To: Non Edges

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test non edges

## Prerequisites

**Required Modules:**
- `random`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign graph = nx.complete_graph(...)

```python
graph = nx.complete_graph(5)
```

**Verification:**
```python
assert len(nedges) == 0
```

### Step 2: Assign nedges = list(...)

```python
nedges = list(nx.non_edges(graph))
```

**Verification:**
```python
assert (u, v) in nedges or (v, u) in nedges
```

### Step 3: Assign graph = nx.path_graph(...)

```python
graph = nx.path_graph(4)
```

**Verification:**
```python
assert (u, v) in nedges or (v, u) in nedges
```

### Step 4: Assign expected = value

```python
expected = [(0, 2), (0, 3), (1, 3)]
```

**Verification:**
```python
assert e in nedges
```

### Step 5: Assign nedges = list(...)

```python
nedges = list(nx.non_edges(graph))
```

### Step 6: Assign graph = nx.star_graph(...)

```python
graph = nx.star_graph(4)
```

### Step 7: Assign expected = value

```python
expected = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
```

### Step 8: Assign nedges = list(...)

```python
nedges = list(nx.non_edges(graph))
```

### Step 9: Assign graph = nx.DiGraph(...)

```python
graph = nx.DiGraph()
```

### Step 10: Call graph.add_edges_from()

```python
graph.add_edges_from([(0, 2), (2, 0), (2, 1)])
```

### Step 11: Assign expected = value

```python
expected = [(0, 1), (1, 0), (1, 2)]
```

### Step 12: Assign nedges = list(...)

```python
nedges = list(nx.non_edges(graph))
```

**Verification:**
```python
assert (u, v) in nedges or (v, u) in nedges
```


## Complete Example

```python
# Workflow
graph = nx.complete_graph(5)
nedges = list(nx.non_edges(graph))
assert len(nedges) == 0
graph = nx.path_graph(4)
expected = [(0, 2), (0, 3), (1, 3)]
nedges = list(nx.non_edges(graph))
for u, v in expected:
    assert (u, v) in nedges or (v, u) in nedges
graph = nx.star_graph(4)
expected = [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]
nedges = list(nx.non_edges(graph))
for u, v in expected:
    assert (u, v) in nedges or (v, u) in nedges
graph = nx.DiGraph()
graph.add_edges_from([(0, 2), (2, 0), (2, 1)])
expected = [(0, 1), (1, 0), (1, 2)]
nedges = list(nx.non_edges(graph))
for e in expected:
    assert e in nedges
```

## Next Steps


---

*Source: test_function.py:339 | Complexity: Advanced | Last updated: 2026-06-02*