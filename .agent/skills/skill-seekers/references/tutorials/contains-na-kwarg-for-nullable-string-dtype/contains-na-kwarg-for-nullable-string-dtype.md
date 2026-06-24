# How To: Contains Na Kwarg For Nullable String Dtype

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test contains na kwarg for nullable string dtype

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
# Fixtures: nullable_string_dtype, na, expected, regex
```

## Step-by-Step Guide

### Step 1: Assign values = Series(...)

```python
values = Series(['a', 'b', 'c', 'a', np.nan], dtype=nullable_string_dtype)
```

### Step 2: Assign msg = "Allowing a non-bool 'na' in obj.str.contains is deprecated and will raise in a future version"

```python
msg = "Allowing a non-bool 'na' in obj.str.contains is deprecated and will raise in a future version"
```

### Step 3: Assign warn = None

```python
warn = None
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([True, False, False, True, expected], dtype='boolean')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign warn = FutureWarning

```python
warn = FutureWarning
```

### Step 7: Assign result = values.str.contains(...)

```python
result = values.str.contains('a', na=na, regex=regex)
```


## Complete Example

```python
# Setup
# Fixtures: nullable_string_dtype, na, expected, regex

# Workflow
values = Series(['a', 'b', 'c', 'a', np.nan], dtype=nullable_string_dtype)
msg = "Allowing a non-bool 'na' in obj.str.contains is deprecated and will raise in a future version"
warn = None
if not pd.isna(na) and (not isinstance(na, bool)):
    warn = FutureWarning
with tm.assert_produces_warning(warn, match=msg):
    result = values.str.contains('a', na=na, regex=regex)
expected = Series([True, False, False, True, expected], dtype='boolean')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_find_replace.py:171 | Complexity: Intermediate | Last updated: 2026-06-02*