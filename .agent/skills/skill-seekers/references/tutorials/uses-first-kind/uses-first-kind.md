# How To: Uses First Kind

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test uses first kind

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
# Fixtures: kind
```

## Step-by-Step Guide

### Step 1: Assign other = value

```python
other = 'integer' if kind == 'block' else 'block'
```

**Verification:**
```python
assert result.kind == kind
```

### Step 2: Assign a = SparseArray(...)

```python
a = SparseArray([1, 0, 0, 2], kind=kind)
```

### Step 3: Assign b = SparseArray(...)

```python
b = SparseArray([1, 0, 2, 2], kind=other)
```

### Step 4: Assign result = SparseArray._concat_same_type(...)

```python
result = SparseArray._concat_same_type([a, b])
```

### Step 5: Assign expected = np.array(...)

```python
expected = np.array([1, 2, 1, 2, 2], dtype='int64')
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result.sp_values, expected)
```

**Verification:**
```python
assert result.kind == kind
```


## Complete Example

```python
# Setup
# Fixtures: kind

# Workflow
other = 'integer' if kind == 'block' else 'block'
a = SparseArray([1, 0, 0, 2], kind=kind)
b = SparseArray([1, 0, 2, 2], kind=other)
result = SparseArray._concat_same_type([a, b])
expected = np.array([1, 2, 1, 2, 2], dtype='int64')
tm.assert_numpy_array_equal(result.sp_values, expected)
assert result.kind == kind
```

## Next Steps


---

*Source: test_combine_concat.py:24 | Complexity: Intermediate | Last updated: 2026-06-02*