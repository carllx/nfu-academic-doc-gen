# How To: Tz Localize Nonexistent

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test tz localize nonexistent

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: warsaw, method, exp, unit
```

## Step-by-Step Guide

### Step 1: Assign tz = warsaw

```python
tz = warsaw
```

### Step 2: Assign n = 60

```python
n = 60
```

### Step 3: Assign dti = date_range(...)

```python
dti = date_range(start='2015-03-29 02:00:00', periods=n, freq='min', unit=unit)
```

### Step 4: Assign ser = Series(...)

```python
ser = Series(1, index=dti)
```

### Step 5: Assign df = ser.to_frame(...)

```python
df = ser.to_frame()
```

### Step 6: Call dti.tz_localize()

```python
dti.tz_localize(tz, nonexistent=method)
```

### Step 7: Call ser.tz_localize()

```python
ser.tz_localize(tz, nonexistent=method)
```

### Step 8: Call df.tz_localize()

```python
df.tz_localize(tz, nonexistent=method)
```

### Step 9: Assign msg = "The nonexistent argument must be one of 'raise', 'NaT', 'shift_forward', 'shift_backward' or a timedelta object"

```python
msg = "The nonexistent argument must be one of 'raise', 'NaT', 'shift_forward', 'shift_backward' or a timedelta object"
```

### Step 10: Assign result = ser.tz_localize(...)

```python
result = ser.tz_localize(tz, nonexistent=method)
```

### Step 11: Assign expected = Series(...)

```python
expected = Series(1, index=DatetimeIndex([exp] * n, tz=tz).as_unit(unit))
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 13: Assign result = df.tz_localize(...)

```python
result = df.tz_localize(tz, nonexistent=method)
```

### Step 14: Assign expected = expected.to_frame(...)

```python
expected = expected.to_frame()
```

### Step 15: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 16: Assign res_index = dti.tz_localize(...)

```python
res_index = dti.tz_localize(tz, nonexistent=method)
```

### Step 17: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res_index, expected.index)
```

### Step 18: Call dti.tz_localize()

```python
dti.tz_localize(tz, nonexistent=method)
```

### Step 19: Call ser.tz_localize()

```python
ser.tz_localize(tz, nonexistent=method)
```

### Step 20: Call df.tz_localize()

```python
df.tz_localize(tz, nonexistent=method)
```


## Complete Example

```python
# Setup
# Fixtures: warsaw, method, exp, unit

# Workflow
tz = warsaw
n = 60
dti = date_range(start='2015-03-29 02:00:00', periods=n, freq='min', unit=unit)
ser = Series(1, index=dti)
df = ser.to_frame()
if method == 'raise':
    with tm.external_error_raised(pytz.NonExistentTimeError):
        dti.tz_localize(tz, nonexistent=method)
    with tm.external_error_raised(pytz.NonExistentTimeError):
        ser.tz_localize(tz, nonexistent=method)
    with tm.external_error_raised(pytz.NonExistentTimeError):
        df.tz_localize(tz, nonexistent=method)
elif exp == 'invalid':
    msg = "The nonexistent argument must be one of 'raise', 'NaT', 'shift_forward', 'shift_backward' or a timedelta object"
    with pytest.raises(ValueError, match=msg):
        dti.tz_localize(tz, nonexistent=method)
    with pytest.raises(ValueError, match=msg):
        ser.tz_localize(tz, nonexistent=method)
    with pytest.raises(ValueError, match=msg):
        df.tz_localize(tz, nonexistent=method)
else:
    result = ser.tz_localize(tz, nonexistent=method)
    expected = Series(1, index=DatetimeIndex([exp] * n, tz=tz).as_unit(unit))
    tm.assert_series_equal(result, expected)
    result = df.tz_localize(tz, nonexistent=method)
    expected = expected.to_frame()
    tm.assert_frame_equal(result, expected)
    res_index = dti.tz_localize(tz, nonexistent=method)
    tm.assert_index_equal(res_index, expected.index)
```

## Next Steps


---

*Source: test_tz_localize.py:73 | Complexity: Advanced | Last updated: 2026-06-02*