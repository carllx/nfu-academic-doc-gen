# How To: Ufunc Passes Args

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test ufunc passes args

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `functools`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.api.types`

**Setup Required:**
```python
# Fixtures: func, arg, expected
```

## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array([[1, 2], [3, 4]])
```

### Step 2: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame(arr)
```

### Step 3: Assign result_inplace = np.zeros_like(...)

```python
result_inplace = np.zeros_like(arr)
```

### Step 4: Assign expected = np.array.reshape(...)

```python
expected = np.array(expected).reshape(2, 2)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result_inplace, expected)
```

### Step 6: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame(expected)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = func(...)

```python
result = func(df, out=result_inplace)
```

### Step 9: Assign result = func(...)

```python
result = func(df, arg, out=result_inplace)
```


## Complete Example

```python
# Setup
# Fixtures: func, arg, expected

# Workflow
arr = np.array([[1, 2], [3, 4]])
df = pd.DataFrame(arr)
result_inplace = np.zeros_like(arr)
if arg is None:
    result = func(df, out=result_inplace)
else:
    result = func(df, arg, out=result_inplace)
expected = np.array(expected).reshape(2, 2)
tm.assert_numpy_array_equal(result_inplace, expected)
expected = pd.DataFrame(expected)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_ufunc.py:82 | Complexity: Advanced | Last updated: 2026-06-02*