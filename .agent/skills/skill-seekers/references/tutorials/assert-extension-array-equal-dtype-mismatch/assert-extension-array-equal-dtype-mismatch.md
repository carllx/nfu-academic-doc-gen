# How To: Assert Extension Array Equal Dtype Mismatch

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test assert extension array equal dtype mismatch

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`

**Setup Required:**
```python
# Fixtures: check_dtype
```

## Step-by-Step Guide

### Step 1: Assign end = 5

```python
end = 5
```

### Step 2: Assign kwargs = value

```python
kwargs = {'check_dtype': check_dtype}
```

### Step 3: Assign arr1 = SparseArray(...)

```python
arr1 = SparseArray(np.arange(end, dtype='int64'))
```

### Step 4: Assign arr2 = SparseArray(...)

```python
arr2 = SparseArray(np.arange(end, dtype='int32'))
```

### Step 5: Assign msg = 'ExtensionArray are different\n\nAttribute "dtype" are different\n\\[left\\]:  Sparse\\[int64, 0\\]\n\\[right\\]: Sparse\\[int32, 0\\]'

```python
msg = 'ExtensionArray are different\n\nAttribute "dtype" are different\n\\[left\\]:  Sparse\\[int64, 0\\]\n\\[right\\]: Sparse\\[int32, 0\\]'
```

### Step 6: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(arr1, arr2, **kwargs)
```

### Step 7: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(arr1, arr2, **kwargs)
```


## Complete Example

```python
# Setup
# Fixtures: check_dtype

# Workflow
end = 5
kwargs = {'check_dtype': check_dtype}
arr1 = SparseArray(np.arange(end, dtype='int64'))
arr2 = SparseArray(np.arange(end, dtype='int32'))
if check_dtype:
    msg = 'ExtensionArray are different\n\nAttribute "dtype" are different\n\\[left\\]:  Sparse\\[int64, 0\\]\n\\[right\\]: Sparse\\[int32, 0\\]'
    with pytest.raises(AssertionError, match=msg):
        tm.assert_extension_array_equal(arr1, arr2, **kwargs)
else:
    tm.assert_extension_array_equal(arr1, arr2, **kwargs)
```

## Next Steps


---

*Source: test_assert_extension_array_equal.py:59 | Complexity: Intermediate | Last updated: 2026-06-02*