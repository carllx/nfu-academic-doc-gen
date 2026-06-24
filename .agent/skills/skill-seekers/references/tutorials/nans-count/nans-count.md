# How To: Nans Count

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test nans count

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.tseries`


## Step-by-Step Guide

### Step 1: Assign obj = Series(...)

```python
obj = Series(np.random.default_rng(2).standard_normal(50))
```

### Step 2: Assign unknown = value

```python
obj[:10] = np.nan
```

### Step 3: Assign unknown = value

```python
obj[-10:] = np.nan
```

### Step 4: Assign result = obj.rolling.count(...)

```python
result = obj.rolling(50, min_periods=30).count()
```

### Step 5: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result.iloc[-1], np.isfinite(obj[10:-10]).astype(float).sum())
```


## Complete Example

```python
# Workflow
obj = Series(np.random.default_rng(2).standard_normal(50))
obj[:10] = np.nan
obj[-10:] = np.nan
result = obj.rolling(50, min_periods=30).count()
tm.assert_almost_equal(result.iloc[-1], np.isfinite(obj[10:-10]).astype(float).sum())
```

## Next Steps


---

*Source: test_rolling_functions.py:178 | Complexity: Intermediate | Last updated: 2026-06-02*