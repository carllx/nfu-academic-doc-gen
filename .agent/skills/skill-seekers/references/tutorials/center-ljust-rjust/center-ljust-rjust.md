# How To: Center Ljust Rjust

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test center ljust rjust

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas`

**Setup Required:**
```python
# Fixtures: any_string_dtype
```

## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series(['a', 'b', np.nan, 'c', np.nan, 'eeeeee'], dtype=any_string_dtype)
```

### Step 2: Assign result = s.str.center(...)

```python
result = s.str.center(5)
```

### Step 3: Assign expected = Series(...)

```python
expected = Series(['  a  ', '  b  ', np.nan, '  c  ', np.nan, 'eeeeee'], dtype=any_string_dtype)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = s.str.ljust(...)

```python
result = s.str.ljust(5)
```

### Step 6: Assign expected = Series(...)

```python
expected = Series(['a    ', 'b    ', np.nan, 'c    ', np.nan, 'eeeeee'], dtype=any_string_dtype)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign result = s.str.rjust(...)

```python
result = s.str.rjust(5)
```

### Step 9: Assign expected = Series(...)

```python
expected = Series(['    a', '    b', np.nan, '    c', np.nan, 'eeeeee'], dtype=any_string_dtype)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: any_string_dtype

# Workflow
s = Series(['a', 'b', np.nan, 'c', np.nan, 'eeeeee'], dtype=any_string_dtype)
result = s.str.center(5)
expected = Series(['  a  ', '  b  ', np.nan, '  c  ', np.nan, 'eeeeee'], dtype=any_string_dtype)
tm.assert_series_equal(result, expected)
result = s.str.ljust(5)
expected = Series(['a    ', 'b    ', np.nan, 'c    ', np.nan, 'eeeeee'], dtype=any_string_dtype)
tm.assert_series_equal(result, expected)
result = s.str.rjust(5)
expected = Series(['    a', '    b', np.nan, '    c', np.nan, 'eeeeee'], dtype=any_string_dtype)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_case_justify.py:213 | Complexity: Advanced | Last updated: 2026-06-02*