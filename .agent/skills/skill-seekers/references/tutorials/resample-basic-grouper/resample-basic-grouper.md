# How To: Resample Basic Grouper

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test resample basic grouper

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `functools`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas._typing`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`
- `pandas.core.indexes.datetimes`
- `pandas.core.indexes.period`
- `pandas.core.resample`
- `pandas.tseries`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: series, unit
```

## Step-by-Step Guide

### Step 1: Assign s = series

```python
s = series
```

### Step 2: Assign s.index = s.index.as_unit(...)

```python
s.index = s.index.as_unit(unit)
```

### Step 3: Assign result = s.resample.last(...)

```python
result = s.resample('5Min').last()
```

### Step 4: Assign grouper = Grouper(...)

```python
grouper = Grouper(freq=Minute(5), closed='left', label='left')
```

### Step 5: Assign expected = s.groupby.agg(...)

```python
expected = s.groupby(grouper).agg(lambda x: x.iloc[-1])
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: series, unit

# Workflow
s = series
s.index = s.index.as_unit(unit)
result = s.resample('5Min').last()
grouper = Grouper(freq=Minute(5), closed='left', label='left')
expected = s.groupby(grouper).agg(lambda x: x.iloc[-1])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_datetime_index.py:178 | Complexity: Intermediate | Last updated: 2026-06-02*