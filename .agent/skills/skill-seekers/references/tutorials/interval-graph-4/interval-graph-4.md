# How To: Interval Graph 4

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test all possible overlaps

## Prerequisites

**Required Modules:**
- `math`
- `pytest`
- `networkx`
- `networkx.generators.interval_graph`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: 'test all possible overlaps'

```python
'test all possible overlaps'
```

**Verification:**
```python
assert set(actual_nbrs) == expected_nbrs
```

### Step 2: Assign intervals = value

```python
intervals = [(0, 2), (-2, -1), (-2, 0), (-2, 1), (-2, 2), (-2, 3), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (3, 4)]
```

### Step 3: Assign expected_graph = nx.Graph(...)

```python
expected_graph = nx.Graph()
```

### Step 4: Call expected_graph.add_nodes_from()

```python
expected_graph.add_nodes_from(intervals)
```

### Step 5: Assign expected_nbrs = value

```python
expected_nbrs = {(-2, 0), (-2, 1), (-2, 2), (-2, 3), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)}
```

### Step 6: Assign actual_g = nx.interval_graph(...)

```python
actual_g = nx.interval_graph(intervals)
```

### Step 7: Assign actual_nbrs = nx.neighbors(...)

```python
actual_nbrs = nx.neighbors(actual_g, (0, 2))
```

**Verification:**
```python
assert set(actual_nbrs) == expected_nbrs
```


## Complete Example

```python
# Workflow
'test all possible overlaps'
intervals = [(0, 2), (-2, -1), (-2, 0), (-2, 1), (-2, 2), (-2, 3), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (3, 4)]
expected_graph = nx.Graph()
expected_graph.add_nodes_from(intervals)
expected_nbrs = {(-2, 0), (-2, 1), (-2, 2), (-2, 3), (0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)}
actual_g = nx.interval_graph(intervals)
actual_nbrs = nx.neighbors(actual_g, (0, 2))
assert set(actual_nbrs) == expected_nbrs
```

## Next Steps


---

*Source: test_interval_graph.py:94 | Complexity: Intermediate | Last updated: 2026-06-02*