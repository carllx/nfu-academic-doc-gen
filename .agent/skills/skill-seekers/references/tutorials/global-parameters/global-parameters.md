# How To: Global Parameters

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test global parameters

## Prerequisites

**Required Modules:**
- `pytest`
- `networkx`
- `networkx`


## Step-by-Step Guide

### Step 1: Assign unknown = nx.intersection_array(...)

```python
b, c = nx.intersection_array(nx.cycle_graph(5))
```

**Verification:**
```python
assert list(g) == [(0, 0, 2), (1, 0, 1), (1, 1, 0)]
```

### Step 2: Assign g = nx.global_parameters(...)

```python
g = nx.global_parameters(b, c)
```

**Verification:**
```python
assert list(g) == [(0, 0, 2), (1, 1, 0)]
```

### Step 3: Assign unknown = nx.intersection_array(...)

```python
b, c = nx.intersection_array(nx.cycle_graph(3))
```

### Step 4: Assign g = nx.global_parameters(...)

```python
g = nx.global_parameters(b, c)
```

**Verification:**
```python
assert list(g) == [(0, 0, 2), (1, 1, 0)]
```


## Complete Example

```python
# Workflow
b, c = nx.intersection_array(nx.cycle_graph(5))
g = nx.global_parameters(b, c)
assert list(g) == [(0, 0, 2), (1, 0, 1), (1, 1, 0)]
b, c = nx.intersection_array(nx.cycle_graph(3))
g = nx.global_parameters(b, c)
assert list(g) == [(0, 0, 2), (1, 1, 0)]
```

## Next Steps


---

*Source: test_distance_regular.py:36 | Complexity: Intermediate | Last updated: 2026-06-02*