# How To: To Numeric From Nullable String Coerce

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to numeric from nullable string coerce

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `decimal`
- `numpy`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: nullable_string_dtype
```

## Step-by-Step Guide

### Step 1: Assign values = value

```python
values = ['a', '1']
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(values, dtype=nullable_string_dtype)
```

### Step 3: Assign result = to_numeric(...)

```python
result = to_numeric(ser, errors='coerce')
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([pd.NA, 1], dtype='Int64')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: nullable_string_dtype

# Workflow
values = ['a', '1']
ser = Series(values, dtype=nullable_string_dtype)
result = to_numeric(ser, errors='coerce')
expected = Series([pd.NA, 1], dtype='Int64')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_to_numeric.py:762 | Complexity: Intermediate | Last updated: 2026-06-02*