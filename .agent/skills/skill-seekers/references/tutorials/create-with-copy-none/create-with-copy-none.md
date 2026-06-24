# How To: Create With Copy None

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test create with copy none

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `copy`
- `itertools`
- `os`
- `pickle`
- `string`
- `sys`
- `tempfile`
- `pytest`
- `numpy`
- `numpy._core.tests._natype`
- `numpy.dtypes`
- `numpy.testing`
- `numpy.lib._stride_tricks_impl`

**Setup Required:**
```python
# Fixtures: string_list
```

## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array(string_list, dtype=StringDType())
```

**Verification:**
```python
assert arr_copy.base is None
```

### Step 2: Assign arr_rev = np.array(...)

```python
arr_rev = np.array(string_list[::-1], dtype=StringDType())
```

**Verification:**
```python
assert arr_view is arr
```

### Step 3: Assign arr_copy = np.array(...)

```python
arr_copy = np.array(arr, copy=None, dtype=arr_rev.dtype)
```

### Step 4: Call np.testing.assert_array_equal()

```python
np.testing.assert_array_equal(arr, arr_copy)
```

**Verification:**
```python
assert arr_copy.base is None
```

### Step 5: Assign arr_view = np.array(...)

```python
arr_view = np.array(arr, copy=None, dtype=arr.dtype)
```

### Step 6: Call np.testing.assert_array_equal()

```python
np.testing.assert_array_equal(arr, arr)
```

### Step 7: Call np.testing.assert_array_equal()

```python
np.testing.assert_array_equal(arr_view[::-1], arr_rev)
```

**Verification:**
```python
assert arr_view is arr
```

### Step 8: Call np.array()

```python
np.array(arr, copy=False, dtype=arr_rev.dtype)
```


## Complete Example

```python
# Setup
# Fixtures: string_list

# Workflow
arr = np.array(string_list, dtype=StringDType())
arr_rev = np.array(string_list[::-1], dtype=StringDType())
arr_copy = np.array(arr, copy=None, dtype=arr_rev.dtype)
np.testing.assert_array_equal(arr, arr_copy)
assert arr_copy.base is None
with pytest.raises(ValueError, match='Unable to avoid copy'):
    np.array(arr, copy=False, dtype=arr_rev.dtype)
arr_view = np.array(arr, copy=None, dtype=arr.dtype)
np.testing.assert_array_equal(arr, arr)
np.testing.assert_array_equal(arr_view[::-1], arr_rev)
assert arr_view is arr
```

## Next Steps


---

*Source: test_stringdtype.py:606 | Complexity: Advanced | Last updated: 2026-06-02*