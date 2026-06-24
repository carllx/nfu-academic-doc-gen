# How To: Annual Upsample

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test annual upsample

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
ts = simple_period_range_series('1/1/1990', '12/31/1995', freq='Y-DEC')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'a': ts})
```

### Step 3: Assign rdf = df.resample.ffill(...)

```python
rdf = df.resample('D').ffill()
```

### Step 4: Assign exp = unknown.resample.ffill(...)

```python
exp = df['a'].resample('D').ffill()
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(rdf['a'], exp)
```


## Complete Example

```python
# Setup
# Fixtures: simple_period_range_series

# Workflow
ts = simple_period_range_series('1/1/1990', '12/31/1995', freq='Y-DEC')
df = DataFrame({'a': ts})
rdf = df.resample('D').ffill()
exp = df['a'].resample('D').ffill()
tm.assert_series_equal(rdf['a'], exp)
```

## Next Steps


---

*Source: test_period_index.py:200 | Complexity: Intermediate | Last updated: 2026-06-02*