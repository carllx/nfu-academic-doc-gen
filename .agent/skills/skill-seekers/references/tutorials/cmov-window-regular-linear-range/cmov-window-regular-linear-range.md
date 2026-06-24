# How To: Cmov Window Regular Linear Range

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cmov window regular linear range

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
# Fixtures: win_types, step
```

## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('scipy')
```

### Step 2: Assign vals = np.array(...)

```python
vals = np.array(range(10), dtype=float)
```

### Step 3: Assign xp = vals.copy(...)

```python
xp = vals.copy()
```

### Step 4: Assign unknown = value

```python
xp[:2] = np.nan
```

### Step 5: Assign unknown = value

```python
xp[-2:] = np.nan
```

### Step 6: Assign xp = value

```python
xp = Series(xp)[::step]
```

### Step 7: Assign rs = Series.rolling.mean(...)

```python
rs = Series(vals).rolling(5, win_type=win_types, center=True, step=step).mean()
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(xp, rs)
```


## Complete Example

```python
# Setup
# Fixtures: win_types, step

# Workflow
pytest.importorskip('scipy')
vals = np.array(range(10), dtype=float)
xp = vals.copy()
xp[:2] = np.nan
xp[-2:] = np.nan
xp = Series(xp)[::step]
rs = Series(vals).rolling(5, win_type=win_types, center=True, step=step).mean()
tm.assert_series_equal(xp, rs)
```

## Next Steps


---

*Source: test_win_type.py:444 | Complexity: Advanced | Last updated: 2026-06-02*