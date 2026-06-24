# How To: Argsort With Na

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test argsort with na

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arrays = value

```python
arrays = [array([2, NA, 1], dtype='Int64'), array([1, 2, 3], dtype='Int64')]
```

### Step 2: Assign index = MultiIndex.from_arrays(...)

```python
index = MultiIndex.from_arrays(arrays)
```

### Step 3: Assign result = index.argsort(...)

```python
result = index.argsort()
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([2, 0, 1], dtype=np.intp)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
arrays = [array([2, NA, 1], dtype='Int64'), array([1, 2, 3], dtype='Int64')]
index = MultiIndex.from_arrays(arrays)
result = index.argsort()
expected = np.array([2, 0, 1], dtype=np.intp)
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_sorted.py:85 | Complexity: Intermediate | Last updated: 2026-06-02*