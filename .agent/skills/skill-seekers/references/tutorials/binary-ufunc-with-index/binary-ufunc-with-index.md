# How To: Binary Ufunc With Index

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test binary ufunc with index

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
# Fixtures: flip, sparse, ufunc, arrays_for_binary_ufunc
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

### Step 4: Assign other = pd.Index.astype(...)

```python
other = pd.Index(a2, name=name).astype('int64')
```

### Step 5: Assign array_args = value

```python
array_args = (a1, a2)
```

### Step 6: Assign series_args = value

```python
series_args = (series, other)
```

### Step 7: Assign expected = pd.Series(...)

```python
expected = pd.Series(ufunc(*array_args), name=name)
```

### Step 8: Assign result = ufunc(...)

```python
result = ufunc(*series_args)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 10: Assign a1 = SparseArray(...)

```python
a1 = SparseArray(a1, dtype=pd.SparseDtype('int64', 0))
```

### Step 11: Assign a2 = SparseArray(...)

```python
a2 = SparseArray(a2, dtype=pd.SparseDtype('int64', 0))
```

### Step 12: Assign array_args = reversed(...)

```python
array_args = reversed(array_args)
```

### Step 13: Assign series_args = reversed(...)

```python
series_args = reversed(series_args)
```


## Complete Example

```python
# Setup
# Fixtures: flip, sparse, ufunc, arrays_for_binary_ufunc

# Workflow
a1, a2 = arrays_for_binary_ufunc
if sparse:
    a1 = SparseArray(a1, dtype=pd.SparseDtype('int64', 0))
    a2 = SparseArray(a2, dtype=pd.SparseDtype('int64', 0))
name = 'name'
series = pd.Series(a1, name=name)
other = pd.Index(a2, name=name).astype('int64')
array_args = (a1, a2)
series_args = (series, other)
if flip:
    array_args = reversed(array_args)
    series_args = reversed(series_args)
expected = pd.Series(ufunc(*array_args), name=name)
result = ufunc(*series_args)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_ufunc.py:83 | Complexity: Advanced | Last updated: 2026-06-02*