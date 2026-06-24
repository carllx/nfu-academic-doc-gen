# How To: Assert Extension Array Equal Non Extension Array

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test assert extension array equal non extension array

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
# Fixtures: side
```

## Step-by-Step Guide

### Step 1: Assign numpy_array = np.arange(...)

```python
numpy_array = np.arange(5)
```

### Step 2: Assign extension_array = SparseArray(...)

```python
extension_array = SparseArray(numpy_array)
```

### Step 3: Assign msg = value

```python
msg = f'{side} is not an ExtensionArray'
```

### Step 4: Assign args = value

```python
args = (numpy_array, extension_array) if side == 'left' else (extension_array, numpy_array)
```

### Step 5: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(*args)
```


## Complete Example

```python
# Setup
# Fixtures: side

# Workflow
numpy_array = np.arange(5)
extension_array = SparseArray(numpy_array)
msg = f'{side} is not an ExtensionArray'
args = (numpy_array, extension_array) if side == 'left' else (extension_array, numpy_array)
with pytest.raises(AssertionError, match=msg):
    tm.assert_extension_array_equal(*args)
```

## Next Steps


---

*Source: test_assert_extension_array_equal.py:96 | Complexity: Intermediate | Last updated: 2026-06-02*