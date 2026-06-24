# How To: Map Keeps Dtype

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test map keeps dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: na_action
```

## Step-by-Step Guide

### Step 1: Assign arr = Series(...)

```python
arr = Series(['a', np.nan, 'b'])
```

### Step 2: Assign sparse_arr = arr.astype(...)

```python
sparse_arr = arr.astype(pd.SparseDtype(object))
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(data={'a': arr, 'b': sparse_arr})
```

### Step 4: Assign result = df.map(...)

```python
result = df.map(func, na_action=na_action)
```

### Step 5: Assign expected_sparse = pd.array(...)

```python
expected_sparse = pd.array(['A', np.nan, 'B'], dtype=pd.SparseDtype(object))
```

### Step 6: Assign expected_arr = expected_sparse.astype(...)

```python
expected_arr = expected_sparse.astype(object)
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': expected_arr, 'b': expected_sparse})
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign result_empty = unknown.map(...)

```python
result_empty = df.iloc[:0, :].map(func, na_action=na_action)
```

### Step 10: Assign expected_empty = value

```python
expected_empty = expected.iloc[:0, :]
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result_empty, expected_empty)
```


## Complete Example

```python
# Setup
# Fixtures: na_action

# Workflow
arr = Series(['a', np.nan, 'b'])
sparse_arr = arr.astype(pd.SparseDtype(object))
df = DataFrame(data={'a': arr, 'b': sparse_arr})

def func(x):
    return str.upper(x) if not pd.isna(x) else x
result = df.map(func, na_action=na_action)
expected_sparse = pd.array(['A', np.nan, 'B'], dtype=pd.SparseDtype(object))
expected_arr = expected_sparse.astype(object)
expected = DataFrame({'a': expected_arr, 'b': expected_sparse})
tm.assert_frame_equal(result, expected)
result_empty = df.iloc[:0, :].map(func, na_action=na_action)
expected_empty = expected.iloc[:0, :]
tm.assert_frame_equal(result_empty, expected_empty)
```

## Next Steps


---

*Source: test_map.py:37 | Complexity: Advanced | Last updated: 2026-06-02*