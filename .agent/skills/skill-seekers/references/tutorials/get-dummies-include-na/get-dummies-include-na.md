# How To: Get Dummies Include Na

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get dummies include na

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `unicodedata`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`
- `pyarrow`

**Setup Required:**
```python
# Fixtures: sparse, dtype
```

## Step-by-Step Guide

### Step 1: Assign s = value

```python
s = ['a', 'b', np.nan]
```

### Step 2: Assign res = get_dummies(...)

```python
res = get_dummies(s, sparse=sparse, dtype=dtype)
```

### Step 3: Assign exp = DataFrame(...)

```python
exp = DataFrame({'a': [1, 0, 0], 'b': [0, 1, 0]}, dtype=self.effective_dtype(dtype))
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, exp)
```

### Step 5: Assign res_na = get_dummies(...)

```python
res_na = get_dummies(s, dummy_na=True, sparse=sparse, dtype=dtype)
```

### Step 6: Assign exp_na = DataFrame(...)

```python
exp_na = DataFrame({np.nan: [0, 0, 1], 'a': [1, 0, 0], 'b': [0, 1, 0]}, dtype=self.effective_dtype(dtype))
```

### Step 7: Assign exp_na = exp_na.reindex(...)

```python
exp_na = exp_na.reindex(['a', 'b', np.nan], axis=1)
```

### Step 8: Assign exp_na.columns = value

```python
exp_na.columns = res_na.columns
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res_na, exp_na)
```

### Step 10: Assign res_just_na = get_dummies(...)

```python
res_just_na = get_dummies([np.nan], dummy_na=True, sparse=sparse, dtype=dtype)
```

### Step 11: Assign exp_just_na = DataFrame(...)

```python
exp_just_na = DataFrame(Series(1, index=[0]), columns=[np.nan], dtype=self.effective_dtype(dtype))
```

### Step 12: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res_just_na.values, exp_just_na.values)
```

### Step 13: Assign exp = exp.apply(...)

```python
exp = exp.apply(SparseArray, fill_value=False)
```

### Step 14: Assign exp = exp.apply(...)

```python
exp = exp.apply(SparseArray, fill_value=0.0)
```

### Step 15: Assign exp_na = exp_na.apply(...)

```python
exp_na = exp_na.apply(SparseArray, fill_value=False)
```

### Step 16: Assign exp_na = exp_na.apply(...)

```python
exp_na = exp_na.apply(SparseArray, fill_value=0.0)
```


## Complete Example

```python
# Setup
# Fixtures: sparse, dtype

# Workflow
s = ['a', 'b', np.nan]
res = get_dummies(s, sparse=sparse, dtype=dtype)
exp = DataFrame({'a': [1, 0, 0], 'b': [0, 1, 0]}, dtype=self.effective_dtype(dtype))
if sparse:
    if dtype.kind == 'b':
        exp = exp.apply(SparseArray, fill_value=False)
    else:
        exp = exp.apply(SparseArray, fill_value=0.0)
tm.assert_frame_equal(res, exp)
res_na = get_dummies(s, dummy_na=True, sparse=sparse, dtype=dtype)
exp_na = DataFrame({np.nan: [0, 0, 1], 'a': [1, 0, 0], 'b': [0, 1, 0]}, dtype=self.effective_dtype(dtype))
exp_na = exp_na.reindex(['a', 'b', np.nan], axis=1)
exp_na.columns = res_na.columns
if sparse:
    if dtype.kind == 'b':
        exp_na = exp_na.apply(SparseArray, fill_value=False)
    else:
        exp_na = exp_na.apply(SparseArray, fill_value=0.0)
tm.assert_frame_equal(res_na, exp_na)
res_just_na = get_dummies([np.nan], dummy_na=True, sparse=sparse, dtype=dtype)
exp_just_na = DataFrame(Series(1, index=[0]), columns=[np.nan], dtype=self.effective_dtype(dtype))
tm.assert_numpy_array_equal(res_just_na.values, exp_just_na.values)
```

## Next Steps


---

*Source: test_get_dummies.py:150 | Complexity: Advanced | Last updated: 2026-06-02*