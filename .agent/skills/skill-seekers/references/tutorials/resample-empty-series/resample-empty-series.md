# How To: Resample Empty Series

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test resample empty series

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.groupby`
- `pandas.core.groupby.grouper`
- `pandas.core.indexes.datetimes`
- `pandas.core.indexes.period`
- `pandas.core.indexes.timedeltas`
- `pandas.core.resample`

**Setup Required:**
```python
# Fixtures: freq, empty_series_dti, resample_method
```

## Step-by-Step Guide

### Step 1: Assign ser = empty_series_dti

```python
ser = empty_series_dti
```

**Verification:**
```python
assert result.index.freq == expected.index.freq
```

### Step 2: Assign rs = ser.resample(...)

```python
rs = ser.resample(freq)
```

### Step 3: Assign result = getattr(...)

```python
result = getattr(rs, resample_method)()
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.index, expected.index)
```

**Verification:**
```python
assert result.index.freq == expected.index.freq
```

### Step 5: Assign msg = "Resampling on a TimedeltaIndex requires fixed-duration `freq`, e.g. '24h' or '3D', not <MonthEnd>"

```python
msg = "Resampling on a TimedeltaIndex requires fixed-duration `freq`, e.g. '24h' or '3D', not <MonthEnd>"
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame([], index=ser.index[:0].copy(), columns=['open', 'high', 'low', 'close'])
```

### Step 7: Assign expected.index = _asfreq_compat(...)

```python
expected.index = _asfreq_compat(ser.index, freq)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected, check_dtype=False)
```

### Step 9: Assign expected = ser.copy(...)

```python
expected = ser.copy()
```

### Step 10: Assign expected.index = _asfreq_compat(...)

```python
expected.index = _asfreq_compat(ser.index, freq)
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected, check_dtype=False)
```

### Step 12: Call ser.resample()

```python
ser.resample(freq)
```

### Step 13: Assign freq = 'M'

```python
freq = 'M'
```


## Complete Example

```python
# Setup
# Fixtures: freq, empty_series_dti, resample_method

# Workflow
ser = empty_series_dti
if freq == 'ME' and isinstance(ser.index, TimedeltaIndex):
    msg = "Resampling on a TimedeltaIndex requires fixed-duration `freq`, e.g. '24h' or '3D', not <MonthEnd>"
    with pytest.raises(ValueError, match=msg):
        ser.resample(freq)
    return
elif freq == 'ME' and isinstance(ser.index, PeriodIndex):
    freq = 'M'
rs = ser.resample(freq)
result = getattr(rs, resample_method)()
if resample_method == 'ohlc':
    expected = DataFrame([], index=ser.index[:0].copy(), columns=['open', 'high', 'low', 'close'])
    expected.index = _asfreq_compat(ser.index, freq)
    tm.assert_frame_equal(result, expected, check_dtype=False)
else:
    expected = ser.copy()
    expected.index = _asfreq_compat(ser.index, freq)
    tm.assert_series_equal(result, expected, check_dtype=False)
tm.assert_index_equal(result.index, expected.index)
assert result.index.freq == expected.index.freq
```

## Next Steps


---

*Source: test_base.py:108 | Complexity: Advanced | Last updated: 2026-06-02*