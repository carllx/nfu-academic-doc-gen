# How To: Dt Namespace Accessor Datetime64Tz

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dt namespace accessor datetime64tz

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('20130101', periods=5, tz='US/Eastern')
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
assert str(tz_result) == 'CET'
```

### Step 4: Assign result = ser.dt.tz_convert(...)

```python
result = ser.dt.tz_convert('CET')
```

**Verification:**
```python
assert freq_result == DatetimeIndex(ser.values, freq='infer').freq
```

### Step 5: Assign expected = Series(...)

```python
expected = Series(ser._values.tz_convert('CET'), index=ser.index, name='xxx')
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign tz_result = value

```python
tz_result = result.dt.tz
```

**Verification:**
```python
assert str(tz_result) == 'CET'
```

### Step 8: Assign freq_result = value

```python
freq_result = ser.dt.freq
```

**Verification:**
```python
assert freq_result == DatetimeIndex(ser.values, freq='infer').freq
```

### Step 9: Call getattr()

```python
getattr(ser.dt, prop)
```

### Step 10: Assign result = ser.dt.to_pydatetime(...)

```python
result = ser.dt.to_pydatetime()
```

### Step 11: Call self._compare()

```python
self._compare(ser, prop)
```


## Complete Example

```python
# Workflow
dti = date_range('20130101', periods=5, tz='US/Eastern')
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
result = ser.dt.tz_convert('CET')
expected = Series(ser._values.tz_convert('CET'), index=ser.index, name='xxx')
tm.assert_series_equal(result, expected)
tz_result = result.dt.tz
assert str(tz_result) == 'CET'
freq_result = ser.dt.freq
assert freq_result == DatetimeIndex(ser.values, freq='infer').freq
```

## Next Steps


---

*Source: test_dt_accessor.py:143 | Complexity: Advanced | Last updated: 2026-06-02*