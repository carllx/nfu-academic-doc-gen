# How To: Array Tz

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test array tz

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
assert result.base is expected.base
```

### Step 2: Assign dti = self.index_cls(...)

```python
dti = self.index_cls(arr1d)
```

**Verification:**
```python
assert result.base is not None
```

### Step 3: Assign copy_false = value

```python
copy_false = None if np_version_gt2 else False
```

**Verification:**
```python
assert result.base is expected.base
```

### Step 4: Assign expected = dti.asi8.view(...)

```python
expected = dti.asi8.view('M8[ns]')
```

**Verification:**
```python
assert result.base is not None
```

### Step 5: Assign result = np.array(...)

```python
result = np.array(arr, dtype='M8[ns]')
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 7: Assign result = np.array(...)

```python
result = np.array(arr, dtype='datetime64[ns]')
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```

### Step 9: Assign result = np.array(...)

```python
result = np.array(arr, dtype='M8[ns]', copy=copy_false)
```

**Verification:**
```python
assert result.base is expected.base
```

### Step 10: Assign result = np.array(...)

```python
result = np.array(arr, dtype='datetime64[ns]', copy=copy_false)
```

**Verification:**
```python
assert result.base is expected.base
```


## Complete Example

```python
# Workflow
arr = arr1d
dti = self.index_cls(arr1d)
copy_false = None if np_version_gt2 else False
expected = dti.asi8.view('M8[ns]')
result = np.array(arr, dtype='M8[ns]')
tm.assert_numpy_array_equal(result, expected)
result = np.array(arr, dtype='datetime64[ns]')
tm.assert_numpy_array_equal(result, expected)
result = np.array(arr, dtype='M8[ns]', copy=copy_false)
assert result.base is expected.base
assert result.base is not None
result = np.array(arr, dtype='datetime64[ns]', copy=copy_false)
assert result.base is expected.base
assert result.base is not None
```

## Next Steps


---

*Source: test_datetimelike.py:699 | Complexity: Advanced | Last updated: 2026-06-02*