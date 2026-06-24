# How To: Interpolate Datetimelike Values

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test interpolate datetimelike values

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign orig = Series(...)

```python
orig = Series(date_range('2012-01-01', periods=5))
```

### Step 2: Assign ser = orig.copy(...)

```python
ser = orig.copy()
```

### Step 3: Assign unknown = NaT

```python
ser[2] = NaT
```

### Step 4: Assign res = frame_or_series.interpolate(...)

```python
res = frame_or_series(ser).interpolate()
```

### Step 5: Assign expected = frame_or_series(...)

```python
expected = frame_or_series(orig)
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(res, expected)
```

### Step 7: Assign ser_tz = ser.dt.tz_localize(...)

```python
ser_tz = ser.dt.tz_localize('US/Pacific')
```

### Step 8: Assign res_tz = frame_or_series.interpolate(...)

```python
res_tz = frame_or_series(ser_tz).interpolate()
```

### Step 9: Assign expected_tz = frame_or_series(...)

```python
expected_tz = frame_or_series(orig.dt.tz_localize('US/Pacific'))
```

### Step 10: Call tm.assert_equal()

```python
tm.assert_equal(res_tz, expected_tz)
```

### Step 11: Assign ser_td = value

```python
ser_td = ser - ser[0]
```

### Step 12: Assign res_td = frame_or_series.interpolate(...)

```python
res_td = frame_or_series(ser_td).interpolate()
```

### Step 13: Assign expected_td = frame_or_series(...)

```python
expected_td = frame_or_series(orig - orig[0])
```

### Step 14: Call tm.assert_equal()

```python
tm.assert_equal(res_td, expected_td)
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
orig = Series(date_range('2012-01-01', periods=5))
ser = orig.copy()
ser[2] = NaT
res = frame_or_series(ser).interpolate()
expected = frame_or_series(orig)
tm.assert_equal(res, expected)
ser_tz = ser.dt.tz_localize('US/Pacific')
res_tz = frame_or_series(ser_tz).interpolate()
expected_tz = frame_or_series(orig.dt.tz_localize('US/Pacific'))
tm.assert_equal(res_tz, expected_tz)
ser_td = ser - ser[0]
res_td = frame_or_series(ser_td).interpolate()
expected_td = frame_or_series(orig - orig[0])
tm.assert_equal(res_td, expected_td)
```

## Next Steps


---

*Source: test_interpolate.py:34 | Complexity: Advanced | Last updated: 2026-06-02*