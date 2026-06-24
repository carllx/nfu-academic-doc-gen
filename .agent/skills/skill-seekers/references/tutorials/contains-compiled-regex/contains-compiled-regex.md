# How To: Contains Compiled Regex

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test contains compiled regex

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

### Step 1: Assign expected_dtype = value

```python
expected_dtype = np.bool_ if is_object_or_nan_string_dtype(any_string_dtype) else 'boolean'
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(['foo', 'bar', 'Baz'], dtype=any_string_dtype)
```

### Step 3: Assign pat = re.compile(...)

```python
pat = re.compile('ba.')
```

### Step 4: Assign result = ser.str.contains(...)

```python
result = ser.str.contains(pat)
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([False, True, False], dtype=expected_dtype)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign pat = re.compile(...)

```python
pat = re.compile('ba.', flags=re.IGNORECASE)
```

### Step 8: Assign result = ser.str.contains(...)

```python
result = ser.str.contains(pat)
```

### Step 9: Assign expected = Series(...)

```python
expected = Series([False, True, True], dtype=expected_dtype)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 11: Assign result = ser.str.contains(...)

```python
result = ser.str.contains(pat, case=False)
```

### Step 12: Assign expected = Series(...)

```python
expected = Series([False, True, True], dtype=expected_dtype)
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 14: Call ser.str.contains()

```python
ser.str.contains(pat, flags=re.IGNORECASE)
```

### Step 15: Call ser.str.contains()

```python
ser.str.contains(pat, case=False)
```


## Complete Example

```python
# Setup
# Fixtures: any_string_dtype

# Workflow
expected_dtype = np.bool_ if is_object_or_nan_string_dtype(any_string_dtype) else 'boolean'
ser = Series(['foo', 'bar', 'Baz'], dtype=any_string_dtype)
pat = re.compile('ba.')
result = ser.str.contains(pat)
expected = Series([False, True, False], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
if any_string_dtype == 'string' and any_string_dtype.storage == 'pyarrow':
    result = ser.str.contains(pat, case=False)
    expected = Series([False, True, True], dtype=expected_dtype)
    tm.assert_series_equal(result, expected)
else:
    with pytest.raises(ValueError, match='cannot process flags argument with a compiled pattern'):
        ser.str.contains(pat, case=False)
pat = re.compile('ba.', flags=re.IGNORECASE)
result = ser.str.contains(pat)
expected = Series([False, True, True], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
with pytest.raises(ValueError, match='cannot process flags argument with a compiled pattern'):
    ser.str.contains(pat, flags=re.IGNORECASE)
```

## Next Steps


---

*Source: test_find_replace.py:293 | Complexity: Advanced | Last updated: 2026-06-02*