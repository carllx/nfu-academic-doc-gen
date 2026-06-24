# How To: Startswith String Dtype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test startswith string dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas.tests.strings`

**Setup Required:**
```python
# Fixtures: any_string_dtype, na
```

## Step-by-Step Guide

### Step 1: Assign values = Series(...)

```python
values = Series(['om', None, 'foo_nom', 'nom', 'bar_foo', None, 'foo', 'regex', 'rege.'], dtype=any_string_dtype)
```

### Step 2: Assign result = values.str.startswith(...)

```python
result = values.str.startswith('foo', na=na)
```

### Step 3: Assign expected_dtype = value

```python
expected_dtype = (object if na is None else bool) if is_object_or_nan_string_dtype(any_string_dtype) else 'boolean'
```

### Step 4: Assign exp = Series(...)

```python
exp = Series([False, na, True, False, False, na, True, False, False], dtype=expected_dtype)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, exp)
```

### Step 6: Assign result = values.str.startswith(...)

```python
result = values.str.startswith('rege.', na=na)
```

### Step 7: Assign exp = Series(...)

```python
exp = Series([False, na, False, False, False, na, False, False, True], dtype=expected_dtype)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, exp)
```

### Step 9: Assign expected_dtype = bool

```python
expected_dtype = bool
```

### Step 10: Assign na = False

```python
na = False
```


## Complete Example

```python
# Setup
# Fixtures: any_string_dtype, na

# Workflow
values = Series(['om', None, 'foo_nom', 'nom', 'bar_foo', None, 'foo', 'regex', 'rege.'], dtype=any_string_dtype)
result = values.str.startswith('foo', na=na)
expected_dtype = (object if na is None else bool) if is_object_or_nan_string_dtype(any_string_dtype) else 'boolean'
if any_string_dtype == 'str':
    expected_dtype = bool
    if na is None:
        na = False
exp = Series([False, na, True, False, False, na, True, False, False], dtype=expected_dtype)
tm.assert_series_equal(result, exp)
result = values.str.startswith('rege.', na=na)
exp = Series([False, na, False, False, False, na, False, False, True], dtype=expected_dtype)
tm.assert_series_equal(result, exp)
```

## Next Steps


---

*Source: test_find_replace.py:417 | Complexity: Advanced | Last updated: 2026-06-02*