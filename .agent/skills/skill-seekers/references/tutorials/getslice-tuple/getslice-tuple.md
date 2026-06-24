# How To: Getslice Tuple

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getslice tuple

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`


## Step-by-Step Guide

### Step 1: Assign dense = np.array(...)

```python
dense = np.array([np.nan, 0, 3, 4, 0, 5, np.nan, np.nan, 0])
```

### Step 2: Assign sparse = SparseArray(...)

```python
sparse = SparseArray(dense)
```

### Step 3: Assign res = value

```python
res = sparse[slice(4, None),]
```

### Step 4: Assign exp = SparseArray(...)

```python
exp = SparseArray(dense[4:])
```

### Step 5: Call tm.assert_sp_array_equal()

```python
tm.assert_sp_array_equal(res, exp)
```

### Step 6: Assign sparse = SparseArray(...)

```python
sparse = SparseArray(dense, fill_value=0)
```

### Step 7: Assign res = value

```python
res = sparse[slice(4, None),]
```

### Step 8: Assign exp = SparseArray(...)

```python
exp = SparseArray(dense[4:], fill_value=0)
```

### Step 9: Call tm.assert_sp_array_equal()

```python
tm.assert_sp_array_equal(res, exp)
```

### Step 10: Assign msg = 'too many indices for array'

```python
msg = 'too many indices for array'
```

### Step 11: sparse[4:, :]

```python
sparse[4:, :]
```

### Step 12: dense[4:, :]

```python
dense[4:, :]
```


## Complete Example

```python
# Workflow
dense = np.array([np.nan, 0, 3, 4, 0, 5, np.nan, np.nan, 0])
sparse = SparseArray(dense)
res = sparse[slice(4, None),]
exp = SparseArray(dense[4:])
tm.assert_sp_array_equal(res, exp)
sparse = SparseArray(dense, fill_value=0)
res = sparse[slice(4, None),]
exp = SparseArray(dense[4:], fill_value=0)
tm.assert_sp_array_equal(res, exp)
msg = 'too many indices for array'
with pytest.raises(IndexError, match=msg):
    sparse[4:, :]
with pytest.raises(IndexError, match=msg):
    dense[4:, :]
```

## Next Steps


---

*Source: test_indexing.py:65 | Complexity: Advanced | Last updated: 2026-06-02*