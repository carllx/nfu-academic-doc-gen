# How To: Visibility Graph  Convex Series  Complete Graph

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: test visibility graph  convex series  complete graph

## Prerequisites

**Required Modules:**
- `itertools`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign series = value

```python
series = [i ** 2 for i in range(10)]
```

**Verification:**
```python
assert actual_graph.number_of_nodes() == expected_series_length
```

### Step 2: Assign expected_series_length = len(...)

```python
expected_series_length = len(series)
```

**Verification:**
```python
assert actual_graph.number_of_edges() == 45
```

### Step 3: Assign actual_graph = nx.visibility_graph(...)

```python
actual_graph = nx.visibility_graph(series)
```

**Verification:**
```python
assert nx.is_isomorphic(actual_graph, nx.complete_graph(expected_series_length))
```


## Complete Example

```python
# Workflow
series = [i ** 2 for i in range(10)]
expected_series_length = len(series)
actual_graph = nx.visibility_graph(series)
assert actual_graph.number_of_nodes() == expected_series_length
assert actual_graph.number_of_edges() == 45
assert nx.is_isomorphic(actual_graph, nx.complete_graph(expected_series_length))
```

## Next Steps


---

*Source: test_time_series.py:24 | Complexity: Beginner | Last updated: 2026-06-02*