# How To: Index

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test index

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
# Fixtures: method, sub, start, end, index_or_series, any_string_dtype, expected
```

## Step-by-Step Guide

### Step 1: Assign obj = index_or_series(...)

```python
obj = index_or_series(['ABCDEFG', 'BCDEFEF', 'DEFGHIJEF', 'EFGHEF'], dtype=any_string_dtype)
```

**Verification:**
```python
assert list(result) == expected
```

### Step 2: Assign expected_dtype = value

```python
expected_dtype = np.int64 if is_object_or_nan_string_dtype(any_string_dtype) else 'Int64'
```

### Step 3: Assign expected = index_or_series(...)

```python
expected = index_or_series(expected, dtype=expected_dtype)
```

### Step 4: Assign result = getattr(...)

```python
result = getattr(obj.str, method)(sub, start, end)
```

### Step 5: Assign expected = value

```python
expected = [getattr(item, method)(sub, start, end) for item in obj]
```

**Verification:**
```python
assert list(result) == expected
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: method, sub, start, end, index_or_series, any_string_dtype, expected

# Workflow
obj = index_or_series(['ABCDEFG', 'BCDEFEF', 'DEFGHIJEF', 'EFGHEF'], dtype=any_string_dtype)
expected_dtype = np.int64 if is_object_or_nan_string_dtype(any_string_dtype) else 'Int64'
expected = index_or_series(expected, dtype=expected_dtype)
result = getattr(obj.str, method)(sub, start, end)
if index_or_series is Series:
    tm.assert_series_equal(result, expected)
else:
    tm.assert_index_equal(result, expected)
expected = [getattr(item, method)(sub, start, end) for item in obj]
assert list(result) == expected
```

## Next Steps


---

*Source: test_strings.py:363 | Complexity: Intermediate | Last updated: 2026-06-02*