# How To: Bidirectional Shorpath Restricted Wheel

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test bidirectional shortest path restricted wheel

## Prerequisites

**Required Modules:**
- `random`
- `pytest`
- `networkx`
- `networkx`
- `networkx.algorithms.simple_paths`
- `networkx.utils`
- `itertools`
- `itertools`


## Step-by-Step Guide

### Step 1: Assign wheel = nx.wheel_graph(...)

```python
wheel = nx.wheel_graph(6)
```

**Verification:**
```python
assert path in [[1, 0, 3], [1, 2, 3]]
```

### Step 2: Assign unknown = _bidirectional_shortest_path(...)

```python
length, path = _bidirectional_shortest_path(wheel, 1, 3)
```

**Verification:**
```python
assert path == [1, 2, 3]
```

### Step 3: Assign unknown = _bidirectional_shortest_path(...)

```python
length, path = _bidirectional_shortest_path(wheel, 1, 3, ignore_nodes=[0])
```

**Verification:**
```python
assert path == [1, 5, 4, 3]
```

### Step 4: Assign unknown = _bidirectional_shortest_path(...)

```python
length, path = _bidirectional_shortest_path(wheel, 1, 3, ignore_nodes=[0, 2])
```

**Verification:**
```python
assert path in [[1, 2, 0, 3], [1, 5, 4, 3]]
```

### Step 5: Assign unknown = _bidirectional_shortest_path(...)

```python
length, path = _bidirectional_shortest_path(wheel, 1, 3, ignore_edges=[(1, 0), (5, 0), (2, 3)])
```

**Verification:**
```python
assert path in [[1, 2, 0, 3], [1, 5, 4, 3]]
```


## Complete Example

```python
# Workflow
wheel = nx.wheel_graph(6)
length, path = _bidirectional_shortest_path(wheel, 1, 3)
assert path in [[1, 0, 3], [1, 2, 3]]
length, path = _bidirectional_shortest_path(wheel, 1, 3, ignore_nodes=[0])
assert path == [1, 2, 3]
length, path = _bidirectional_shortest_path(wheel, 1, 3, ignore_nodes=[0, 2])
assert path == [1, 5, 4, 3]
length, path = _bidirectional_shortest_path(wheel, 1, 3, ignore_edges=[(1, 0), (5, 0), (2, 3)])
assert path in [[1, 2, 0, 3], [1, 5, 4, 3]]
```

## Next Steps


---

*Source: test_simple_paths.py:655 | Complexity: Intermediate | Last updated: 2026-06-02*