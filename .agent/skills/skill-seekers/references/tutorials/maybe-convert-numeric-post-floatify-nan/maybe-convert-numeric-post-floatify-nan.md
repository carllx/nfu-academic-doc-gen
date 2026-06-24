# How To: Maybe Convert Numeric Post Floatify Nan

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test maybe convert numeric post floatify nan

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `collections`
- `collections.abc`
- `datetime`
- `decimal`
- `fractions`
- `io`
- `itertools`
- `numbers`
- `re`
- `sys`
- `typing`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas.compat.numpy`
- `pandas.core.dtypes`
- `pandas.core.dtypes.cast`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: coerce, convert_to_masked_nullable
```

## Step-by-Step Guide

### Step 1: Assign data = np.array(...)

```python
data = np.array(['1.200', '-999.000', '4.500'], dtype=object)
```

### Step 2: Assign expected = np.array(...)

```python
expected = np.array([1.2, np.nan, 4.5], dtype=np.float64)
```

### Step 3: Assign nan_values = value

```python
nan_values = {-999, -999.0}
```

### Step 4: Assign out = lib.maybe_convert_numeric(...)

```python
out = lib.maybe_convert_numeric(data, nan_values, coerce, convert_to_masked_nullable=convert_to_masked_nullable)
```

### Step 5: Assign expected = FloatingArray(...)

```python
expected = FloatingArray(expected, np.isnan(expected))
```

### Step 6: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(expected, FloatingArray(*out))
```

### Step 7: Assign out = value

```python
out = out[0]
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(out, expected)
```


## Complete Example

```python
# Setup
# Fixtures: coerce, convert_to_masked_nullable

# Workflow
data = np.array(['1.200', '-999.000', '4.500'], dtype=object)
expected = np.array([1.2, np.nan, 4.5], dtype=np.float64)
nan_values = {-999, -999.0}
out = lib.maybe_convert_numeric(data, nan_values, coerce, convert_to_masked_nullable=convert_to_masked_nullable)
if convert_to_masked_nullable:
    expected = FloatingArray(expected, np.isnan(expected))
    tm.assert_extension_array_equal(expected, FloatingArray(*out))
else:
    out = out[0]
    tm.assert_numpy_array_equal(out, expected)
```

## Next Steps


---

*Source: test_inference.py:582 | Complexity: Advanced | Last updated: 2026-06-02*