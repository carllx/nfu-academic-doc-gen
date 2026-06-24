# How To: Contains Nan

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test contains nan

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
# Fixtures: any_string_dtype
```

## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series([np.nan, np.nan, np.nan], dtype=any_string_dtype)
```

### Step 2: Assign result = s.str.contains(...)

```python
result = s.str.contains('foo', na=False)
```

### Step 3: Assign expected_dtype = value

```python
expected_dtype = np.bool_ if is_object_or_nan_string_dtype(any_string_dtype) else 'boolean'
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([False, False, False], dtype=expected_dtype)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign result = s.str.contains(...)

```python
result = s.str.contains('foo', na=True)
```

### Step 7: Assign expected = Series(...)

```python
expected = Series([True, True, True], dtype=expected_dtype)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 9: Assign result = s.str.contains(...)

```python
result = s.str.contains('foo')
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 11: Assign msg = "Allowing a non-bool 'na' in obj.str.contains is deprecated and will raise in a future version"

```python
msg = "Allowing a non-bool 'na' in obj.str.contains is deprecated and will raise in a future version"
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 13: Assign expected = Series(...)

```python
expected = Series([False, False, False], dtype=bool)
```

### Step 14: Assign expected_dtype = value

```python
expected_dtype = 'object' if is_object_or_nan_string_dtype(any_string_dtype) else 'boolean'
```

### Step 15: Assign expected = Series(...)

```python
expected = Series([np.nan, np.nan, np.nan], dtype=expected_dtype)
```

### Step 16: Assign result = s.str.contains(...)

```python
result = s.str.contains('foo', na='foo')
```

### Step 17: Assign expected = Series(...)

```python
expected = Series(['foo', 'foo', 'foo'], dtype=np.object_)
```

### Step 18: Assign expected = Series(...)

```python
expected = Series([True, True, True], dtype=np.bool_)
```

### Step 19: Assign expected = Series(...)

```python
expected = Series([True, True, True], dtype='boolean')
```


## Complete Example

```python
# Setup
# Fixtures: any_string_dtype

# Workflow
s = Series([np.nan, np.nan, np.nan], dtype=any_string_dtype)
result = s.str.contains('foo', na=False)
expected_dtype = np.bool_ if is_object_or_nan_string_dtype(any_string_dtype) else 'boolean'
expected = Series([False, False, False], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
result = s.str.contains('foo', na=True)
expected = Series([True, True, True], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
if not (hasattr(any_string_dtype, 'storage') and any_string_dtype.storage == 'python' and (any_string_dtype.na_value is np.nan)):
    msg = "Allowing a non-bool 'na' in obj.str.contains is deprecated and will raise in a future version"
    with tm.assert_produces_warning(FutureWarning, match=msg):
        result = s.str.contains('foo', na='foo')
    if any_string_dtype == 'object':
        expected = Series(['foo', 'foo', 'foo'], dtype=np.object_)
    elif any_string_dtype.na_value is np.nan:
        expected = Series([True, True, True], dtype=np.bool_)
    else:
        expected = Series([True, True, True], dtype='boolean')
    tm.assert_series_equal(result, expected)
result = s.str.contains('foo')
if any_string_dtype == 'str':
    expected = Series([False, False, False], dtype=bool)
else:
    expected_dtype = 'object' if is_object_or_nan_string_dtype(any_string_dtype) else 'boolean'
    expected = Series([np.nan, np.nan, np.nan], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_find_replace.py:243 | Complexity: Advanced | Last updated: 2026-06-02*