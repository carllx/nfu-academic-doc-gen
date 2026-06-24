# How To: Get Numeric Data Preserve Dtype

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get numeric data preserve dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign obj = Series(...)

```python
obj = Series([1, 2, 3])
```

**Verification:**
```python
assert obj.iloc[0] == 1
```

### Step 2: Assign result = obj._get_numeric_data(...)

```python
result = obj._get_numeric_data()
```

**Verification:**
```python
assert obj.iloc[0] == 0
```

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, obj)
```

### Step 4: Assign obj = Series(...)

```python
obj = Series([1, '2', 3.0])
```

### Step 5: Assign result = obj._get_numeric_data(...)

```python
result = obj._get_numeric_data()
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([], dtype=object, index=Index([], dtype=object))
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign obj = Series(...)

```python
obj = Series([True, False, True])
```

### Step 9: Assign result = obj._get_numeric_data(...)

```python
result = obj._get_numeric_data()
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, obj)
```

### Step 11: Assign obj = Series(...)

```python
obj = Series(date_range('20130101', periods=3))
```

### Step 12: Assign result = obj._get_numeric_data(...)

```python
result = obj._get_numeric_data()
```

### Step 13: Assign expected = Series(...)

```python
expected = Series([], dtype='M8[ns]', index=Index([], dtype=object))
```

### Step 14: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 15: Assign unknown = 0

```python
result.iloc[0] = 0
```

**Verification:**
```python
assert obj.iloc[0] == 1
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, warn_copy_on_write

# Workflow
obj = Series([1, 2, 3])
result = obj._get_numeric_data()
tm.assert_series_equal(result, obj)
with tm.assert_cow_warning(warn_copy_on_write):
    result.iloc[0] = 0
if using_copy_on_write:
    assert obj.iloc[0] == 1
else:
    assert obj.iloc[0] == 0
obj = Series([1, '2', 3.0])
result = obj._get_numeric_data()
expected = Series([], dtype=object, index=Index([], dtype=object))
tm.assert_series_equal(result, expected)
obj = Series([True, False, True])
result = obj._get_numeric_data()
tm.assert_series_equal(result, obj)
obj = Series(date_range('20130101', periods=3))
result = obj._get_numeric_data()
expected = Series([], dtype='M8[ns]', index=Index([], dtype=object))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_get_numeric_data.py:10 | Complexity: Advanced | Last updated: 2026-06-02*