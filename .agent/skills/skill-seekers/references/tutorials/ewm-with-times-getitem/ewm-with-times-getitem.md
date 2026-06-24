# How To: Ewm With Times Getitem

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ewm with times getitem

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: halflife_with_times
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

### Step 4: Assign times = date_range(...)

```python
times = date_range('2000', freq='D', periods=10)
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame({'A': data, 'B': data})
```

### Step 6: Assign result = unknown.mean(...)

```python
result = df.ewm(halflife=halflife, times=times)['A'].mean()
```

### Step 7: Assign expected = unknown.mean(...)

```python
expected = df.ewm(halflife=1.0)['A'].mean()
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: halflife_with_times

# Workflow
halflife = halflife_with_times
data = np.arange(10.0)
data[::2] = np.nan
times = date_range('2000', freq='D', periods=10)
df = DataFrame({'A': data, 'B': data})
result = df.ewm(halflife=halflife, times=times)['A'].mean()
expected = df.ewm(halflife=1.0)['A'].mean()
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_ewm.py:128 | Complexity: Advanced | Last updated: 2026-06-02*