# How To: Min Periods

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test min periods

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `functools`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tseries`

**Setup Required:**
```python
# Fixtures: series, minp, q, step
```

## Step-by-Step Guide

### Step 1: Assign result = series.rolling.quantile(...)

```python
result = series.rolling(len(series) + 1, min_periods=minp, step=step).quantile(q)
```

### Step 2: Assign expected = series.rolling.quantile(...)

```python
expected = series.rolling(len(series), min_periods=minp, step=step).quantile(q)
```

### Step 3: Assign nan_mask = isna(...)

```python
nan_mask = isna(result)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(nan_mask, isna(expected))
```

### Step 5: Assign nan_mask = value

```python
nan_mask = ~nan_mask
```

### Step 6: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result[nan_mask], expected[nan_mask])
```


## Complete Example

```python
# Setup
# Fixtures: series, minp, q, step

# Workflow
result = series.rolling(len(series) + 1, min_periods=minp, step=step).quantile(q)
expected = series.rolling(len(series), min_periods=minp, step=step).quantile(q)
nan_mask = isna(result)
tm.assert_series_equal(nan_mask, isna(expected))
nan_mask = ~nan_mask
tm.assert_almost_equal(result[nan_mask], expected[nan_mask])
```

## Next Steps


---

*Source: test_rolling_quantile.py:118 | Complexity: Intermediate | Last updated: 2026-06-02*