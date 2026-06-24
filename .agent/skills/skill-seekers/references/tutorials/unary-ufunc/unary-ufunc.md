# How To: Unary Ufunc

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test unary ufunc

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
# Fixtures: ufunc, sparse
```

## Step-by-Step Guide

### Step 1: Assign arr = np.random.default_rng.integers(...)

```python
arr = np.random.default_rng(2).integers(0, 10, 10, dtype='int64')
```

### Step 2: Assign unknown = 0

```python
arr[::2] = 0
```

### Step 3: Assign index = list(...)

```python
index = list(string.ascii_letters[:10])
```

### Step 4: Assign name = 'name'

```python
name = 'name'
```

### Step 5: Assign series = pd.Series(...)

```python
series = pd.Series(arr, index=index, name=name)
```

### Step 6: Assign result = ufunc(...)

```python
result = ufunc(series)
```

### Step 7: Assign expected = pd.Series(...)

```python
expected = pd.Series(ufunc(arr), index=index, name=name)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 9: Assign arr = SparseArray(...)

```python
arr = SparseArray(arr, dtype=pd.SparseDtype('int64', 0))
```


## Complete Example

```python
# Setup
# Fixtures: ufunc, sparse

# Workflow
arr = np.random.default_rng(2).integers(0, 10, 10, dtype='int64')
arr[::2] = 0
if sparse:
    arr = SparseArray(arr, dtype=pd.SparseDtype('int64', 0))
index = list(string.ascii_letters[:10])
name = 'name'
series = pd.Series(arr, index=index, name=name)
result = ufunc(series)
expected = pd.Series(ufunc(arr), index=index, name=name)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_ufunc.py:42 | Complexity: Advanced | Last updated: 2026-06-02*