# How To: Time Rule Frame

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test time rule frame

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `functools`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tseries`

**Setup Required:**
```python
# Fixtures: raw, frame, q
```

## Step-by-Step Guide

### Step 1: Assign compare_func = partial(...)

```python
compare_func = partial(scoreatpercentile, per=q)
```

### Step 2: Assign win = 25

```python
win = 25
```

### Step 3: Assign frm = unknown.resample.mean(...)

```python
frm = frame[::2].resample('B').mean()
```

### Step 4: Assign frame_result = frm.rolling.quantile(...)

```python
frame_result = frm.rolling(window=win, min_periods=10).quantile(q)
```

### Step 5: Assign last_date = value

```python
last_date = frame_result.index[-1]
```

### Step 6: Assign prev_date = value

```python
prev_date = last_date - 24 * offsets.BDay()
```

### Step 7: Assign trunc_frame = unknown.truncate(...)

```python
trunc_frame = frame[::2].truncate(prev_date, last_date)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(frame_result.xs(last_date), trunc_frame.apply(compare_func, raw=raw), check_names=False)
```


## Complete Example

```python
# Setup
# Fixtures: raw, frame, q

# Workflow
compare_func = partial(scoreatpercentile, per=q)
win = 25
frm = frame[::2].resample('B').mean()
frame_result = frm.rolling(window=win, min_periods=10).quantile(q)
last_date = frame_result.index[-1]
prev_date = last_date - 24 * offsets.BDay()
trunc_frame = frame[::2].truncate(prev_date, last_date)
tm.assert_series_equal(frame_result.xs(last_date), trunc_frame.apply(compare_func, raw=raw), check_names=False)
```

## Next Steps


---

*Source: test_rolling_quantile.py:72 | Complexity: Advanced | Last updated: 2026-06-02*