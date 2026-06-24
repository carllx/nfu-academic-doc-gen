# How To: Where Unsafe Int

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test where unsafe int

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: any_signed_int_numpy_dtype
```

## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(np.arange(10), dtype=any_signed_int_numpy_dtype)
```

### Step 2: Assign mask = value

```python
mask = s < 5
```

### Step 3: Assign unknown = range(...)

```python
s[mask] = range(2, 7)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series(list(range(2, 7)) + list(range(5, 10)), dtype=any_signed_int_numpy_dtype)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s, expected)
```


## Complete Example

```python
# Setup
# Fixtures: any_signed_int_numpy_dtype

# Workflow
s = Series(np.arange(10), dtype=any_signed_int_numpy_dtype)
mask = s < 5
s[mask] = range(2, 7)
expected = Series(list(range(2, 7)) + list(range(5, 10)), dtype=any_signed_int_numpy_dtype)
tm.assert_series_equal(s, expected)
```

## Next Steps


---

*Source: test_where.py:16 | Complexity: Intermediate | Last updated: 2026-06-02*