# How To: Drop With Ignore Errors

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test drop with ignore errors

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.api.types`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(range(3), index=list('abc'))
```

**Verification:**
```python
assert is_bool_dtype(ser.index)
```

### Step 2: Assign result = ser.drop(...)

```python
result = ser.drop('bc', errors='ignore')
```

**Verification:**
```python
assert ser.index.dtype == bool
```

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, ser)
```

### Step 4: Assign result = ser.drop(...)

```python
result = ser.drop(['a', 'd'], errors='ignore')
```

### Step 5: Assign expected = value

```python
expected = ser.iloc[1:]
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign ser = Series(...)

```python
ser = Series([2, 3], index=[True, False])
```

**Verification:**
```python
assert is_bool_dtype(ser.index)
```

### Step 8: Assign result = ser.drop(...)

```python
result = ser.drop(True)
```

### Step 9: Assign expected = Series(...)

```python
expected = Series([3], index=[False])
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
ser = Series(range(3), index=list('abc'))
result = ser.drop('bc', errors='ignore')
tm.assert_series_equal(result, ser)
result = ser.drop(['a', 'd'], errors='ignore')
expected = ser.iloc[1:]
tm.assert_series_equal(result, expected)
ser = Series([2, 3], index=[True, False])
assert is_bool_dtype(ser.index)
assert ser.index.dtype == bool
result = ser.drop(True)
expected = Series([3], index=[False])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_drop.py:49 | Complexity: Advanced | Last updated: 2026-06-02*