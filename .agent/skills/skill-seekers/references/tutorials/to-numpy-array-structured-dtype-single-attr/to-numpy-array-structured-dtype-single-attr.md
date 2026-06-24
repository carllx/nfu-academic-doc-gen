# How To: To Numpy Array Structured Dtype Single Attr

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test to numpy array structured dtype single attr

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.utils`

**Setup Required:**
```python
# Fixtures: field_name, expected_attr_val
```

## Step-by-Step Guide

### Step 1: Assign G = nx.Graph(...)

```python
G = nx.Graph()
```

### Step 2: Call G.add_edge()

```python
G.add_edge(0, 1, cost=3)
```

### Step 3: Assign dtype = np.dtype(...)

```python
dtype = np.dtype([(field_name, float)])
```

### Step 4: Assign A = nx.to_numpy_array(...)

```python
A = nx.to_numpy_array(G, dtype=dtype, weight=None)
```

### Step 5: Assign expected = np.array(...)

```python
expected = np.array([[0, expected_attr_val], [expected_attr_val, 0]], dtype=float)
```

### Step 6: Call npt.assert_array_equal()

```python
npt.assert_array_equal(A[field_name], expected)
```


## Complete Example

```python
# Setup
# Fixtures: field_name, expected_attr_val

# Workflow
G = nx.Graph()
G.add_edge(0, 1, cost=3)
dtype = np.dtype([(field_name, float)])
A = nx.to_numpy_array(G, dtype=dtype, weight=None)
expected = np.array([[0, expected_attr_val], [expected_attr_val, 0]], dtype=float)
npt.assert_array_equal(A[field_name], expected)
```

## Next Steps


---

*Source: test_convert_numpy.py:327 | Complexity: Intermediate | Last updated: 2026-06-02*