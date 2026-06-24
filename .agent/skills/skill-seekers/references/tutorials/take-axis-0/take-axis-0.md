# How To: Take Axis 0

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test take axis 0

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._testing`
- `pandas.core.algorithms`


## Step-by-Step Guide

### Step 1: Assign arr = np.arange.reshape(...)

```python
arr = np.arange(12).reshape(4, 3)
```

### Step 2: Assign result = algos.take(...)

```python
result = algos.take(arr, [0, -1])
```

### Step 3: Assign expected = np.array(...)

```python
expected = np.array([[0, 1, 2], [9, 10, 11]])
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 5: Assign result = algos.take(...)

```python
result = algos.take(arr, [0, -1], allow_fill=True, fill_value=0)
```

### Step 6: Assign expected = np.array(...)

```python
expected = np.array([[0, 1, 2], [0, 0, 0]])
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
arr = np.arange(12).reshape(4, 3)
result = algos.take(arr, [0, -1])
expected = np.array([[0, 1, 2], [9, 10, 11]])
tm.assert_numpy_array_equal(result, expected)
result = algos.take(arr, [0, -1], allow_fill=True, fill_value=0)
expected = np.array([[0, 1, 2], [0, 0, 0]])
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_take.py:215 | Complexity: Intermediate | Last updated: 2026-06-02*