# How To: Resample Nat Index Series

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test resample nat index series

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
# Fixtures: freq, series, resample_method
```

## Step-by-Step Guide

### Step 1: Assign ser = series.copy(...)

```python
ser = series.copy()
```

**Verification:**
```python
assert result.index.freq == expected.index.freq
```

### Step 2: Assign ser.index = PeriodIndex(...)

```python
ser.index = PeriodIndex([NaT] * len(ser), freq=freq)
```

### Step 3: Assign rs = ser.resample(...)

```python
rs = ser.resample(freq)
```

### Step 4: Assign result = getattr(...)

```python
result = getattr(rs, resample_method)()
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result.index, expected.index)
```

**Verification:**
```python
assert result.index.freq == expected.index.freq
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame([], index=ser.index[:0].copy(), columns=['open', 'high', 'low', 'close'])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected, check_dtype=False)
```

### Step 8: Assign expected = unknown.copy(...)

```python
expected = ser[:0].copy()
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected, check_dtype=False)
```


## Complete Example

```python
# Setup
# Fixtures: freq, series, resample_method

# Workflow
ser = series.copy()
ser.index = PeriodIndex([NaT] * len(ser), freq=freq)
rs = ser.resample(freq)
result = getattr(rs, resample_method)()
if resample_method == 'ohlc':
    expected = DataFrame([], index=ser.index[:0].copy(), columns=['open', 'high', 'low', 'close'])
    tm.assert_frame_equal(result, expected, check_dtype=False)
else:
    expected = ser[:0].copy()
    tm.assert_series_equal(result, expected, check_dtype=False)
tm.assert_index_equal(result.index, expected.index)
assert result.index.freq == expected.index.freq
```

## Next Steps


---

*Source: test_base.py:175 | Complexity: Advanced | Last updated: 2026-06-02*