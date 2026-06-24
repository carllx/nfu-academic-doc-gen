# How To: Convert Numeric Uint64 Nan Values

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test convert numeric uint64 nan values

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

### Step 1: Assign arr = np.array(...)

```python
arr = np.array([2 ** 63, 2 ** 63 + 1], dtype=object)
```

### Step 2: Assign na_values = value

```python
na_values = {2 ** 63}
```

### Step 3: Assign expected = value

```python
expected = np.array([np.nan, 2 ** 63 + 1], dtype=float) if coerce else arr.copy()
```

### Step 4: Assign result = lib.maybe_convert_numeric(...)

```python
result = lib.maybe_convert_numeric(arr, na_values, coerce_numeric=coerce, convert_to_masked_nullable=convert_to_masked_nullable)
```

### Step 5: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```

### Step 6: Assign expected = IntegerArray(...)

```python
expected = IntegerArray(np.array([0, 2 ** 63 + 1], dtype='u8'), np.array([True, False], dtype='bool'))
```

### Step 7: Assign result = IntegerArray(...)

```python
result = IntegerArray(*result)
```

### Step 8: Assign result = value

```python
result = result[0]
```


## Complete Example

```python
# Setup
# Fixtures: coerce, convert_to_masked_nullable

# Workflow
arr = np.array([2 ** 63, 2 ** 63 + 1], dtype=object)
na_values = {2 ** 63}
expected = np.array([np.nan, 2 ** 63 + 1], dtype=float) if coerce else arr.copy()
result = lib.maybe_convert_numeric(arr, na_values, coerce_numeric=coerce, convert_to_masked_nullable=convert_to_masked_nullable)
if convert_to_masked_nullable and coerce:
    expected = IntegerArray(np.array([0, 2 ** 63 + 1], dtype='u8'), np.array([True, False], dtype='bool'))
    result = IntegerArray(*result)
else:
    result = result[0]
tm.assert_almost_equal(result, expected)
```

## Next Steps


---

*Source: test_inference.py:653 | Complexity: Advanced | Last updated: 2026-06-02*