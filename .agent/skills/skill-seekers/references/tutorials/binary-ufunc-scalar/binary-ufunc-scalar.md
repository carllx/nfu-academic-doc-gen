# How To: Binary Ufunc Scalar

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test binary ufunc scalar

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `re`
- `string`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.arrays`

**Setup Required:**
```python
# Fixtures: ufunc, sparse, flip, arrays_for_binary_ufunc
```

## Step-by-Step Guide

### Step 1: Assign unknown = arrays_for_binary_ufunc

```python
arr, _ = arrays_for_binary_ufunc
```

### Step 2: Assign other = 2

```python
other = 2
```

### Step 3: Assign series = pd.Series(...)

```python
series = pd.Series(arr, name='name')
```

### Step 4: Assign series_args = value

```python
series_args = (series, other)
```

### Step 5: Assign array_args = value

```python
array_args = (arr, other)
```

### Step 6: Assign expected = pd.Series(...)

```python
expected = pd.Series(ufunc(*array_args), name='name')
```

### Step 7: Assign result = ufunc(...)

```python
result = ufunc(*series_args)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 9: Assign arr = SparseArray(...)

```python
arr = SparseArray(arr)
```

### Step 10: Assign series_args = tuple(...)

```python
series_args = tuple(reversed(series_args))
```

### Step 11: Assign array_args = tuple(...)

```python
array_args = tuple(reversed(array_args))
```


## Complete Example

```python
# Setup
# Fixtures: ufunc, sparse, flip, arrays_for_binary_ufunc

# Workflow
arr, _ = arrays_for_binary_ufunc
if sparse:
    arr = SparseArray(arr)
other = 2
series = pd.Series(arr, name='name')
series_args = (series, other)
array_args = (arr, other)
if flip:
    series_args = tuple(reversed(series_args))
    array_args = tuple(reversed(array_args))
expected = pd.Series(ufunc(*array_args), name='name')
result = ufunc(*series_args)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_ufunc.py:150 | Complexity: Advanced | Last updated: 2026-06-02*