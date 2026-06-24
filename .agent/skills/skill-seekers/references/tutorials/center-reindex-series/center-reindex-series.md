# How To: Center Reindex Series

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test center reindex series

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.tseries`

**Setup Required:**
```python
# Fixtures: series, roll_func, kwargs, minp, fill_value
```

## Step-by-Step Guide

### Step 1: Assign s = value

```python
s = [f'x{x:d}' for x in range(12)]
```

### Step 2: Assign series_xp = getattr.shift.reindex(...)

```python
series_xp = getattr(series.reindex(list(series.index) + s).rolling(window=25, min_periods=minp), roll_func)(**kwargs).shift(-12).reindex(series.index)
```

### Step 3: Assign series_rs = getattr(...)

```python
series_rs = getattr(series.rolling(window=25, min_periods=minp, center=True), roll_func)(**kwargs)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(series_xp, series_rs)
```

### Step 5: Assign series_xp = series_xp.fillna(...)

```python
series_xp = series_xp.fillna(fill_value)
```


## Complete Example

```python
# Setup
# Fixtures: series, roll_func, kwargs, minp, fill_value

# Workflow
s = [f'x{x:d}' for x in range(12)]
series_xp = getattr(series.reindex(list(series.index) + s).rolling(window=25, min_periods=minp), roll_func)(**kwargs).shift(-12).reindex(series.index)
series_rs = getattr(series.rolling(window=25, min_periods=minp, center=True), roll_func)(**kwargs)
if fill_value is not None:
    series_xp = series_xp.fillna(fill_value)
tm.assert_series_equal(series_xp, series_rs)
```

## Next Steps


---

*Source: test_rolling_functions.py:275 | Complexity: Intermediate | Last updated: 2026-06-02*