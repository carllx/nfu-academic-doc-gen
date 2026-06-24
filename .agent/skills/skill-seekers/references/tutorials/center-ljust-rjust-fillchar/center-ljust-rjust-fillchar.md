# How To: Center Ljust Rjust Fillchar

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test center ljust rjust fillchar

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
s = Series(['a', 'bb', 'cccc', 'ddddd', 'eeeeee'], dtype=any_string_dtype)
```

### Step 2: Assign result = s.str.center(...)

```python
result = s.str.center(5, fillchar='X')
```

### Step 3: Assign expected = Series(...)

```python
expected = Series(['XXaXX', 'XXbbX', 'Xcccc', 'ddddd', 'eeeeee'], dtype=any_string_dtype)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign expected = np.array(...)

```python
expected = np.array([v.center(5, 'X') for v in np.array(s)], dtype=np.object_)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(np.array(result, dtype=np.object_), expected)
```

### Step 7: Assign result = s.str.ljust(...)

```python
result = s.str.ljust(5, fillchar='X')
```

### Step 8: Assign expected = Series(...)

```python
expected = Series(['aXXXX', 'bbXXX', 'ccccX', 'ddddd', 'eeeeee'], dtype=any_string_dtype)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 10: Assign expected = np.array(...)

```python
expected = np.array([v.ljust(5, 'X') for v in np.array(s)], dtype=np.object_)
```

### Step 11: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(np.array(result, dtype=np.object_), expected)
```

### Step 12: Assign result = s.str.rjust(...)

```python
result = s.str.rjust(5, fillchar='X')
```

### Step 13: Assign expected = Series(...)

```python
expected = Series(['XXXXa', 'XXXbb', 'Xcccc', 'ddddd', 'eeeeee'], dtype=any_string_dtype)
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 15: Assign expected = np.array(...)

```python
expected = np.array([v.rjust(5, 'X') for v in np.array(s)], dtype=np.object_)
```

### Step 16: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(np.array(result, dtype=np.object_), expected)
```


## Complete Example

```python
# Setup
# Fixtures: any_string_dtype

# Workflow
s = Series(['a', 'bb', 'cccc', 'ddddd', 'eeeeee'], dtype=any_string_dtype)
result = s.str.center(5, fillchar='X')
expected = Series(['XXaXX', 'XXbbX', 'Xcccc', 'ddddd', 'eeeeee'], dtype=any_string_dtype)
tm.assert_series_equal(result, expected)
expected = np.array([v.center(5, 'X') for v in np.array(s)], dtype=np.object_)
tm.assert_numpy_array_equal(np.array(result, dtype=np.object_), expected)
result = s.str.ljust(5, fillchar='X')
expected = Series(['aXXXX', 'bbXXX', 'ccccX', 'ddddd', 'eeeeee'], dtype=any_string_dtype)
tm.assert_series_equal(result, expected)
expected = np.array([v.ljust(5, 'X') for v in np.array(s)], dtype=np.object_)
tm.assert_numpy_array_equal(np.array(result, dtype=np.object_), expected)
result = s.str.rjust(5, fillchar='X')
expected = Series(['XXXXa', 'XXXbb', 'Xcccc', 'ddddd', 'eeeeee'], dtype=any_string_dtype)
tm.assert_series_equal(result, expected)
expected = np.array([v.rjust(5, 'X') for v in np.array(s)], dtype=np.object_)
tm.assert_numpy_array_equal(np.array(result, dtype=np.object_), expected)
```

## Next Steps


---

*Source: test_case_justify.py:293 | Complexity: Advanced | Last updated: 2026-06-02*