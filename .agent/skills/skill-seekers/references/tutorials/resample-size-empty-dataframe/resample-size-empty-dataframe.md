# How To: Resample Size Empty Dataframe

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test resample size empty dataframe

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
# Fixtures: freq, empty_frame_dti
```

## Step-by-Step Guide

### Step 1: Assign unknown = value

```python
empty_frame_dti['a'] = []
```

### Step 2: Assign result = empty_frame_dti.resample.size(...)

```python
result = empty_frame_dti.resample(freq).size()
```

### Step 3: Assign index = _asfreq_compat(...)

```python
index = _asfreq_compat(empty_frame_dti.index, freq)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([], dtype='int64', index=index)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign msg = "Resampling on a TimedeltaIndex requires fixed-duration `freq`, e.g. '24h' or '3D', not <MonthEnd>"

```python
msg = "Resampling on a TimedeltaIndex requires fixed-duration `freq`, e.g. '24h' or '3D', not <MonthEnd>"
```

### Step 7: Call empty_frame_dti.resample()

```python
empty_frame_dti.resample(freq)
```

### Step 8: Assign freq = 'M'

```python
freq = 'M'
```


## Complete Example

```python
# Setup
# Fixtures: freq, empty_frame_dti

# Workflow
empty_frame_dti['a'] = []
if freq == 'ME' and isinstance(empty_frame_dti.index, TimedeltaIndex):
    msg = "Resampling on a TimedeltaIndex requires fixed-duration `freq`, e.g. '24h' or '3D', not <MonthEnd>"
    with pytest.raises(ValueError, match=msg):
        empty_frame_dti.resample(freq)
    return
elif freq == 'ME' and isinstance(empty_frame_dti.index, PeriodIndex):
    freq = 'M'
result = empty_frame_dti.resample(freq).size()
index = _asfreq_compat(empty_frame_dti.index, freq)
expected = Series([], dtype='int64', index=index)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_base.py:295 | Complexity: Advanced | Last updated: 2026-06-02*