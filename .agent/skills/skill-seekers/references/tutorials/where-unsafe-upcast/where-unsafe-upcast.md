# How To: Where Unsafe Upcast

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test where unsafe upcast

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
# Fixtures: dtype, expected_dtype
```

## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(np.arange(10), dtype=dtype)
```

### Step 2: Assign values = value

```python
values = [2.5, 3.5, 4.5, 5.5, 6.5]
```

### Step 3: Assign mask = value

```python
mask = s < 5
```

### Step 4: Assign expected = Series(...)

```python
expected = Series(values + list(range(5, 10)), dtype=expected_dtype)
```

### Step 5: Assign warn = value

```python
warn = None if np.dtype(dtype).kind == np.dtype(expected_dtype).kind == 'f' else FutureWarning
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s, expected)
```

### Step 7: Assign unknown = values

```python
s[mask] = values
```


## Complete Example

```python
# Setup
# Fixtures: dtype, expected_dtype

# Workflow
s = Series(np.arange(10), dtype=dtype)
values = [2.5, 3.5, 4.5, 5.5, 6.5]
mask = s < 5
expected = Series(values + list(range(5, 10)), dtype=expected_dtype)
warn = None if np.dtype(dtype).kind == np.dtype(expected_dtype).kind == 'f' else FutureWarning
with tm.assert_produces_warning(warn, match='incompatible dtype'):
    s[mask] = values
tm.assert_series_equal(s, expected)
```

## Next Steps


---

*Source: test_where.py:51 | Complexity: Intermediate | Last updated: 2026-06-02*