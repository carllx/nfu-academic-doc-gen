# How To: Value Counts Masked

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test value counts masked

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dtype = 'Int64'

```python
dtype = 'Int64'
```

### Step 2: Assign ser = Series(...)

```python
ser = Series([1, 2, None, 2, None, 3], dtype=dtype)
```

### Step 3: Assign result = ser.value_counts(...)

```python
result = ser.value_counts(dropna=False)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([2, 2, 1, 1], index=Index([2, None, 1, 3], dtype=dtype), dtype=dtype, name='count')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign result = ser.value_counts(...)

```python
result = ser.value_counts(dropna=True)
```

### Step 7: Assign expected = Series(...)

```python
expected = Series([2, 1, 1], index=Index([2, 1, 3], dtype=dtype), dtype=dtype, name='count')
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
dtype = 'Int64'
ser = Series([1, 2, None, 2, None, 3], dtype=dtype)
result = ser.value_counts(dropna=False)
expected = Series([2, 2, 1, 1], index=Index([2, None, 1, 3], dtype=dtype), dtype=dtype, name='count')
tm.assert_series_equal(result, expected)
result = ser.value_counts(dropna=True)
expected = Series([2, 1, 1], index=Index([2, 1, 3], dtype=dtype), dtype=dtype, name='count')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_value_counts.py:254 | Complexity: Advanced | Last updated: 2026-06-02*