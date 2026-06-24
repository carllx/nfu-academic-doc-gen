# How To: Where Unsafe Float

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test where unsafe float

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
# Fixtures: float_numpy_dtype
```

## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(np.arange(10), dtype=float_numpy_dtype)
```

### Step 2: Assign mask = value

```python
mask = s < 5
```

### Step 3: Assign unknown = range(...)

```python
s[mask] = range(2, 7)
```

### Step 4: Assign data = value

```python
data = list(range(2, 7)) + list(range(5, 10))
```

### Step 5: Assign expected = Series(...)

```python
expected = Series(data, dtype=float_numpy_dtype)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s, expected)
```


## Complete Example

```python
# Setup
# Fixtures: float_numpy_dtype

# Workflow
s = Series(np.arange(10), dtype=float_numpy_dtype)
mask = s < 5
s[mask] = range(2, 7)
data = list(range(2, 7)) + list(range(5, 10))
expected = Series(data, dtype=float_numpy_dtype)
tm.assert_series_equal(s, expected)
```

## Next Steps


---

*Source: test_where.py:29 | Complexity: Intermediate | Last updated: 2026-06-02*