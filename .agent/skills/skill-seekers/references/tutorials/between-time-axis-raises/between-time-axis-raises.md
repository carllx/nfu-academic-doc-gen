# How To: Between Time Axis Raises

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test between time axis raises

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: axis
```

## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('1/1/2000', periods=100, freq='10min')
```

### Step 2: Assign mask = np.arange(...)

```python
mask = np.arange(0, len(rng))
```

### Step 3: Assign rand_data = np.random.default_rng.standard_normal(...)

```python
rand_data = np.random.default_rng(2).standard_normal((len(rng), len(rng)))
```

### Step 4: Assign ts = DataFrame(...)

```python
ts = DataFrame(rand_data, index=rng, columns=rng)
```

### Step 5: Assign unknown = value

```python
stime, etime = ('08:00:00', '09:00:00')
```

### Step 6: Assign msg = 'Index must be DatetimeIndex'

```python
msg = 'Index must be DatetimeIndex'
```

### Step 7: Assign ts.index = mask

```python
ts.index = mask
```

### Step 8: Assign ts.columns = mask

```python
ts.columns = mask
```

### Step 9: Call ts.between_time()

```python
ts.between_time(stime, etime)
```

### Step 10: Call ts.between_time()

```python
ts.between_time(stime, etime, axis=0)
```

### Step 11: Call ts.between_time()

```python
ts.between_time(stime, etime, axis=1)
```


## Complete Example

```python
# Setup
# Fixtures: axis

# Workflow
rng = date_range('1/1/2000', periods=100, freq='10min')
mask = np.arange(0, len(rng))
rand_data = np.random.default_rng(2).standard_normal((len(rng), len(rng)))
ts = DataFrame(rand_data, index=rng, columns=rng)
stime, etime = ('08:00:00', '09:00:00')
msg = 'Index must be DatetimeIndex'
if axis in ['columns', 1]:
    ts.index = mask
    with pytest.raises(TypeError, match=msg):
        ts.between_time(stime, etime)
    with pytest.raises(TypeError, match=msg):
        ts.between_time(stime, etime, axis=0)
if axis in ['index', 0]:
    ts.columns = mask
    with pytest.raises(TypeError, match=msg):
        ts.between_time(stime, etime, axis=1)
```

## Next Steps


---

*Source: test_between_time.py:179 | Complexity: Advanced | Last updated: 2026-06-02*