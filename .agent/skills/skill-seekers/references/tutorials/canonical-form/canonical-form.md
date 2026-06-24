# How To: Canonical Form

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test canonical form

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign T = nx.Graph(...)

```python
T = nx.Graph()
```

**Verification:**
```python
assert actual == expected
```

### Step 2: Call T.add_edges_from()

```python
T.add_edges_from([(0, 1), (0, 2), (0, 3)])
```

### Step 3: Call T.add_edges_from()

```python
T.add_edges_from([(1, 4), (1, 5)])
```

### Step 4: Call T.add_edges_from()

```python
T.add_edges_from([(3, 6), (3, 7)])
```

### Step 5: Assign root = 0

```python
root = 0
```

### Step 6: Assign actual = nx.to_nested_tuple(...)

```python
actual = nx.to_nested_tuple(T, root, canonical_form=True)
```

### Step 7: Assign expected = value

```python
expected = ((), ((), ()), ((), ()))
```

**Verification:**
```python
assert actual == expected
```


## Complete Example

```python
# Workflow
T = nx.Graph()
T.add_edges_from([(0, 1), (0, 2), (0, 3)])
T.add_edges_from([(1, 4), (1, 5)])
T.add_edges_from([(3, 6), (3, 7)])
root = 0
actual = nx.to_nested_tuple(T, root, canonical_form=True)
expected = ((), ((), ()), ((), ()))
assert actual == expected
```

## Next Steps


---

*Source: test_coding.py:93 | Complexity: Intermediate | Last updated: 2026-06-02*