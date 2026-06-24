# How To: Index Missing

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test index missing

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `pathlib`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.core.strings.accessor`
- `pandas.tests.strings`

**Setup Required:**
```python
# Fixtures: any_string_dtype, method, exp
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(['abcb', 'ab', 'bcbe', np.nan], dtype=any_string_dtype)
```

### Step 2: Assign expected_dtype = value

```python
expected_dtype = np.float64 if is_object_or_nan_string_dtype(any_string_dtype) else 'Int64'
```

### Step 3: Assign result = getattr(...)

```python
result = getattr(ser.str, method)('b')
```

### Step 4: Assign expected = Series(...)

```python
expected = Series(exp + [np.nan], dtype=expected_dtype)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: any_string_dtype, method, exp

# Workflow
ser = Series(['abcb', 'ab', 'bcbe', np.nan], dtype=any_string_dtype)
expected_dtype = np.float64 if is_object_or_nan_string_dtype(any_string_dtype) else 'Int64'
result = getattr(ser.str, method)('b')
expected = Series(exp + [np.nan], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_strings.py:408 | Complexity: Intermediate | Last updated: 2026-06-02*