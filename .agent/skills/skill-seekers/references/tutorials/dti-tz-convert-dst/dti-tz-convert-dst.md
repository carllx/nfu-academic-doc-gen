# How To: Dti Tz Convert Dst

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dti tz convert dst

## Prerequisites

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = date_range(...)

```python
idx = date_range('2014-03-08 00:00', '2014-03-09 00:00', freq='D', tz='UTC')
```

### Step 2: Assign idx = idx.tz_convert(...)

```python
idx = idx.tz_convert('US/Eastern')
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.hour, Index([19, 19], dtype=np.int32))
```

### Step 4: Assign idx = date_range(...)

```python
idx = date_range('2014-03-08 00:00', '2014-03-09 00:00', freq='D', tz='US/Eastern')
```

### Step 5: Assign idx = idx.tz_convert(...)

```python
idx = idx.tz_convert('UTC')
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.hour, Index([5, 5], dtype=np.int32))
```

### Step 7: Assign idx = date_range(...)

```python
idx = date_range('2014-11-01 00:00', '2014-11-02 00:00', freq='D', tz='UTC')
```

### Step 8: Assign idx = idx.tz_convert(...)

```python
idx = idx.tz_convert('US/Eastern')
```

### Step 9: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.hour, Index([20, 20], dtype=np.int32))
```

### Step 10: Assign idx = date_range(...)

```python
idx = date_range('2014-11-01 00:00', '2014-11-02 000:00', freq='D', tz='US/Eastern')
```

### Step 11: Assign idx = idx.tz_convert(...)

```python
idx = idx.tz_convert('UTC')
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.hour, Index([4, 4], dtype=np.int32))
```

### Step 13: Assign idx = date_range(...)

```python
idx = date_range('2014-03-08 23:00', '2014-03-09 09:00', freq=freq, tz='UTC')
```

### Step 14: Assign idx = idx.tz_convert(...)

```python
idx = idx.tz_convert('US/Eastern')
```

### Step 15: Assign expected = np.repeat(...)

```python
expected = np.repeat(np.array([18, 19, 20, 21, 22, 23, 0, 1, 3, 4, 5]), np.array([n, n, n, n, n, n, n, n, n, n, 1]))
```

### Step 16: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.hour, Index(expected, dtype=np.int32))
```

### Step 17: Assign idx = date_range(...)

```python
idx = date_range('2014-03-08 18:00', '2014-03-09 05:00', freq=freq, tz='US/Eastern')
```

### Step 18: Assign idx = idx.tz_convert(...)

```python
idx = idx.tz_convert('UTC')
```

### Step 19: Assign expected = np.repeat(...)

```python
expected = np.repeat(np.array([23, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), np.array([n, n, n, n, n, n, n, n, n, n, 1]))
```

### Step 20: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.hour, Index(expected, dtype=np.int32))
```

### Step 21: Assign idx = date_range(...)

```python
idx = date_range('2014-11-01 23:00', '2014-11-02 09:00', freq=freq, tz='UTC')
```

### Step 22: Assign idx = idx.tz_convert(...)

```python
idx = idx.tz_convert('US/Eastern')
```

### Step 23: Assign expected = np.repeat(...)

```python
expected = np.repeat(np.array([19, 20, 21, 22, 23, 0, 1, 1, 2, 3, 4]), np.array([n, n, n, n, n, n, n, n, n, n, 1]))
```

### Step 24: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.hour, Index(expected, dtype=np.int32))
```

### Step 25: Assign idx = date_range(...)

```python
idx = date_range('2014-11-01 18:00', '2014-11-02 05:00', freq=freq, tz='US/Eastern')
```

### Step 26: Assign idx = idx.tz_convert(...)

```python
idx = idx.tz_convert('UTC')
```

### Step 27: Assign expected = np.repeat(...)

```python
expected = np.repeat(np.array([22, 23, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), np.array([n, n, n, n, n, n, n, n, n, n, n, n, 1]))
```

### Step 28: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx.hour, Index(expected, dtype=np.int32))
```


## Complete Example

```python
# Workflow
for freq, n in [('h', 1), ('min', 60), ('s', 3600)]:
    idx = date_range('2014-03-08 23:00', '2014-03-09 09:00', freq=freq, tz='UTC')
    idx = idx.tz_convert('US/Eastern')
    expected = np.repeat(np.array([18, 19, 20, 21, 22, 23, 0, 1, 3, 4, 5]), np.array([n, n, n, n, n, n, n, n, n, n, 1]))
    tm.assert_index_equal(idx.hour, Index(expected, dtype=np.int32))
    idx = date_range('2014-03-08 18:00', '2014-03-09 05:00', freq=freq, tz='US/Eastern')
    idx = idx.tz_convert('UTC')
    expected = np.repeat(np.array([23, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), np.array([n, n, n, n, n, n, n, n, n, n, 1]))
    tm.assert_index_equal(idx.hour, Index(expected, dtype=np.int32))
    idx = date_range('2014-11-01 23:00', '2014-11-02 09:00', freq=freq, tz='UTC')
    idx = idx.tz_convert('US/Eastern')
    expected = np.repeat(np.array([19, 20, 21, 22, 23, 0, 1, 1, 2, 3, 4]), np.array([n, n, n, n, n, n, n, n, n, n, 1]))
    tm.assert_index_equal(idx.hour, Index(expected, dtype=np.int32))
    idx = date_range('2014-11-01 18:00', '2014-11-02 05:00', freq=freq, tz='US/Eastern')
    idx = idx.tz_convert('UTC')
    expected = np.repeat(np.array([22, 23, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), np.array([n, n, n, n, n, n, n, n, n, n, n, n, 1]))
    tm.assert_index_equal(idx.hour, Index(expected, dtype=np.int32))
idx = date_range('2014-03-08 00:00', '2014-03-09 00:00', freq='D', tz='UTC')
idx = idx.tz_convert('US/Eastern')
tm.assert_index_equal(idx.hour, Index([19, 19], dtype=np.int32))
idx = date_range('2014-03-08 00:00', '2014-03-09 00:00', freq='D', tz='US/Eastern')
idx = idx.tz_convert('UTC')
tm.assert_index_equal(idx.hour, Index([5, 5], dtype=np.int32))
idx = date_range('2014-11-01 00:00', '2014-11-02 00:00', freq='D', tz='UTC')
idx = idx.tz_convert('US/Eastern')
tm.assert_index_equal(idx.hour, Index([20, 20], dtype=np.int32))
idx = date_range('2014-11-01 00:00', '2014-11-02 000:00', freq='D', tz='US/Eastern')
idx = idx.tz_convert('UTC')
tm.assert_index_equal(idx.hour, Index([4, 4], dtype=np.int32))
```

## Next Steps


---

*Source: test_tz_convert.py:157 | Complexity: Advanced | Last updated: 2026-06-02*