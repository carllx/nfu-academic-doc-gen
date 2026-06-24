# How To: Assert Extension Array Equal Less Precise

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test assert extension array equal less precise

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
# Fixtures: decimals
```

## Step-by-Step Guide

### Step 1: Assign rtol = value

```python
rtol = 0.5 * 10 ** (-decimals)
```

### Step 2: Assign arr1 = SparseArray(...)

```python
arr1 = SparseArray([0.5, 0.123456])
```

### Step 3: Assign arr2 = SparseArray(...)

```python
arr2 = SparseArray([0.5, 0.123457])
```

### Step 4: Assign msg = 'ExtensionArray are different\n\nExtensionArray values are different \\(50\\.0 %\\)\n\\[left\\]:  \\[0\\.5, 0\\.123456\\]\n\\[right\\]: \\[0\\.5, 0\\.123457\\]'

```python
msg = 'ExtensionArray are different\n\nExtensionArray values are different \\(50\\.0 %\\)\n\\[left\\]:  \\[0\\.5, 0\\.123456\\]\n\\[right\\]: \\[0\\.5, 0\\.123457\\]'
```

### Step 5: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(arr1, arr2, rtol=rtol)
```

### Step 6: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(arr1, arr2, rtol=rtol)
```


## Complete Example

```python
# Setup
# Fixtures: decimals

# Workflow
rtol = 0.5 * 10 ** (-decimals)
arr1 = SparseArray([0.5, 0.123456])
arr2 = SparseArray([0.5, 0.123457])
if decimals >= 5:
    msg = 'ExtensionArray are different\n\nExtensionArray values are different \\(50\\.0 %\\)\n\\[left\\]:  \\[0\\.5, 0\\.123456\\]\n\\[right\\]: \\[0\\.5, 0\\.123457\\]'
    with pytest.raises(AssertionError, match=msg):
        tm.assert_extension_array_equal(arr1, arr2, rtol=rtol)
else:
    tm.assert_extension_array_equal(arr1, arr2, rtol=rtol)
```

## Next Steps


---

*Source: test_assert_extension_array_equal.py:40 | Complexity: Intermediate | Last updated: 2026-06-02*