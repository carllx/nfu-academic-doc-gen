# How To: Array I8 Dtype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test array i8 dtype

## Prerequisites

**Required Modules:**
- `__future__`
- `re`
- `warnings`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.tslibs.dtypes`
- `pandas.compat.numpy`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign arr = arr1d

```python
arr = arr1d
```

**Verification:**
```python
assert result.base is not expected.base
```

### Step 2: Assign dti = self.index_cls(...)

```python
dti = self.index_cls(arr1d)
```

**Verification:**
```python
assert result.base is None
```

### Step 3: Assign copy_false = value

```python
copy_false = None if np_version_gt2 else False
```

### Step 4: Assign expected = value

```python
expected = dti.asi8
```

### Step 5: Assign result = np.array(...)

```python
result = np.array(arr, dtype='i8')
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 7: Assign result = np.array(...)

```python
result = np.array(arr, dtype=np.int64)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 9: Assign result = np.array(...)

```python
result = np.array(arr, dtype='i8', copy=copy_false)
```

**Verification:**
```python
assert result.base is not expected.base
```


## Complete Example

```python
# Workflow
arr = arr1d
dti = self.index_cls(arr1d)
copy_false = None if np_version_gt2 else False
expected = dti.asi8
result = np.array(arr, dtype='i8')
tm.assert_numpy_array_equal(result, expected)
result = np.array(arr, dtype=np.int64)
tm.assert_numpy_array_equal(result, expected)
result = np.array(arr, dtype='i8', copy=copy_false)
assert result.base is not expected.base
assert result.base is None
```

## Next Steps


---

*Source: test_datetimelike.py:720 | Complexity: Advanced | Last updated: 2026-06-02*