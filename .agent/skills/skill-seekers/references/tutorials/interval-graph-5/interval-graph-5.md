# How To: Interval Graph 5

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: this test is to see that an interval supports infinite number

## Prerequisites

**Required Modules:**
- `math`
- `pytest`
- `networkx`
- `networkx.generators.interval_graph`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: 'this test is to see that an interval supports infinite number'

```python
'this test is to see that an interval supports infinite number'
```

**Verification:**
```python
assert set(actual_g.nodes) == set(expected_graph.nodes)
```

### Step 2: Assign intervals = value

```python
intervals = {(-math.inf, 0), (-1, -1), (0.5, 0.5), (1, 1), (1, math.inf)}
```

**Verification:**
```python
assert edges_equal(expected_graph, actual_g)
```

### Step 3: Assign expected_graph = nx.Graph(...)

```python
expected_graph = nx.Graph()
```

### Step 4: Call expected_graph.add_nodes_from()

```python
expected_graph.add_nodes_from(intervals)
```

### Step 5: Assign e1 = value

```python
e1 = ((-math.inf, 0), (-1, -1))
```

### Step 6: Assign e2 = value

```python
e2 = ((1, 1), (1, math.inf))
```

### Step 7: Call expected_graph.add_edges_from()

```python
expected_graph.add_edges_from([e1, e2])
```

### Step 8: Assign actual_g = interval_graph(...)

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
'this test is to see that an interval supports infinite number'
intervals = {(-math.inf, 0), (-1, -1), (0.5, 0.5), (1, 1), (1, math.inf)}
expected_graph = nx.Graph()
expected_graph.add_nodes_from(intervals)
e1 = ((-math.inf, 0), (-1, -1))
e2 = ((1, 1), (1, math.inf))
expected_graph.add_edges_from([e1, e2])
actual_g = interval_graph(intervals)
assert set(actual_g.nodes) == set(expected_graph.nodes)
assert edges_equal(expected_graph, actual_g)
```

## Next Steps


---

*Source: test_interval_graph.py:131 | Complexity: Advanced | Last updated: 2026-06-02*