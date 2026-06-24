# How To: Map Na Ignore

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test map na ignore

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: float_frame
```

## Step-by-Step Guide

### Step 1: Assign strlen_frame = float_frame.map(...)

```python
strlen_frame = float_frame.map(lambda x: len(str(x)))
```

### Step 2: Assign float_frame_with_na = float_frame.copy(...)

```python
float_frame_with_na = float_frame.copy()
```

### Step 3: Assign mask = np.random.default_rng.integers(...)

```python
mask = np.random.default_rng(2).integers(0, 2, size=float_frame.shape, dtype=bool)
```

### Step 4: Assign unknown = value

```python
float_frame_with_na[mask] = pd.NA
```

### Step 5: Assign strlen_frame_na_ignore = float_frame_with_na.map(...)

```python
strlen_frame_na_ignore = float_frame_with_na.map(lambda x: len(str(x)), na_action='ignore')
```

### Step 6: Assign strlen_frame_with_na = strlen_frame.copy.astype(...)

```python
strlen_frame_with_na = strlen_frame.copy().astype('float64')
```

### Step 7: Assign unknown = value

```python
strlen_frame_with_na[mask] = pd.NA
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(strlen_frame_na_ignore, strlen_frame_with_na)
```


## Complete Example

```python
# Setup
# Fixtures: float_frame

# Workflow
strlen_frame = float_frame.map(lambda x: len(str(x)))
float_frame_with_na = float_frame.copy()
mask = np.random.default_rng(2).integers(0, 2, size=float_frame.shape, dtype=bool)
float_frame_with_na[mask] = pd.NA
strlen_frame_na_ignore = float_frame_with_na.map(lambda x: len(str(x)), na_action='ignore')
strlen_frame_with_na = strlen_frame.copy().astype('float64')
strlen_frame_with_na[mask] = pd.NA
tm.assert_frame_equal(strlen_frame_na_ignore, strlen_frame_with_na)
```

## Next Steps


---

*Source: test_map.py:107 | Complexity: Advanced | Last updated: 2026-06-02*