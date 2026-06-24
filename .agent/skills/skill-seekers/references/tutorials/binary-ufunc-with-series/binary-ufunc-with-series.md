# How To: Binary Ufunc With Series

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test binary ufunc with series

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
# Fixtures: flip, shuffle, sparse, ufunc, arrays_for_binary_ufunc
```

## Step-by-Step Guide

### Step 1: Assign unknown = arrays_for_binary_ufunc

```python
a1, a2 = arrays_for_binary_ufunc
```

### Step 2: Assign name = 'name'

```python
name = 'name'
```

### Step 3: Assign series = pd.Series(...)

```python
series = pd.Series(a1, name=name)
```

### Step 4: Assign other = pd.Series(...)

```python
other = pd.Series(a2, name=name)
```

### Step 5: Assign idx = np.random.default_rng.permutation(...)

```python
idx = np.random.default_rng(2).permutation(len(a1))
```

### Step 6: Assign array_args = value

```python
array_args = (a1, a2)
```

### Step 7: Assign series_args = value

```python
series_args = (series, other)
```

### Step 8: Assign expected = pd.Series(...)

```python
expected = pd.Series(ufunc(*array_args), index=index, name=name)
```

### Step 9: Assign result = ufunc(...)

```python
result = ufunc(*series_args)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 11: Assign a1 = SparseArray(...)

```python
a1 = SparseArray(a1, dtype=pd.SparseDtype('int64', 0))
```

### Step 12: Assign a2 = SparseArray(...)

```python
a2 = SparseArray(a2, dtype=pd.SparseDtype('int64', 0))
```

### Step 13: Assign other = other.take(...)

```python
other = other.take(idx)
```

### Step 14: Assign index = value

```python
index = series.index
```

### Step 15: Assign array_args = tuple(...)

```python
array_args = tuple(reversed(array_args))
```

### Step 16: Assign series_args = tuple(...)

```python
series_args = tuple(reversed(series_args))
```

### Step 17: Assign index = value

```python
index = other.align(series)[0].index
```

### Step 18: Assign index = value

```python
index = series.align(other)[0].index
```


## Complete Example

```python
# Setup
# Fixtures: flip, shuffle, sparse, ufunc, arrays_for_binary_ufunc

# Workflow
a1, a2 = arrays_for_binary_ufunc
if sparse:
    a1 = SparseArray(a1, dtype=pd.SparseDtype('int64', 0))
    a2 = SparseArray(a2, dtype=pd.SparseDtype('int64', 0))
name = 'name'
series = pd.Series(a1, name=name)
other = pd.Series(a2, name=name)
idx = np.random.default_rng(2).permutation(len(a1))
if shuffle:
    other = other.take(idx)
    if flip:
        index = other.align(series)[0].index
    else:
        index = series.align(other)[0].index
else:
    index = series.index
array_args = (a1, a2)
series_args = (series, other)
if flip:
    array_args = tuple(reversed(array_args))
    series_args = tuple(reversed(series_args))
expected = pd.Series(ufunc(*array_args), index=index, name=name)
result = ufunc(*series_args)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_ufunc.py:111 | Complexity: Advanced | Last updated: 2026-06-02*