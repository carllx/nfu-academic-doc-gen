# How To: Astype Datetime64Tz

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype datetime64tz

## Prerequisites

**Required Modules:**
- `datetime`
- `importlib`
- `string`
- `sys`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(date_range('20130101', periods=3, tz='US/Eastern'))
```

### Step 2: Assign result = ser.astype(...)

```python
result = ser.astype(object)
```

### Step 3: Assign expected = Series(...)

```python
expected = Series(ser.astype(object), dtype=object)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = Series.dt.tz_localize.dt.tz_convert(...)

```python
result = Series(ser.values).dt.tz_localize('UTC').dt.tz_convert(ser.dt.tz)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, ser)
```

### Step 7: Assign result = Series(...)

```python
result = Series(ser.astype(object))
```

### Step 8: Assign expected = ser.astype(...)

```python
expected = ser.astype(object)
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 10: Assign msg = 'Cannot use .astype to convert from timezone-naive'

```python
msg = 'Cannot use .astype to convert from timezone-naive'
```

### Step 11: Assign result = ser.astype(...)

```python
result = ser.astype('datetime64[ns, CET]')
```

### Step 12: Assign expected = Series(...)

```python
expected = Series(date_range('20130101 06:00:00', periods=3, tz='CET'))
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 14: Call Series.astype()

```python
Series(ser.values).astype('datetime64[ns, US/Eastern]')
```

### Step 15: Call Series.astype()

```python
Series(ser.values).astype(ser.dtype)
```


## Complete Example

```python
# Workflow
ser = Series(date_range('20130101', periods=3, tz='US/Eastern'))
result = ser.astype(object)
expected = Series(ser.astype(object), dtype=object)
tm.assert_series_equal(result, expected)
result = Series(ser.values).dt.tz_localize('UTC').dt.tz_convert(ser.dt.tz)
tm.assert_series_equal(result, ser)
result = Series(ser.astype(object))
expected = ser.astype(object)
tm.assert_series_equal(result, expected)
msg = 'Cannot use .astype to convert from timezone-naive'
with pytest.raises(TypeError, match=msg):
    Series(ser.values).astype('datetime64[ns, US/Eastern]')
with pytest.raises(TypeError, match=msg):
    Series(ser.values).astype(ser.dtype)
result = ser.astype('datetime64[ns, CET]')
expected = Series(date_range('20130101 06:00:00', periods=3, tz='CET'))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_astype.py:257 | Complexity: Advanced | Last updated: 2026-06-02*