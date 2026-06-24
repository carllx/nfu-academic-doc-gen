# How To: Cmov Window Frame

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test cmov window frame

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
# Fixtures: f, xp, step
```

## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('scipy')
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.array([[12.18, 3.64], [10.18, 9.16], [13.24, 14.61], [4.51, 8.11], [6.15, 11.44], [9.14, 6.21], [11.31, 10.67], [2.94, 6.51], [9.42, 8.39], [12.44, 7.34]]))
```

### Step 3: Assign xp = value

```python
xp = DataFrame(np.array(xp))[::step]
```

### Step 4: Assign roll = df.rolling(...)

```python
roll = df.rolling(5, win_type='boxcar', center=True, step=step)
```

### Step 5: Assign rs = getattr(...)

```python
rs = getattr(roll, f)()
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(xp, rs)
```


## Complete Example

```python
# Setup
# Fixtures: f, xp, step

# Workflow
pytest.importorskip('scipy')
df = DataFrame(np.array([[12.18, 3.64], [10.18, 9.16], [13.24, 14.61], [4.51, 8.11], [6.15, 11.44], [9.14, 6.21], [11.31, 10.67], [2.94, 6.51], [9.42, 8.39], [12.44, 7.34]]))
xp = DataFrame(np.array(xp))[::step]
roll = df.rolling(5, win_type='boxcar', center=True, step=step)
rs = getattr(roll, f)()
tm.assert_frame_equal(xp, rs)
```

## Next Steps


---

*Source: test_win_type.py:295 | Complexity: Intermediate | Last updated: 2026-06-02*