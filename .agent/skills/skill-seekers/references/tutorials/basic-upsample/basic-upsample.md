# How To: Basic Upsample

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test basic upsample

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `warnings`
- `dateutil`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs.ccalendar`
- `pandas._libs.tslibs.period`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.datetimes`
- `pandas.core.indexes.period`
- `pandas.core.resample`
- `pandas.tseries`

**Setup Required:**
```python
# Fixtures: freq, simple_period_range_series
```

## Step-by-Step Guide

### Step 1: Assign ts = simple_period_range_series(...)

```python
ts = simple_period_range_series('1/1/1990', '6/30/1995', freq='M')
```

### Step 2: Assign result = ts.resample.mean(...)

```python
result = ts.resample('Y-DEC').mean()
```

### Step 3: Assign resampled = result.resample.ffill(...)

```python
resampled = result.resample(freq, convention='end').ffill()
```

### Step 4: Assign expected = result.to_timestamp(...)

```python
expected = result.to_timestamp(freq, how='end')
```

### Step 5: Assign expected = expected.asfreq.to_period(...)

```python
expected = expected.asfreq(freq, 'ffill').to_period(freq)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(resampled, expected)
```


## Complete Example

```python
# Setup
# Fixtures: freq, simple_period_range_series

# Workflow
ts = simple_period_range_series('1/1/1990', '6/30/1995', freq='M')
result = ts.resample('Y-DEC').mean()
resampled = result.resample(freq, convention='end').ffill()
expected = result.to_timestamp(freq, how='end')
expected = expected.asfreq(freq, 'ffill').to_period(freq)
tm.assert_series_equal(resampled, expected)
```

## Next Steps


---

*Source: test_period_index.py:183 | Complexity: Intermediate | Last updated: 2026-06-02*