# How To: Mixed Object Comparison

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mixed object comparison

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `string`
- `typing`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.core.dtypes.base`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.arrays`
- `pandas.core.arrays.string_`
- `pandas.tests.arrays.string_.test_string`
- `pandas.tests.extension`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign ser = pd.Series(...)

```python
ser = pd.Series(['a', 'b'], dtype=dtype)
```

### Step 2: Assign mixed = pd.Series(...)

```python
mixed = pd.Series([1, 'b'], dtype=object)
```

### Step 3: Assign result = value

```python
result = ser == mixed
```

### Step 4: Assign expected = pd.Series(...)

```python
expected = pd.Series([False, True], dtype=bool)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign expected = expected.astype(...)

```python
expected = expected.astype('boolean')
```

### Step 7: Assign expected = expected.astype(...)

```python
expected = expected.astype('bool[pyarrow]')
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
ser = pd.Series(['a', 'b'], dtype=dtype)
mixed = pd.Series([1, 'b'], dtype=object)
result = ser == mixed
expected = pd.Series([False, True], dtype=bool)
if dtype.storage == 'python' and dtype.na_value is pd.NA:
    expected = expected.astype('boolean')
elif dtype.storage == 'pyarrow' and dtype.na_value is pd.NA:
    expected = expected.astype('bool[pyarrow]')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_string.py:280 | Complexity: Intermediate | Last updated: 2026-06-02*