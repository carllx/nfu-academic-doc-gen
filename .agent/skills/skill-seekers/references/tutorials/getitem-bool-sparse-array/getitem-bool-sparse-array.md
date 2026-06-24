# How To: Getitem Bool Sparse Array

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem bool sparse array

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
# Fixtures: arr
```

## Step-by-Step Guide

### Step 1: Assign spar_bool = SparseArray(...)

```python
spar_bool = SparseArray([False, True] * 5, dtype=np.bool_, fill_value=True)
```

### Step 2: Assign exp = SparseArray(...)

```python
exp = SparseArray([np.nan, 2, np.nan, 5, 6])
```

### Step 3: Call tm.assert_sp_array_equal()

```python
tm.assert_sp_array_equal(arr[spar_bool], exp)
```

### Step 4: Assign spar_bool = value

```python
spar_bool = ~spar_bool
```

### Step 5: Assign res = value

```python
res = arr[spar_bool]
```

### Step 6: Assign exp = SparseArray(...)

```python
exp = SparseArray([np.nan, 1, 3, 4, np.nan])
```

### Step 7: Call tm.assert_sp_array_equal()

```python
tm.assert_sp_array_equal(res, exp)
```

### Step 8: Assign spar_bool = SparseArray(...)

```python
spar_bool = SparseArray([False, True, np.nan] * 3, dtype=np.bool_, fill_value=np.nan)
```

### Step 9: Assign res = value

```python
res = arr[spar_bool]
```

### Step 10: Assign exp = SparseArray(...)

```python
exp = SparseArray([np.nan, 3, 5])
```

### Step 11: Call tm.assert_sp_array_equal()

```python
tm.assert_sp_array_equal(res, exp)
```


## Complete Example

```python
# Setup
# Fixtures: arr

# Workflow
spar_bool = SparseArray([False, True] * 5, dtype=np.bool_, fill_value=True)
exp = SparseArray([np.nan, 2, np.nan, 5, 6])
tm.assert_sp_array_equal(arr[spar_bool], exp)
spar_bool = ~spar_bool
res = arr[spar_bool]
exp = SparseArray([np.nan, 1, 3, 4, np.nan])
tm.assert_sp_array_equal(res, exp)
spar_bool = SparseArray([False, True, np.nan] * 3, dtype=np.bool_, fill_value=np.nan)
res = arr[spar_bool]
exp = SparseArray([np.nan, 3, 5])
tm.assert_sp_array_equal(res, exp)
```

## Next Steps


---

*Source: test_indexing.py:91 | Complexity: Advanced | Last updated: 2026-06-02*