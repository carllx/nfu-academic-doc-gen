# How To: Center

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test center

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
# Fixtures: q
```

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

### Step 4: Assign result = obj.rolling.quantile(...)

```python
result = obj.rolling(20, center=True).quantile(q)
```

### Step 5: Assign expected = unknown.reset_index(...)

```python
expected = concat([obj, Series([np.nan] * 9)]).rolling(20).quantile(q).iloc[9:].reset_index(drop=True)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: q

# Workflow
obj = Series(np.random.default_rng(2).standard_normal(50))
obj[:10] = np.nan
obj[-10:] = np.nan
result = obj.rolling(20, center=True).quantile(q)
expected = concat([obj, Series([np.nan] * 9)]).rolling(20).quantile(q).iloc[9:].reset_index(drop=True)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_rolling_quantile.py:129 | Complexity: Intermediate | Last updated: 2026-06-02*