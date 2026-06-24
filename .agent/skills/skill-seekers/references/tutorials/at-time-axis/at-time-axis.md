# How To: At Time Axis

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test at time axis

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: axis
```

## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('1/1/2000', '1/5/2000', freq='5min')
```

### Step 2: Assign ts = DataFrame(...)

```python
ts = DataFrame(np.random.default_rng(2).standard_normal((len(rng), len(rng))))
```

### Step 3: Assign unknown = value

```python
ts.index, ts.columns = (rng, rng)
```

### Step 4: Assign indices = value

```python
indices = rng[(rng.hour == 9) & (rng.minute == 30) & (rng.second == 0)]
```

### Step 5: Assign result = ts.at_time(...)

```python
result = ts.at_time('9:30', axis=axis)
```

### Step 6: Assign result.index = result.index._with_freq(...)

```python
result.index = result.index._with_freq(None)
```

### Step 7: Assign expected.index = expected.index._with_freq(...)

```python
expected.index = expected.index._with_freq(None)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign expected = value

```python
expected = ts.loc[indices, :]
```

### Step 10: Assign expected = value

```python
expected = ts.loc[:, indices]
```


## Complete Example

```python
# Setup
# Fixtures: axis

# Workflow
rng = date_range('1/1/2000', '1/5/2000', freq='5min')
ts = DataFrame(np.random.default_rng(2).standard_normal((len(rng), len(rng))))
ts.index, ts.columns = (rng, rng)
indices = rng[(rng.hour == 9) & (rng.minute == 30) & (rng.second == 0)]
if axis in ['index', 0]:
    expected = ts.loc[indices, :]
elif axis in ['columns', 1]:
    expected = ts.loc[:, indices]
result = ts.at_time('9:30', axis=axis)
result.index = result.index._with_freq(None)
expected.index = expected.index._with_freq(None)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_at_time.py:99 | Complexity: Advanced | Last updated: 2026-06-02*