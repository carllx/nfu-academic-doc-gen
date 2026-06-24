# How To: Floordiv By Int Zero No Mask

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test floordiv by int zero no mask

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: any_int_ea_dtype
```

## Step-by-Step Guide

### Step 1: Assign ser = pd.Series(...)

```python
ser = pd.Series([0, 1], dtype=any_int_ea_dtype)
```

### Step 2: Assign result = value

```python
result = 1 // ser
```

### Step 3: Assign expected = pd.Series(...)

```python
expected = pd.Series([np.inf, 1.0], dtype='Float64')
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign ser_non_nullable = ser.astype(...)

```python
ser_non_nullable = ser.astype(ser.dtype.numpy_dtype)
```

### Step 6: Assign result = value

```python
result = 1 // ser_non_nullable
```

### Step 7: Assign expected = expected.astype(...)

```python
expected = expected.astype(np.float64)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: any_int_ea_dtype

# Workflow
ser = pd.Series([0, 1], dtype=any_int_ea_dtype)
result = 1 // ser
expected = pd.Series([np.inf, 1.0], dtype='Float64')
tm.assert_series_equal(result, expected)
ser_non_nullable = ser.astype(ser.dtype.numpy_dtype)
result = 1 // ser_non_nullable
expected = expected.astype(np.float64)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_arithmetic.py:78 | Complexity: Advanced | Last updated: 2026-06-02*