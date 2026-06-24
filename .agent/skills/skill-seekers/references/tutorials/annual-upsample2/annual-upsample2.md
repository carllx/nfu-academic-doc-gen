# How To: Annual Upsample2

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test annual upsample2

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign rng = period_range(...)

```python
rng = period_range('2000', '2003', freq='Y-DEC')
```

### Step 2: Assign ts = Series(...)

```python
ts = Series([1, 2, 3, 4], index=rng)
```

### Step 3: Assign result = ts.resample.ffill(...)

```python
result = ts.resample('M').ffill()
```

### Step 4: Assign ex_index = period_range(...)

```python
ex_index = period_range('2000-01', '2003-12', freq='M')
```

### Step 5: Assign expected = ts.asfreq.reindex(...)

```python
expected = ts.asfreq('M', how='start').reindex(ex_index, method='ffill')
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
rng = period_range('2000', '2003', freq='Y-DEC')
ts = Series([1, 2, 3, 4], index=rng)
result = ts.resample('M').ffill()
ex_index = period_range('2000-01', '2003-12', freq='M')
expected = ts.asfreq('M', how='start').reindex(ex_index, method='ffill')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_period_index.py:207 | Complexity: Intermediate | Last updated: 2026-06-02*