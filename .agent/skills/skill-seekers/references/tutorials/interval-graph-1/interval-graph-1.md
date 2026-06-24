# How To: Interval Graph 1

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test interval graph 1

## Prerequisites

**Required Modules:**
- `math`
- `pytest`
- `networkx`
- `networkx.generators.interval_graph`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign intervals = value

```python
intervals = [(1, 2), (2, 3), (3, 4), (1, 4)]
```

**Verification:**
```python
assert set(actual_g.nodes) == set(expected_graph.nodes)
```

### Step 2: Assign expected_graph = nx.Graph(...)

```python
expected_graph = nx.Graph()
```

**Verification:**
```python
assert edges_equal(expected_graph, actual_g)
```

### Step 3: Call expected_graph.add_nodes_from()

```python
expected_graph.add_nodes_from(intervals)
```

### Step 4: Assign e1 = value

```python
e1 = ((1, 4), (1, 2))
```

### Step 5: Assign e2 = value

```python
e2 = ((1, 4), (2, 3))
```

### Step 6: Assign e3 = value

```python
e3 = ((1, 4), (3, 4))
```

### Step 7: Assign e4 = value

```python
e4 = ((3, 4), (2, 3))
```

### Step 8: Assign e5 = value

```python
e5 = ((1, 2), (2, 3))
```

### Step 9: Call expected_graph.add_edges_from()

```python
expected_graph.add_edges_from([e1, e2, e3, e4, e5])
```

### Step 10: Assign actual_g = interval_graph(...)

```python
actual_g = interval_graph(intervals)
```

**Verification:**
```python
assert set(actual_g.nodes) == set(expected_graph.nodes)
```


## Complete Example

```python
# Workflow
intervals = [(1, 2), (2, 3), (3, 4), (1, 4)]
expected_graph = nx.Graph()
expected_graph.add_nodes_from(intervals)
e1 = ((1, 4), (1, 2))
e2 = ((1, 4), (2, 3))
e3 = ((1, 4), (3, 4))
e4 = ((3, 4), (2, 3))
e5 = ((1, 2), (2, 3))
expected_graph.add_edges_from([e1, e2, e3, e4, e5])
actual_g = interval_graph(intervals)
assert set(actual_g.nodes) == set(expected_graph.nodes)
assert edges_equal(expected_graph, actual_g)
```

## Next Steps


---

*Source: test_interval_graph.py:49 | Complexity: Advanced | Last updated: 2026-06-02*