# How To: Upsample With Limit

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test upsample with limit

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
rng = period_range('1/1/2000', periods=5, freq='Y')
```

### Step 2: Assign ts = Series(...)

```python
ts = Series(np.random.default_rng(2).standard_normal(len(rng)), rng)
```

### Step 3: Assign result = ts.resample.ffill(...)

```python
result = ts.resample('M', convention='end').ffill(limit=2)
```

### Step 4: Assign expected = ts.asfreq.reindex(...)

```python
expected = ts.asfreq('M').reindex(result.index, method='ffill', limit=2)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
rng = period_range('1/1/2000', periods=5, freq='Y')
ts = Series(np.random.default_rng(2).standard_normal(len(rng)), rng)
result = ts.resample('M', convention='end').ffill(limit=2)
expected = ts.asfreq('M').reindex(result.index, method='ffill', limit=2)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_period_index.py:192 | Complexity: Intermediate | Last updated: 2026-06-02*