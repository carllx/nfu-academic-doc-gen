# How To: Ndarray Inplace

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ndarray inplace

## Prerequisites

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`


## Step-by-Step Guide

### Step 1: Assign sparray = SparseArray(...)

```python
sparray = SparseArray([0, 2, 0, 0])
```

### Step 2: Assign ndarray = np.array(...)

```python
ndarray = np.array([0, 1, 2, 3])
```

### Step 3: Assign expected = np.array(...)

```python
expected = np.array([0, 3, 2, 3])
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(ndarray, expected)
```


## Complete Example

```python
# Workflow
sparray = SparseArray([0, 2, 0, 0])
ndarray = np.array([0, 1, 2, 3])
ndarray += sparray
expected = np.array([0, 3, 2, 3])
tm.assert_numpy_array_equal(ndarray, expected)
```

## Next Steps


---

*Source: test_arithmetics.py:450 | Complexity: Intermediate | Last updated: 2026-06-02*