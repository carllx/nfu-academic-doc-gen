# How To: Contains Compiled Regex Flags

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test contains compiled regex flags

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
ser = Series(['foobar', 'foo\nbar', 'Baz'], dtype=any_string_dtype)
```

### Step 3: Assign pat = re.compile(...)

```python
pat = re.compile('^ba')
```

### Step 4: Assign result = ser.str.contains(...)

```python
result = ser.str.contains(pat)
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([False, False, False], dtype=expected_dtype)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign pat = re.compile(...)

```python
pat = re.compile('^ba', flags=re.MULTILINE)
```

### Step 8: Assign result = ser.str.contains(...)

```python
result = ser.str.contains(pat)
```

### Step 9: Assign expected = Series(...)

```python
expected = Series([False, True, False], dtype=expected_dtype)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 11: Assign pat = re.compile(...)

```python
pat = re.compile('^ba', flags=re.MULTILINE | re.IGNORECASE)
```

### Step 12: Assign result = ser.str.contains(...)

```python
result = ser.str.contains(pat)
```

### Step 13: Assign expected = Series(...)

```python
expected = Series([False, True, True], dtype=expected_dtype)
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: any_string_dtype

# Workflow
expected_dtype = np.bool_ if is_object_or_nan_string_dtype(any_string_dtype) else 'boolean'
ser = Series(['foobar', 'foo\nbar', 'Baz'], dtype=any_string_dtype)
pat = re.compile('^ba')
result = ser.str.contains(pat)
expected = Series([False, False, False], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
pat = re.compile('^ba', flags=re.MULTILINE)
result = ser.str.contains(pat)
expected = Series([False, True, False], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
pat = re.compile('^ba', flags=re.MULTILINE | re.IGNORECASE)
result = ser.str.contains(pat)
expected = Series([False, True, True], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_find_replace.py:329 | Complexity: Advanced | Last updated: 2026-06-02*