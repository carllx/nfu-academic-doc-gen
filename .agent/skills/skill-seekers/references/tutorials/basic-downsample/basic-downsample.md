# How To: Basic Downsample

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test basic downsample

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
# Fixtures: simple_period_range_series
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

### Step 3: Assign expected = ts.groupby.mean(...)

```python
expected = ts.groupby(ts.index.year).mean()
```

### Step 4: Assign expected.index = period_range(...)

```python
expected.index = period_range('1/1/1990', '6/30/1995', freq='Y-DEC')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ts.resample('Y-DEC').mean(), result)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ts.resample('Y').mean(), result)
```


## Complete Example

```python
# Setup
# Fixtures: simple_period_range_series

# Workflow
ts = simple_period_range_series('1/1/1990', '6/30/1995', freq='M')
result = ts.resample('Y-DEC').mean()
expected = ts.groupby(ts.index.year).mean()
expected.index = period_range('1/1/1990', '6/30/1995', freq='Y-DEC')
tm.assert_series_equal(result, expected)
tm.assert_series_equal(ts.resample('Y-DEC').mean(), result)
tm.assert_series_equal(ts.resample('Y').mean(), result)
```

## Next Steps


---

*Source: test_period_index.py:151 | Complexity: Intermediate | Last updated: 2026-06-02*