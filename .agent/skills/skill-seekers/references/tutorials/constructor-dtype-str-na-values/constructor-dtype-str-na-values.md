# How To: Constructor Dtype Str Na Values

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test constructor dtype str na values

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `collections.abc`
- `datetime`
- `dateutil.tz`
- `numpy`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.internals.blocks`
- `numpy.dtypes`

**Setup Required:**
```python
# Fixtures: string_dtype
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(['x', None], dtype=string_dtype)
```

**Verification:**
```python
assert ser.iloc[1] is None
```

### Step 2: Assign result = ser.isna(...)

```python
result = ser.isna()
```

**Verification:**
```python
assert np.isnan(ser.iloc[1])
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([False, True])
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

**Verification:**
```python
assert ser.iloc[1] is None
```

### Step 5: Assign ser = Series(...)

```python
ser = Series(['x', np.nan], dtype=string_dtype)
```

**Verification:**
```python
assert np.isnan(ser.iloc[1])
```


## Complete Example

```python
# Setup
# Fixtures: string_dtype

# Workflow
ser = Series(['x', None], dtype=string_dtype)
result = ser.isna()
expected = Series([False, True])
tm.assert_series_equal(result, expected)
assert ser.iloc[1] is None
ser = Series(['x', np.nan], dtype=string_dtype)
assert np.isnan(ser.iloc[1])
```

## Next Steps


---

*Source: test_constructors.py:271 | Complexity: Intermediate | Last updated: 2026-06-02*