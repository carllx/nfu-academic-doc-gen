# How To: Apply To Empty Series

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test apply to empty series

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
# Fixtures: empty_series_dti, freq
```

## Step-by-Step Guide

### Step 1: Assign ser = empty_series_dti

```python
ser = empty_series_dti
```

### Step 2: Assign result = ser.resample.apply(...)

```python
result = ser.resample(freq, group_keys=False).apply(lambda x: 1)
```

### Step 3: Assign expected = ser.resample.apply(...)

```python
expected = ser.resample(freq).apply('sum')
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected, check_dtype=False)
```

### Step 5: Assign msg = "Resampling on a TimedeltaIndex requires fixed-duration `freq`, e.g. '24h' or '3D', not <MonthEnd>"

```python
msg = "Resampling on a TimedeltaIndex requires fixed-duration `freq`, e.g. '24h' or '3D', not <MonthEnd>"
```

### Step 6: Call empty_series_dti.resample()

```python
empty_series_dti.resample(freq)
```

### Step 7: Assign freq = 'M'

```python
freq = 'M'
```


## Complete Example

```python
# Setup
# Fixtures: empty_series_dti, freq

# Workflow
ser = empty_series_dti
if freq == 'ME' and isinstance(empty_series_dti.index, TimedeltaIndex):
    msg = "Resampling on a TimedeltaIndex requires fixed-duration `freq`, e.g. '24h' or '3D', not <MonthEnd>"
    with pytest.raises(ValueError, match=msg):
        empty_series_dti.resample(freq)
    return
elif freq == 'ME' and isinstance(empty_series_dti.index, PeriodIndex):
    freq = 'M'
result = ser.resample(freq, group_keys=False).apply(lambda x: 1)
expected = ser.resample(freq).apply('sum')
tm.assert_series_equal(result, expected, check_dtype=False)
```

## Next Steps


---

*Source: test_base.py:345 | Complexity: Intermediate | Last updated: 2026-06-02*