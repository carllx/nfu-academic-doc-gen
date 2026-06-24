# How To: Constructor Datetime64 Tzformat

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test constructor datetime64 tzformat

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `functools`
- `operator`
- `dateutil`
- `dateutil.tz`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: freq
```

## Step-by-Step Guide

### Step 1: Assign idx = date_range(...)

```python
idx = date_range('2013-01-01T00:00:00-05:00', '2016-01-01T23:59:59-05:00', freq=freq)
```

### Step 2: Assign expected = date_range(...)

```python
expected = date_range('2013-01-01T00:00:00', '2016-01-01T23:59:59', freq=freq, tz=timezone(timedelta(minutes=-300)))
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, expected)
```

### Step 4: Assign expected_i8 = date_range(...)

```python
expected_i8 = date_range('2013-01-01T00:00:00', '2016-01-01T23:59:59', freq=freq, tz='America/Lima')
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.asi8, expected_i8.asi8)
```

### Step 6: Assign idx = date_range(...)

```python
idx = date_range('2013-01-01T00:00:00+09:00', '2016-01-01T23:59:59+09:00', freq=freq)
```

### Step 7: Assign expected = date_range(...)

```python
expected = date_range('2013-01-01T00:00:00', '2016-01-01T23:59:59', freq=freq, tz=timezone(timedelta(minutes=540)))
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, expected)
```

### Step 9: Assign expected_i8 = date_range(...)

```python
expected_i8 = date_range('2013-01-01T00:00:00', '2016-01-01T23:59:59', freq=freq, tz='Asia/Tokyo')
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.asi8, expected_i8.asi8)
```

### Step 11: Assign idx = date_range(...)

```python
idx = date_range('2013/1/1 0:00:00-5:00', '2016/1/1 23:59:59-5:00', freq=freq)
```

### Step 12: Assign expected = date_range(...)

```python
expected = date_range('2013-01-01T00:00:00', '2016-01-01T23:59:59', freq=freq, tz=timezone(timedelta(minutes=-300)))
```

### Step 13: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, expected)
```

### Step 14: Assign expected_i8 = date_range(...)

```python
expected_i8 = date_range('2013-01-01T00:00:00', '2016-01-01T23:59:59', freq=freq, tz='America/Lima')
```

### Step 15: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.asi8, expected_i8.asi8)
```

### Step 16: Assign idx = date_range(...)

```python
idx = date_range('2013/1/1 0:00:00+9:00', '2016/1/1 23:59:59+09:00', freq=freq)
```

### Step 17: Assign expected = date_range(...)

```python
expected = date_range('2013-01-01T00:00:00', '2016-01-01T23:59:59', freq=freq, tz=timezone(timedelta(minutes=540)))
```

### Step 18: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, expected)
```

### Step 19: Assign expected_i8 = date_range(...)

```python
expected_i8 = date_range('2013-01-01T00:00:00', '2016-01-01T23:59:59', freq=freq, tz='Asia/Tokyo')
```

### Step 20: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.asi8, expected_i8.asi8)
```


## Complete Example

```python
# Setup
# Fixtures: freq

# Workflow
idx = date_range('2013-01-01T00:00:00-05:00', '2016-01-01T23:59:59-05:00', freq=freq)
expected = date_range('2013-01-01T00:00:00', '2016-01-01T23:59:59', freq=freq, tz=timezone(timedelta(minutes=-300)))
tm.assert_index_equal(idx, expected)
expected_i8 = date_range('2013-01-01T00:00:00', '2016-01-01T23:59:59', freq=freq, tz='America/Lima')
tm.assert_numpy_array_equal(idx.asi8, expected_i8.asi8)
idx = date_range('2013-01-01T00:00:00+09:00', '2016-01-01T23:59:59+09:00', freq=freq)
expected = date_range('2013-01-01T00:00:00', '2016-01-01T23:59:59', freq=freq, tz=timezone(timedelta(minutes=540)))
tm.assert_index_equal(idx, expected)
expected_i8 = date_range('2013-01-01T00:00:00', '2016-01-01T23:59:59', freq=freq, tz='Asia/Tokyo')
tm.assert_numpy_array_equal(idx.asi8, expected_i8.asi8)
idx = date_range('2013/1/1 0:00:00-5:00', '2016/1/1 23:59:59-5:00', freq=freq)
expected = date_range('2013-01-01T00:00:00', '2016-01-01T23:59:59', freq=freq, tz=timezone(timedelta(minutes=-300)))
tm.assert_index_equal(idx, expected)
expected_i8 = date_range('2013-01-01T00:00:00', '2016-01-01T23:59:59', freq=freq, tz='America/Lima')
tm.assert_numpy_array_equal(idx.asi8, expected_i8.asi8)
idx = date_range('2013/1/1 0:00:00+9:00', '2016/1/1 23:59:59+09:00', freq=freq)
expected = date_range('2013-01-01T00:00:00', '2016-01-01T23:59:59', freq=freq, tz=timezone(timedelta(minutes=540)))
tm.assert_index_equal(idx, expected)
expected_i8 = date_range('2013-01-01T00:00:00', '2016-01-01T23:59:59', freq=freq, tz='Asia/Tokyo')
tm.assert_numpy_array_equal(idx.asi8, expected_i8.asi8)
```

## Next Steps


---

*Source: test_constructors.py:641 | Complexity: Advanced | Last updated: 2026-06-02*