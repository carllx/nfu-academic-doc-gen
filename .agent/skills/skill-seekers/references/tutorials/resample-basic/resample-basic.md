# How To: Resample Basic

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test resample basic

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
# Fixtures: series, closed, expected, unit
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

### Step 3: Assign expected = expected(...)

```python
expected = expected(s)
```

### Step 4: Assign expected.index = expected.index.as_unit(...)

```python
expected.index = expected.index.as_unit(unit)
```

### Step 5: Assign result = s.resample.mean(...)

```python
result = s.resample('5min', closed=closed, label='right').mean()
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: series, closed, expected, unit

# Workflow
s = series
s.index = s.index.as_unit(unit)
expected = expected(s)
expected.index = expected.index.as_unit(unit)
result = s.resample('5min', closed=closed, label='right').mean()
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_datetime_index.py:145 | Complexity: Intermediate | Last updated: 2026-06-02*