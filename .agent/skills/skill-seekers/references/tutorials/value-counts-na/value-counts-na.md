# How To: Value Counts Na

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test value counts na

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arr = pd.array(...)

```python
arr = pd.array([0.1, 0.2, 0.1, pd.NA], dtype='Float64')
```

**Verification:**
```python
assert idx.dtype == arr.dtype
```

### Step 2: Assign result = arr.value_counts(...)

```python
result = arr.value_counts(dropna=False)
```

### Step 3: Assign idx = pd.Index(...)

```python
idx = pd.Index([0.1, 0.2, pd.NA], dtype=arr.dtype)
```

**Verification:**
```python
assert idx.dtype == arr.dtype
```

### Step 4: Assign expected = pd.Series(...)

```python
expected = pd.Series([2, 1, 1], index=idx, dtype='Int64', name='count')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign result = arr.value_counts(...)

```python
result = arr.value_counts(dropna=True)
```

### Step 7: Assign expected = pd.Series(...)

```python
expected = pd.Series([2, 1], index=idx[:-1], dtype='Int64', name='count')
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
arr = pd.array([0.1, 0.2, 0.1, pd.NA], dtype='Float64')
result = arr.value_counts(dropna=False)
idx = pd.Index([0.1, 0.2, pd.NA], dtype=arr.dtype)
assert idx.dtype == arr.dtype
expected = pd.Series([2, 1, 1], index=idx, dtype='Int64', name='count')
tm.assert_series_equal(result, expected)
result = arr.value_counts(dropna=True)
expected = pd.Series([2, 1], index=idx[:-1], dtype='Int64', name='count')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_function.py:100 | Complexity: Advanced | Last updated: 2026-06-02*