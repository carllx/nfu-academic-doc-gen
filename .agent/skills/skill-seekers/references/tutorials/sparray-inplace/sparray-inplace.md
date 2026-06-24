# How To: Sparray Inplace

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sparray inplace

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

### Step 3: Assign expected = SparseArray(...)

```python
expected = SparseArray([0, 3, 2, 3], fill_value=0)
```

### Step 4: Call tm.assert_sp_array_equal()

```python
tm.assert_sp_array_equal(sparray, expected)
```


## Complete Example

```python
# Workflow
sparray = SparseArray([0, 2, 0, 0])
ndarray = np.array([0, 1, 2, 3])
sparray += ndarray
expected = SparseArray([0, 3, 2, 3], fill_value=0)
tm.assert_sp_array_equal(sparray, expected)
```

## Next Steps


---

*Source: test_arithmetics.py:458 | Complexity: Intermediate | Last updated: 2026-06-02*