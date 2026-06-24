# How To: Setitem Numeric Should Not Fallback To Positional

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test setitem numeric should not fallback to positional

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

### Step 4: Assign unknown = 10

```python
ser[1] = 10
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([10, 1, 10], index=idx)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, expected, check_exact=True)
```


## Complete Example

```python
# Setup
# Fixtures: any_numeric_dtype

# Workflow
dtype = any_numeric_dtype
idx = Index([1, 0, 1], dtype=dtype)
ser = Series(range(3), index=idx)
ser[1] = 10
expected = Series([10, 1, 10], index=idx)
tm.assert_series_equal(ser, expected, check_exact=True)
```

## Next Steps


---

*Source: test_indexing.py:68 | Complexity: Intermediate | Last updated: 2026-06-02*