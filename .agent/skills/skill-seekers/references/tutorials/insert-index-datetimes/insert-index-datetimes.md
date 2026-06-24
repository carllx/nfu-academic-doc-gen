# How To: Insert Index Datetimes

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test insert index datetimes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: fill_val, exp_dtype, insert_value
```

## Step-by-Step Guide

### Step 1: Assign obj = pd.DatetimeIndex.as_unit(...)

```python
obj = pd.DatetimeIndex(['2011-01-01', '2011-01-02', '2011-01-03', '2011-01-04'], tz=fill_val.tz).as_unit('ns')
```

**Verification:**
```python
assert obj.dtype == exp_dtype
```

### Step 2: Assign exp = pd.DatetimeIndex.as_unit(...)

```python
exp = pd.DatetimeIndex(['2011-01-01', fill_val.date(), '2011-01-02', '2011-01-03', '2011-01-04'], tz=fill_val.tz).as_unit('ns')
```

**Verification:**
```python
assert expected.dtype == object
```

### Step 3: Call self._assert_insert_conversion()

```python
self._assert_insert_conversion(obj, fill_val, exp, exp_dtype)
```

**Verification:**
```python
assert expected.dtype == obj.dtype
```

### Step 4: Assign item = 1

```python
item = 1
```

**Verification:**
```python
assert expected.dtype == object
```

### Step 5: Assign result = obj.insert(...)

```python
result = obj.insert(1, item)
```

**Verification:**
```python
assert expected[1] == item
```

### Step 6: Assign expected = obj.astype.insert(...)

```python
expected = obj.astype(object).insert(1, item)
```

**Verification:**
```python
assert expected.dtype == object
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 8: Assign ts = pd.Timestamp(...)

```python
ts = pd.Timestamp('2012-01-01')
```

### Step 9: Assign result = obj.insert(...)

```python
result = obj.insert(1, ts)
```

### Step 10: Assign expected = obj.astype.insert(...)

```python
expected = obj.astype(object).insert(1, ts)
```

**Verification:**
```python
assert expected.dtype == object
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 12: Assign ts = pd.Timestamp(...)

```python
ts = pd.Timestamp('2012-01-01', tz='Asia/Tokyo')
```

### Step 13: Assign result = obj.insert(...)

```python
result = obj.insert(1, ts)
```

### Step 14: Assign expected = obj.insert(...)

```python
expected = obj.insert(1, ts.tz_convert(obj.dtype.tz))
```

**Verification:**
```python
assert expected.dtype == obj.dtype
```

### Step 15: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 16: Assign ts = pd.Timestamp(...)

```python
ts = pd.Timestamp('2012-01-01', tz='Asia/Tokyo')
```

### Step 17: Assign result = obj.insert(...)

```python
result = obj.insert(1, ts)
```

### Step 18: Assign expected = obj.astype.insert(...)

```python
expected = obj.astype(object).insert(1, ts)
```

**Verification:**
```python
assert expected.dtype == object
```

### Step 19: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: fill_val, exp_dtype, insert_value

# Workflow
obj = pd.DatetimeIndex(['2011-01-01', '2011-01-02', '2011-01-03', '2011-01-04'], tz=fill_val.tz).as_unit('ns')
assert obj.dtype == exp_dtype
exp = pd.DatetimeIndex(['2011-01-01', fill_val.date(), '2011-01-02', '2011-01-03', '2011-01-04'], tz=fill_val.tz).as_unit('ns')
self._assert_insert_conversion(obj, fill_val, exp, exp_dtype)
if fill_val.tz:
    ts = pd.Timestamp('2012-01-01')
    result = obj.insert(1, ts)
    expected = obj.astype(object).insert(1, ts)
    assert expected.dtype == object
    tm.assert_index_equal(result, expected)
    ts = pd.Timestamp('2012-01-01', tz='Asia/Tokyo')
    result = obj.insert(1, ts)
    expected = obj.insert(1, ts.tz_convert(obj.dtype.tz))
    assert expected.dtype == obj.dtype
    tm.assert_index_equal(result, expected)
else:
    ts = pd.Timestamp('2012-01-01', tz='Asia/Tokyo')
    result = obj.insert(1, ts)
    expected = obj.astype(object).insert(1, ts)
    assert expected.dtype == object
    tm.assert_index_equal(result, expected)
item = 1
result = obj.insert(1, item)
expected = obj.astype(object).insert(1, item)
assert expected[1] == item
assert expected.dtype == object
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_coercion.py:261 | Complexity: Advanced | Last updated: 2026-06-02*