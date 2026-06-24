# How To: Union With Duplicate Index And Non Monotonic

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test union with duplicate index and non monotonic

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.core.dtypes.cast`
- `pandas`
- `pandas._testing`
- `pandas.api.types`

**Setup Required:**
```python
# Fixtures: any_dtype_for_small_pos_integer_indexes
```

## Step-by-Step Guide

### Step 1: Assign dtype = any_dtype_for_small_pos_integer_indexes

```python
dtype = any_dtype_for_small_pos_integer_indexes
```

### Step 2: Assign a = Index(...)

```python
a = Index([1, 0, 0], dtype=dtype)
```

### Step 3: Assign b = Index(...)

```python
b = Index([0, 1], dtype=dtype)
```

### Step 4: Assign expected = Index(...)

```python
expected = Index([0, 0, 1], dtype=dtype)
```

### Step 5: Assign result = a.union(...)

```python
result = a.union(b)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 7: Assign result = b.union(...)

```python
result = b.union(a)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: any_dtype_for_small_pos_integer_indexes

# Workflow
dtype = any_dtype_for_small_pos_integer_indexes
a = Index([1, 0, 0], dtype=dtype)
b = Index([0, 1], dtype=dtype)
expected = Index([0, 0, 1], dtype=dtype)
result = a.union(b)
tm.assert_index_equal(result, expected)
result = b.union(a)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_setops.py:592 | Complexity: Advanced | Last updated: 2026-06-02*