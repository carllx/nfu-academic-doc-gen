# How To: Getitem Numeric Should Not Fallback To Positional

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getitem numeric should not fallback to positional

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: any_numeric_dtype
```

## Step-by-Step Guide

### Step 1: Assign dtype = any_numeric_dtype

```python
dtype = any_numeric_dtype
```

### Step 2: Assign idx = Index(...)

```python
idx = Index([1, 0, 1], dtype=dtype)
```

### Step 3: Assign ser = Series(...)

```python
ser = Series(range(3), index=idx)
```

### Step 4: Assign result = value

```python
result = ser[1]
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([0, 2], index=Index([1, 1], dtype=dtype))
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected, check_exact=True)
```


## Complete Example

```python
# Setup
# Fixtures: any_numeric_dtype

# Workflow
dtype = any_numeric_dtype
idx = Index([1, 0, 1], dtype=dtype)
ser = Series(range(3), index=idx)
result = ser[1]
expected = Series([0, 2], index=Index([1, 1], dtype=dtype))
tm.assert_series_equal(result, expected, check_exact=True)
```

## Next Steps


---

*Source: test_indexing.py:58 | Complexity: Intermediate | Last updated: 2026-06-02*