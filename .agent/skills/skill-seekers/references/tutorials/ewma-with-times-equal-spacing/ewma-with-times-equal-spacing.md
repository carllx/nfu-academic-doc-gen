# How To: Ewma With Times Equal Spacing

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test ewma with times equal spacing

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: halflife_with_times, times, min_periods
```

## Step-by-Step Guide

### Step 1: Assign halflife = halflife_with_times

```python
halflife = halflife_with_times
```

### Step 2: Assign data = np.arange(...)

```python
data = np.arange(10.0)
```

### Step 3: Assign unknown = value

```python
data[::2] = np.nan
```

### Step 4: Assign df = DataFrame(...)

```python
df = DataFrame({'A': data})
```

### Step 5: Assign result = df.ewm.mean(...)

```python
result = df.ewm(halflife=halflife, min_periods=min_periods, times=times).mean()
```

### Step 6: Assign expected = df.ewm.mean(...)

```python
expected = df.ewm(halflife=1.0, min_periods=min_periods).mean()
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: halflife_with_times, times, min_periods

# Workflow
halflife = halflife_with_times
data = np.arange(10.0)
data[::2] = np.nan
df = DataFrame({'A': data})
result = df.ewm(halflife=halflife, min_periods=min_periods, times=times).mean()
expected = df.ewm(halflife=1.0, min_periods=min_periods).mean()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_ewm.py:95 | Complexity: Intermediate | Last updated: 2026-06-02*