# How To: Take Filling

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test take filling

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`


## Step-by-Step Guide

### Step 1: Assign sparse = SparseArray(...)

```python
sparse = SparseArray([np.nan, np.nan, 1, np.nan, 4])
```

### Step 2: Assign result = sparse.take(...)

```python
result = sparse.take(np.array([1, 0, -1]))
```

### Step 3: Assign expected = SparseArray(...)

```python
expected = SparseArray([np.nan, np.nan, 4])
```

### Step 4: Call tm.assert_sp_array_equal()

```python
tm.assert_sp_array_equal(result, expected)
```

### Step 5: Assign result = sparse.take(...)

```python
result = sparse.take(np.array([1, 0, -1]), allow_fill=True)
```

### Step 6: Assign expected = SparseArray(...)

```python
expected = SparseArray([np.nan, np.nan, np.nan])
```

### Step 7: Call tm.assert_sp_array_equal()

```python
tm.assert_sp_array_equal(result, expected)
```

### Step 8: Assign result = sparse.take(...)

```python
result = sparse.take(np.array([1, 0, -1]), allow_fill=False, fill_value=True)
```

### Step 9: Assign expected = SparseArray(...)

```python
expected = SparseArray([np.nan, np.nan, 4])
```

### Step 10: Call tm.assert_sp_array_equal()

```python
tm.assert_sp_array_equal(result, expected)
```

### Step 11: Assign msg = "Invalid value in 'indices'"

```python
msg = "Invalid value in 'indices'"
```

### Step 12: Assign msg = "out of bounds value in 'indices'"

```python
msg = "out of bounds value in 'indices'"
```

### Step 13: Call sparse.take()

```python
sparse.take(np.array([1, 0, -2]), allow_fill=True)
```

### Step 14: Call sparse.take()

```python
sparse.take(np.array([1, 0, -5]), allow_fill=True)
```

### Step 15: Call sparse.take()

```python
sparse.take(np.array([1, -6]))
```

### Step 16: Call sparse.take()

```python
sparse.take(np.array([1, 5]))
```

### Step 17: Call sparse.take()

```python
sparse.take(np.array([1, 5]), allow_fill=True)
```


## Complete Example

```python
# Workflow
sparse = SparseArray([np.nan, np.nan, 1, np.nan, 4])
result = sparse.take(np.array([1, 0, -1]))
expected = SparseArray([np.nan, np.nan, 4])
tm.assert_sp_array_equal(result, expected)
result = sparse.take(np.array([1, 0, -1]), allow_fill=True)
expected = SparseArray([np.nan, np.nan, np.nan])
tm.assert_sp_array_equal(result, expected)
result = sparse.take(np.array([1, 0, -1]), allow_fill=False, fill_value=True)
expected = SparseArray([np.nan, np.nan, 4])
tm.assert_sp_array_equal(result, expected)
msg = "Invalid value in 'indices'"
with pytest.raises(ValueError, match=msg):
    sparse.take(np.array([1, 0, -2]), allow_fill=True)
with pytest.raises(ValueError, match=msg):
    sparse.take(np.array([1, 0, -5]), allow_fill=True)
msg = "out of bounds value in 'indices'"
with pytest.raises(IndexError, match=msg):
    sparse.take(np.array([1, -6]))
with pytest.raises(IndexError, match=msg):
    sparse.take(np.array([1, 5]))
with pytest.raises(IndexError, match=msg):
    sparse.take(np.array([1, 5]), allow_fill=True)
```

## Next Steps


---

*Source: test_indexing.py:201 | Complexity: Advanced | Last updated: 2026-06-02*