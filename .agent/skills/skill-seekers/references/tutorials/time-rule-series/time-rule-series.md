# How To: Time Rule Series

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test time rule series

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
# Fixtures: series, q
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

### Step 3: Assign ser = unknown.resample.mean(...)

```python
ser = series[::2].resample('B').mean()
```

### Step 4: Assign series_result = ser.rolling.quantile(...)

```python
series_result = ser.rolling(window=win, min_periods=10).quantile(q)
```

### Step 5: Assign last_date = value

```python
last_date = series_result.index[-1]
```

### Step 6: Assign prev_date = value

```python
prev_date = last_date - 24 * offsets.BDay()
```

### Step 7: Assign trunc_series = unknown.truncate(...)

```python
trunc_series = series[::2].truncate(prev_date, last_date)
```

### Step 8: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(series_result.iloc[-1], compare_func(trunc_series))
```


## Complete Example

```python
# Setup
# Fixtures: series, q

# Workflow
compare_func = partial(scoreatpercentile, per=q)
win = 25
ser = series[::2].resample('B').mean()
series_result = ser.rolling(window=win, min_periods=10).quantile(q)
last_date = series_result.index[-1]
prev_date = last_date - 24 * offsets.BDay()
trunc_series = series[::2].truncate(prev_date, last_date)
tm.assert_almost_equal(series_result.iloc[-1], compare_func(trunc_series))
```

## Next Steps


---

*Source: test_rolling_quantile.py:59 | Complexity: Advanced | Last updated: 2026-06-02*