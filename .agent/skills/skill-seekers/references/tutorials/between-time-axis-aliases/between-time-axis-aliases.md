# How To: Between Time Axis Aliases

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test between time axis aliases

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

**Verification:**
```python
assert len(ts.between_time(stime, etime)) == exp_len
```

### Step 2: Assign ts = DataFrame(...)

```python
ts = DataFrame(np.random.default_rng(2).standard_normal((len(rng), len(rng))))
```

**Verification:**
```python
assert len(ts.between_time(stime, etime, axis=0)) == exp_len
```

### Step 3: Assign unknown = value

```python
stime, etime = ('08:00:00', '09:00:00')
```

**Verification:**
```python
assert len(selected) == exp_len
```

### Step 4: Assign exp_len = 7

```python
exp_len = 7
```

### Step 5: Assign ts.index = rng

```python
ts.index = rng
```

**Verification:**
```python
assert len(ts.between_time(stime, etime)) == exp_len
```

### Step 6: Assign ts.columns = rng

```python
ts.columns = rng
```

### Step 7: Assign selected = value

```python
selected = ts.between_time(stime, etime, axis=1).columns
```

**Verification:**
```python
assert len(selected) == exp_len
```


## Complete Example

```python
# Setup
# Fixtures: axis

# Workflow
rng = date_range('1/1/2000', periods=100, freq='10min')
ts = DataFrame(np.random.default_rng(2).standard_normal((len(rng), len(rng))))
stime, etime = ('08:00:00', '09:00:00')
exp_len = 7
if axis in ['index', 0]:
    ts.index = rng
    assert len(ts.between_time(stime, etime)) == exp_len
    assert len(ts.between_time(stime, etime, axis=0)) == exp_len
if axis in ['columns', 1]:
    ts.columns = rng
    selected = ts.between_time(stime, etime, axis=1).columns
    assert len(selected) == exp_len
```

## Next Steps


---

*Source: test_between_time.py:162 | Complexity: Intermediate | Last updated: 2026-06-02*