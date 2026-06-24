# How To: Ewma With Times Variable Spacing

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ewma with times variable spacing

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz_aware_fixture, unit
```

## Step-by-Step Guide

### Step 1: Assign tz = tz_aware_fixture

```python
tz = tz_aware_fixture
```

### Step 2: Assign halflife = '23 days'

```python
halflife = '23 days'
```

### Step 3: Assign times = DatetimeIndex.tz_localize.as_unit(...)

```python
times = DatetimeIndex(['2020-01-01', '2020-01-10T00:04:05', '2020-02-23T05:00:23']).tz_localize(tz).as_unit(unit)
```

### Step 4: Assign data = np.arange(...)

```python
data = np.arange(3)
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame(data)
```

### Step 6: Assign result = df.ewm.mean(...)

```python
result = df.ewm(halflife=halflife, times=times).mean()
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame([0.0, 0.5674161888241773, 1.545239952073459])
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tz_aware_fixture, unit

# Workflow
tz = tz_aware_fixture
halflife = '23 days'
times = DatetimeIndex(['2020-01-01', '2020-01-10T00:04:05', '2020-02-23T05:00:23']).tz_localize(tz).as_unit(unit)
data = np.arange(3)
df = DataFrame(data)
result = df.ewm(halflife=halflife, times=times).mean()
expected = DataFrame([0.0, 0.5674161888241773, 1.545239952073459])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_ewm.py:105 | Complexity: Advanced | Last updated: 2026-06-02*