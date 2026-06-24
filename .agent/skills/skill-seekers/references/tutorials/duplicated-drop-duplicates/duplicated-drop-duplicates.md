# How To: Duplicated Drop Duplicates

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test duplicated drop duplicates

## Prerequisites

**Required Modules:**
- `itertools`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = MultiIndex.from_arrays(...)

```python
idx = MultiIndex.from_arrays(([1, 2, 3, 1, 2, 3], [1, 1, 1, 1, 2, 2]))
```

**Verification:**
```python
assert duplicated.dtype == bool
```

### Step 2: Assign expected = np.array(...)

```python
expected = np.array([False, False, False, True, False, False], dtype=bool)
```

**Verification:**
```python
assert duplicated.dtype == bool
```

### Step 3: Assign duplicated = idx.duplicated(...)

```python
duplicated = idx.duplicated()
```

**Verification:**
```python
assert duplicated.dtype == bool
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(duplicated, expected)
```

**Verification:**
```python
assert duplicated.dtype == bool
```

### Step 5: Assign expected = MultiIndex.from_arrays(...)

```python
expected = MultiIndex.from_arrays(([1, 2, 3, 2, 3], [1, 1, 1, 2, 2]))
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.drop_duplicates(), expected)
```

### Step 7: Assign expected = np.array(...)

```python
expected = np.array([True, False, False, False, False, False])
```

### Step 8: Assign duplicated = idx.duplicated(...)

```python
duplicated = idx.duplicated(keep='last')
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(duplicated, expected)
```

**Verification:**
```python
assert duplicated.dtype == bool
```

### Step 10: Assign expected = MultiIndex.from_arrays(...)

```python
expected = MultiIndex.from_arrays(([2, 3, 1, 2, 3], [1, 1, 1, 2, 2]))
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.drop_duplicates(keep='last'), expected)
```

### Step 12: Assign expected = np.array(...)

```python
expected = np.array([True, False, False, True, False, False])
```

### Step 13: Assign duplicated = idx.duplicated(...)

```python
duplicated = idx.duplicated(keep=False)
```

### Step 14: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(duplicated, expected)
```

**Verification:**
```python
assert duplicated.dtype == bool
```

### Step 15: Assign expected = MultiIndex.from_arrays(...)

```python
expected = MultiIndex.from_arrays(([2, 3, 2, 3], [1, 1, 2, 2]))
```

### Step 16: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.drop_duplicates(keep=False), expected)
```


## Complete Example

```python
# Workflow
idx = MultiIndex.from_arrays(([1, 2, 3, 1, 2, 3], [1, 1, 1, 1, 2, 2]))
expected = np.array([False, False, False, True, False, False], dtype=bool)
duplicated = idx.duplicated()
tm.assert_numpy_array_equal(duplicated, expected)
assert duplicated.dtype == bool
expected = MultiIndex.from_arrays(([1, 2, 3, 2, 3], [1, 1, 1, 2, 2]))
tm.assert_index_equal(idx.drop_duplicates(), expected)
expected = np.array([True, False, False, False, False, False])
duplicated = idx.duplicated(keep='last')
tm.assert_numpy_array_equal(duplicated, expected)
assert duplicated.dtype == bool
expected = MultiIndex.from_arrays(([2, 3, 1, 2, 3], [1, 1, 1, 2, 2]))
tm.assert_index_equal(idx.drop_duplicates(keep='last'), expected)
expected = np.array([True, False, False, True, False, False])
duplicated = idx.duplicated(keep=False)
tm.assert_numpy_array_equal(duplicated, expected)
assert duplicated.dtype == bool
expected = MultiIndex.from_arrays(([2, 3, 2, 3], [1, 1, 2, 2]))
tm.assert_index_equal(idx.drop_duplicates(keep=False), expected)
```

## Next Steps


---

*Source: test_duplicates.py:296 | Complexity: Advanced | Last updated: 2026-06-02*