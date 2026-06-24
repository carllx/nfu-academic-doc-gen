# How To: Contains Moar

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test contains moar

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
s = Series(['A', 'B', 'C', 'Aaba', 'Baca', '', np.nan, 'CABA', 'dog', 'cat'], dtype=any_string_dtype)
```

### Step 2: Assign result = s.str.contains(...)

```python
result = s.str.contains('a')
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([False, False, False, True, True, False, na_value, False, False, True], dtype=expected_dtype)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = s.str.contains(...)

```python
result = s.str.contains('a', case=False)
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([True, False, False, True, True, False, na_value, True, False, True], dtype=expected_dtype)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign result = s.str.contains(...)

```python
result = s.str.contains('Aa')
```

### Step 9: Assign expected = Series(...)

```python
expected = Series([False, False, False, True, False, False, na_value, False, False, False], dtype=expected_dtype)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 11: Assign result = s.str.contains(...)

```python
result = s.str.contains('ba')
```

### Step 12: Assign expected = Series(...)

```python
expected = Series([False, False, False, True, False, False, na_value, False, False, False], dtype=expected_dtype)
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 14: Assign result = s.str.contains(...)

```python
result = s.str.contains('ba', case=False)
```

### Step 15: Assign expected = Series(...)

```python
expected = Series([False, False, False, True, True, False, na_value, True, False, False], dtype=expected_dtype)
```

### Step 16: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 17: Assign expected_dtype = bool

```python
expected_dtype = bool
```

### Step 18: Assign na_value = False

```python
na_value = False
```

### Step 19: Assign expected_dtype = value

```python
expected_dtype = 'object' if is_object_or_nan_string_dtype(any_string_dtype) else 'boolean'
```

### Step 20: Assign na_value = value

```python
na_value = np.nan
```


## Complete Example

```python
# Setup
# Fixtures: any_string_dtype

# Workflow
s = Series(['A', 'B', 'C', 'Aaba', 'Baca', '', np.nan, 'CABA', 'dog', 'cat'], dtype=any_string_dtype)
result = s.str.contains('a')
if any_string_dtype == 'str':
    expected_dtype = bool
    na_value = False
else:
    expected_dtype = 'object' if is_object_or_nan_string_dtype(any_string_dtype) else 'boolean'
    na_value = np.nan
expected = Series([False, False, False, True, True, False, na_value, False, False, True], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
result = s.str.contains('a', case=False)
expected = Series([True, False, False, True, True, False, na_value, True, False, True], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
result = s.str.contains('Aa')
expected = Series([False, False, False, True, False, False, na_value, False, False, False], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
result = s.str.contains('ba')
expected = Series([False, False, False, True, False, False, na_value, False, False, False], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
result = s.str.contains('ba', case=False)
expected = Series([False, False, False, True, True, False, na_value, True, False, False], dtype=expected_dtype)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_find_replace.py:191 | Complexity: Advanced | Last updated: 2026-06-02*