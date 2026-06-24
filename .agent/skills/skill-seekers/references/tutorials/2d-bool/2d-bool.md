# How To: 2D Bool

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test 2d bool

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._testing`
- `pandas.core.algorithms`


## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 1]], dtype=bool)
```

**Verification:**
```python
assert result.dtype == np.object_
```

### Step 2: Assign result = algos.take_nd(...)

```python
result = algos.take_nd(arr, [0, 2, 2, 1])
```

### Step 3: Assign expected = arr.take(...)

```python
expected = arr.take([0, 2, 2, 1], axis=0)
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 5: Assign result = algos.take_nd(...)

```python
result = algos.take_nd(arr, [0, 2, 2, 1], axis=1)
```

### Step 6: Assign expected = arr.take(...)

```python
expected = arr.take([0, 2, 2, 1], axis=1)
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 8: Assign result = algos.take_nd(...)

```python
result = algos.take_nd(arr, [0, 2, -1])
```

**Verification:**
```python
assert result.dtype == np.object_
```


## Complete Example

```python
# Workflow
arr = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 1]], dtype=bool)
result = algos.take_nd(arr, [0, 2, 2, 1])
expected = arr.take([0, 2, 2, 1], axis=0)
tm.assert_numpy_array_equal(result, expected)
result = algos.take_nd(arr, [0, 2, 2, 1], axis=1)
expected = arr.take([0, 2, 2, 1], axis=1)
tm.assert_numpy_array_equal(result, expected)
result = algos.take_nd(arr, [0, 2, -1])
assert result.dtype == np.object_
```

## Next Steps


---

*Source: test_take.py:153 | Complexity: Advanced | Last updated: 2026-06-02*