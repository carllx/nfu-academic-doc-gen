# How To: Quarterly Upsample

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test quarterly upsample

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
# Fixtures: month, offset, period, convention, simple_period_range_series
```

## Step-by-Step Guide

### Step 1: Assign freq = value

```python
freq = f'Q-{month}'
```

### Step 2: Assign ts = simple_period_range_series(...)

```python
ts = simple_period_range_series('1/1/1990', '12/31/1995', freq=freq)
```

### Step 3: Assign warn = value

```python
warn = FutureWarning if period == 'B' else None
```

### Step 4: Assign msg = 'PeriodDtype\\[B\\] is deprecated'

```python
msg = 'PeriodDtype\\[B\\] is deprecated'
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign result = ts.resample.ffill(...)

```python
result = ts.resample(period, convention=convention).ffill()
```

### Step 7: Assign expected = result.to_timestamp(...)

```python
expected = result.to_timestamp(period, how=convention)
```

### Step 8: Assign expected = expected.asfreq.to_period(...)

```python
expected = expected.asfreq(offset, 'ffill').to_period()
```


## Complete Example

```python
# Setup
# Fixtures: month, offset, period, convention, simple_period_range_series

# Workflow
freq = f'Q-{month}'
ts = simple_period_range_series('1/1/1990', '12/31/1995', freq=freq)
warn = FutureWarning if period == 'B' else None
msg = 'PeriodDtype\\[B\\] is deprecated'
with tm.assert_produces_warning(warn, match=msg):
    result = ts.resample(period, convention=convention).ffill()
    expected = result.to_timestamp(period, how=convention)
    expected = expected.asfreq(offset, 'ffill').to_period()
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_period_index.py:222 | Complexity: Advanced | Last updated: 2026-06-02*