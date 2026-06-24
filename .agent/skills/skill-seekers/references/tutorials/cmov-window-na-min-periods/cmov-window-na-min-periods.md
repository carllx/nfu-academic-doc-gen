# How To: Cmov Window Na Min Periods

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test cmov window na min periods

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.api.indexers`

**Setup Required:**
```python
# Fixtures: step, min_periods
```

## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('scipy')
```

### Step 2: Assign vals = Series(...)

```python
vals = Series(np.random.default_rng(2).standard_normal(10))
```

### Step 3: Assign unknown = value

```python
vals[4] = np.nan
```

### Step 4: Assign unknown = value

```python
vals[8] = np.nan
```

### Step 5: Assign xp = vals.rolling.mean(...)

```python
xp = vals.rolling(5, min_periods=min_periods, center=True, step=step).mean()
```

### Step 6: Assign rs = vals.rolling.mean(...)

```python
rs = vals.rolling(5, win_type='boxcar', min_periods=min_periods, center=True, step=step).mean()
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(xp, rs)
```


## Complete Example

```python
# Setup
# Fixtures: step, min_periods

# Workflow
pytest.importorskip('scipy')
vals = Series(np.random.default_rng(2).standard_normal(10))
vals[4] = np.nan
vals[8] = np.nan
xp = vals.rolling(5, min_periods=min_periods, center=True, step=step).mean()
rs = vals.rolling(5, win_type='boxcar', min_periods=min_periods, center=True, step=step).mean()
tm.assert_series_equal(xp, rs)
```

## Next Steps


---

*Source: test_win_type.py:323 | Complexity: Intermediate | Last updated: 2026-06-02*