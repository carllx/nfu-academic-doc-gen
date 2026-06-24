# How To: Fillna Consistency

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fillna consistency

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([Timestamp('20130101'), NaT])
```

### Step 2: Assign result = ser.fillna(...)

```python
result = ser.fillna(Timestamp('20130101', tz='US/Eastern'))
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([Timestamp('20130101'), Timestamp('2013-01-01', tz='US/Eastern')], dtype='object')
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = ser.where(...)

```python
result = ser.where([True, False], Timestamp('20130101', tz='US/Eastern'))
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign result = ser.where(...)

```python
result = ser.where([True, False], Timestamp('20130101', tz='US/Eastern'))
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 9: Assign result = ser.fillna(...)

```python
result = ser.fillna('foo')
```

### Step 10: Assign expected = Series(...)

```python
expected = Series([Timestamp('20130101'), 'foo'])
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 12: Assign ser2 = ser.copy(...)

```python
ser2 = ser.copy()
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser2, expected)
```

### Step 14: Assign unknown = 'foo'

```python
ser2[1] = 'foo'
```


## Complete Example

```python
# Workflow
ser = Series([Timestamp('20130101'), NaT])
result = ser.fillna(Timestamp('20130101', tz='US/Eastern'))
expected = Series([Timestamp('20130101'), Timestamp('2013-01-01', tz='US/Eastern')], dtype='object')
tm.assert_series_equal(result, expected)
result = ser.where([True, False], Timestamp('20130101', tz='US/Eastern'))
tm.assert_series_equal(result, expected)
result = ser.where([True, False], Timestamp('20130101', tz='US/Eastern'))
tm.assert_series_equal(result, expected)
result = ser.fillna('foo')
expected = Series([Timestamp('20130101'), 'foo'])
tm.assert_series_equal(result, expected)
ser2 = ser.copy()
with tm.assert_produces_warning(FutureWarning, match='incompatible dtype'):
    ser2[1] = 'foo'
tm.assert_series_equal(ser2, expected)
```

## Next Steps


---

*Source: test_fillna.py:148 | Complexity: Advanced | Last updated: 2026-06-02*