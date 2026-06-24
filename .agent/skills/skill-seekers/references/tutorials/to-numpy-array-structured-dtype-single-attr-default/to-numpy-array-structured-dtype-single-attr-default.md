# How To: To Numpy Array Structured Dtype Single Attr Default

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to numpy array structured dtype single attr default

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `networkx`
- `networkx.utils`


## Step-by-Step Guide

### Step 1: Assign G = nx.path_graph(...)

```python
G = nx.path_graph(3)
```

### Step 2: Assign dtype = np.dtype(...)

```python
dtype = np.dtype([('weight', float)])
```

### Step 3: Assign A = nx.to_numpy_array(...)

```python
A = nx.to_numpy_array(G, dtype=dtype, weight=None)
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]], dtype=float)
```

### Step 5: Call npt.assert_array_equal()

```python
npt.assert_array_equal(A['weight'], expected)
```


## Complete Example

```python
# Workflow
G = nx.path_graph(3)
dtype = np.dtype([('weight', float)])
A = nx.to_numpy_array(G, dtype=dtype, weight=None)
expected = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]], dtype=float)
npt.assert_array_equal(A['weight'], expected)
```

## Next Steps


---

*Source: test_convert_numpy.py:312 | Complexity: Intermediate | Last updated: 2026-06-02*