# How To: Take Filling All Nan

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test take filling all nan

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`

**Setup Required:**
```python
# Fixtures: kind
```

## Step-by-Step Guide

### Step 1: Assign sparse = SparseArray(...)

```python
sparse = SparseArray([np.nan, np.nan, np.nan, np.nan, np.nan], kind=kind)
```

### Step 2: Assign result = sparse.take(...)

```python
result = sparse.take(np.array([1, 0, -1]))
```

### Step 3: Assign expected = SparseArray(...)

```python
expected = SparseArray([np.nan, np.nan, np.nan], kind=kind)
```

### Step 4: Call tm.assert_sp_array_equal()

```python
tm.assert_sp_array_equal(result, expected)
```

### Step 5: Assign result = sparse.take(...)

```python
result = sparse.take(np.array([1, 0, -1]), fill_value=True)
```

### Step 6: Assign expected = SparseArray(...)

```python
expected = SparseArray([np.nan, np.nan, np.nan], kind=kind)
```

### Step 7: Call tm.assert_sp_array_equal()

```python
tm.assert_sp_array_equal(result, expected)
```

### Step 8: Assign msg = "out of bounds value in 'indices'"

```python
msg = "out of bounds value in 'indices'"
```

### Step 9: Call sparse.take()

```python
sparse.take(np.array([1, -6]))
```

### Step 10: Call sparse.take()

```python
sparse.take(np.array([1, 5]))
```

### Step 11: Call sparse.take()

```python
sparse.take(np.array([1, 5]), fill_value=True)
```


## Complete Example

```python
# Setup
# Fixtures: kind

# Workflow
sparse = SparseArray([np.nan, np.nan, np.nan, np.nan, np.nan], kind=kind)
result = sparse.take(np.array([1, 0, -1]))
expected = SparseArray([np.nan, np.nan, np.nan], kind=kind)
tm.assert_sp_array_equal(result, expected)
result = sparse.take(np.array([1, 0, -1]), fill_value=True)
expected = SparseArray([np.nan, np.nan, np.nan], kind=kind)
tm.assert_sp_array_equal(result, expected)
msg = "out of bounds value in 'indices'"
with pytest.raises(IndexError, match=msg):
    sparse.take(np.array([1, -6]))
with pytest.raises(IndexError, match=msg):
    sparse.take(np.array([1, 5]))
with pytest.raises(IndexError, match=msg):
    sparse.take(np.array([1, 5]), fill_value=True)
```

## Next Steps


---

*Source: test_indexing.py:270 | Complexity: Advanced | Last updated: 2026-06-02*