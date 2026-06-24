# How To: Concat With Non Sparse

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test concat with non sparse

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
# Fixtures: other, expected_dtype
```

## Step-by-Step Guide

### Step 1: Assign s_sparse = pd.Series(...)

```python
s_sparse = pd.Series([1, 0, 2], dtype=pd.SparseDtype('int64', 0))
```

### Step 2: Assign result = pd.concat(...)

```python
result = pd.concat([s_sparse, other], ignore_index=True)
```

### Step 3: Assign expected = pd.Series.astype(...)

```python
expected = pd.Series(list(s_sparse) + list(other)).astype(expected_dtype)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = pd.concat(...)

```python
result = pd.concat([other, s_sparse], ignore_index=True)
```

### Step 6: Assign expected = pd.Series.astype(...)

```python
expected = pd.Series(list(other) + list(s_sparse)).astype(expected_dtype)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: other, expected_dtype

# Workflow
s_sparse = pd.Series([1, 0, 2], dtype=pd.SparseDtype('int64', 0))
result = pd.concat([s_sparse, other], ignore_index=True)
expected = pd.Series(list(s_sparse) + list(other)).astype(expected_dtype)
tm.assert_series_equal(result, expected)
result = pd.concat([other, s_sparse], ignore_index=True)
expected = pd.Series(list(other) + list(s_sparse)).astype(expected_dtype)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_combine_concat.py:52 | Complexity: Intermediate | Last updated: 2026-06-02*