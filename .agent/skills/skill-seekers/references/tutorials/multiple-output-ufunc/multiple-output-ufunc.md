# How To: Multiple Output Ufunc

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multiple output ufunc

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
# Fixtures: sparse, arrays_for_binary_ufunc
```

## Step-by-Step Guide

### Step 1: Assign unknown = arrays_for_binary_ufunc

```python
arr, _ = arrays_for_binary_ufunc
```

**Verification:**
```python
assert isinstance(result, tuple)
```

### Step 2: Assign series = pd.Series(...)

```python
series = pd.Series(arr, name='name')
```

**Verification:**
```python
assert isinstance(expected, tuple)
```

### Step 3: Assign result = np.modf(...)

```python
result = np.modf(series)
```

### Step 4: Assign expected = np.modf(...)

```python
expected = np.modf(arr)
```

**Verification:**
```python
assert isinstance(result, tuple)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result[0], pd.Series(expected[0], name='name'))
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result[1], pd.Series(expected[1], name='name'))
```

### Step 7: Assign arr = SparseArray(...)

```python
arr = SparseArray(arr)
```


## Complete Example

```python
# Setup
# Fixtures: sparse, arrays_for_binary_ufunc

# Workflow
arr, _ = arrays_for_binary_ufunc
if sparse:
    arr = SparseArray(arr)
series = pd.Series(arr, name='name')
result = np.modf(series)
expected = np.modf(arr)
assert isinstance(result, tuple)
assert isinstance(expected, tuple)
tm.assert_series_equal(result[0], pd.Series(expected[0], name='name'))
tm.assert_series_equal(result[1], pd.Series(expected[1], name='name'))
```

## Next Steps


---

*Source: test_ufunc.py:206 | Complexity: Intermediate | Last updated: 2026-06-02*