# How To: Dt Namespace Accessor Datetime64

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dt namespace accessor datetime64

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `calendar`
- `datetime`
- `locale`
- `unicodedata`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs.timezones`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.indexes.accessors`

**Setup Required:**
```python
# Fixtures: freq
```

## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('20130101', periods=5, freq=freq)
```

**Verification:**
```python
assert isinstance(result, np.ndarray)
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(dti, name='xxx')
```

**Verification:**
```python
assert result.dtype == object
```

### Step 3: Assign msg = 'The behavior of DatetimeProperties.to_pydatetime is deprecated'

```python
msg = 'The behavior of DatetimeProperties.to_pydatetime is deprecated'
```

**Verification:**
```python
assert str(tz_result) == 'US/Eastern'
```

### Step 4: Assign result = ser.dt.tz_localize(...)

```python
result = ser.dt.tz_localize('US/Eastern')
```

**Verification:**
```python
assert freq_result == DatetimeIndex(ser.values, freq='infer').freq
```

### Step 5: Assign exp_values = DatetimeIndex.tz_localize(...)

```python
exp_values = DatetimeIndex(ser.values).tz_localize('US/Eastern')
```

### Step 6: Assign expected = Series(...)

```python
expected = Series(exp_values, index=ser.index, name='xxx')
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign tz_result = value

```python
tz_result = result.dt.tz
```

**Verification:**
```python
assert str(tz_result) == 'US/Eastern'
```

### Step 9: Assign freq_result = value

```python
freq_result = ser.dt.freq
```

**Verification:**
```python
assert freq_result == DatetimeIndex(ser.values, freq='infer').freq
```

### Step 10: Assign result = ser.dt.tz_localize.dt.tz_convert(...)

```python
result = ser.dt.tz_localize('UTC').dt.tz_convert('US/Eastern')
```

### Step 11: Assign exp_values = DatetimeIndex.tz_localize.tz_convert(...)

```python
exp_values = DatetimeIndex(ser.values).tz_localize('UTC').tz_convert('US/Eastern')
```

### Step 12: Assign expected = Series(...)

```python
expected = Series(exp_values, index=ser.index, name='xxx')
```

### Step 13: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 14: Call getattr()

```python
getattr(ser.dt, prop)
```

### Step 15: Assign result = ser.dt.to_pydatetime(...)

```python
result = ser.dt.to_pydatetime()
```

### Step 16: Call self._compare()

```python
self._compare(ser, prop)
```


## Complete Example

```python
# Setup
# Fixtures: freq

# Workflow
dti = date_range('20130101', periods=5, freq=freq)
ser = Series(dti, name='xxx')
for prop in ok_for_dt:
    if prop != 'freq':
        self._compare(ser, prop)
for prop in ok_for_dt_methods:
    getattr(ser.dt, prop)
msg = 'The behavior of DatetimeProperties.to_pydatetime is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = ser.dt.to_pydatetime()
assert isinstance(result, np.ndarray)
assert result.dtype == object
result = ser.dt.tz_localize('US/Eastern')
exp_values = DatetimeIndex(ser.values).tz_localize('US/Eastern')
expected = Series(exp_values, index=ser.index, name='xxx')
tm.assert_series_equal(result, expected)
tz_result = result.dt.tz
assert str(tz_result) == 'US/Eastern'
freq_result = ser.dt.freq
assert freq_result == DatetimeIndex(ser.values, freq='infer').freq
result = ser.dt.tz_localize('UTC').dt.tz_convert('US/Eastern')
exp_values = DatetimeIndex(ser.values).tz_localize('UTC').tz_convert('US/Eastern')
expected = Series(exp_values, index=ser.index, name='xxx')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_dt_accessor.py:103 | Complexity: Advanced | Last updated: 2026-06-02*