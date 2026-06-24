# How To: Annual Upsample Cases

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test annual upsample cases

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
# Fixtures: offset, period, conv, meth, month, simple_period_range_series
```

## Step-by-Step Guide

### Step 1: Assign ts = simple_period_range_series(...)

```python
ts = simple_period_range_series('1/1/1990', '12/31/1991', freq=f'Y-{month}')
```

### Step 2: Assign warn = value

```python
warn = FutureWarning if period == 'B' else None
```

### Step 3: Assign msg = 'PeriodDtype\\[B\\] is deprecated'

```python
msg = 'PeriodDtype\\[B\\] is deprecated'
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = getattr(...)

```python
result = getattr(ts.resample(period, convention=conv), meth)()
```

### Step 6: Assign expected = result.to_timestamp(...)

```python
expected = result.to_timestamp(period, how=conv)
```

### Step 7: Assign expected = expected.asfreq.to_period(...)

```python
expected = expected.asfreq(offset, meth).to_period()
```


## Complete Example

```python
# Setup
# Fixtures: offset, period, conv, meth, month, simple_period_range_series

# Workflow
ts = simple_period_range_series('1/1/1990', '12/31/1991', freq=f'Y-{month}')
warn = FutureWarning if period == 'B' else None
msg = 'PeriodDtype\\[B\\] is deprecated'
with tm.assert_produces_warning(warn, match=msg):
    result = getattr(ts.resample(period, convention=conv), meth)()
    expected = result.to_timestamp(period, how=conv)
    expected = expected.asfreq(offset, meth).to_period()
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_period_index.py:139 | Complexity: Intermediate | Last updated: 2026-06-02*