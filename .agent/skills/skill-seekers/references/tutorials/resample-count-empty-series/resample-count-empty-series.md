# How To: Resample Count Empty Series

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test resample count empty series

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

### Step 2: Assign rs = ser.resample(...)

```python
rs = ser.resample(freq)
```

### Step 3: Assign result = getattr(...)

```python
result = getattr(rs, resample_method)()
```

### Step 4: Assign index = _asfreq_compat(...)

```python
index = _asfreq_compat(ser.index, freq)
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([], dtype='int64', index=index, name=ser.name)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign msg = "Resampling on a TimedeltaIndex requires fixed-duration `freq`, e.g. '24h' or '3D', not <MonthEnd>"

```python
msg = "Resampling on a TimedeltaIndex requires fixed-duration `freq`, e.g. '24h' or '3D', not <MonthEnd>"
```

### Step 8: Call ser.resample()

```python
ser.resample(freq)
```

### Step 9: Assign freq = 'M'

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
index = _asfreq_compat(ser.index, freq)
expected = Series([], dtype='int64', index=index, name=ser.name)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_base.py:199 | Complexity: Advanced | Last updated: 2026-06-02*