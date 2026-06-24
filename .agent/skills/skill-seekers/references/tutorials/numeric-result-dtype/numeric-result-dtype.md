# How To: Numeric Result Dtype

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test numeric result dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: any_numeric_dtype
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([0, 1], dtype=any_numeric_dtype)
```

### Step 2: Assign result = ser.describe(...)

```python
result = ser.describe()
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([2.0, 0.5, ser.std(), 0, 0.25, 0.5, 0.75, 1.0], index=['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'], dtype=dtype)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign dtype = 'Float64'

```python
dtype = 'Float64'
```

### Step 6: Assign dtype = value

```python
dtype = 'complex128' if is_complex_dtype(any_numeric_dtype) else None
```

### Step 7: Call ser.describe()

```python
ser.describe()
```


## Complete Example

```python
# Setup
# Fixtures: any_numeric_dtype

# Workflow
if is_extension_array_dtype(any_numeric_dtype):
    dtype = 'Float64'
else:
    dtype = 'complex128' if is_complex_dtype(any_numeric_dtype) else None
ser = Series([0, 1], dtype=any_numeric_dtype)
if dtype == 'complex128' and np_version_gte1p25:
    with pytest.raises(TypeError, match='^a must be an array of real numbers$'):
        ser.describe()
    return
result = ser.describe()
expected = Series([2.0, 0.5, ser.std(), 0, 0.25, 0.5, 0.75, 1.0], index=['count', 'mean', 'std', 'min', '25%', '50%', '75%', 'max'], dtype=dtype)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_describe.py:162 | Complexity: Intermediate | Last updated: 2026-06-02*