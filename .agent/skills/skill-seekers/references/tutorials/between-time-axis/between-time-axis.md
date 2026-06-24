# How To: Between Time Axis

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test between time axis

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
# Fixtures: frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('1/1/2000', periods=100, freq='10min')
```

**Verification:**
```python
assert len(ts.between_time(stime, etime)) == expected_length
```

### Step 2: Assign ts = Series(...)

```python
ts = Series(np.random.default_rng(2).standard_normal(len(rng)), index=rng)
```

**Verification:**
```python
assert len(ts.between_time(stime, etime, axis=0)) == expected_length
```

### Step 3: Assign unknown = value

```python
stime, etime = ('08:00:00', '09:00:00')
```

### Step 4: Assign expected_length = 7

```python
expected_length = 7
```

**Verification:**
```python
assert len(ts.between_time(stime, etime)) == expected_length
```

### Step 5: Assign msg = value

```python
msg = f'No axis named {ts.ndim} for object type {type(ts).__name__}'
```

### Step 6: Assign ts = ts.to_frame(...)

```python
ts = ts.to_frame()
```

### Step 7: Call ts.between_time()

```python
ts.between_time(stime, etime, axis=ts.ndim)
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series

# Workflow
rng = date_range('1/1/2000', periods=100, freq='10min')
ts = Series(np.random.default_rng(2).standard_normal(len(rng)), index=rng)
if frame_or_series is DataFrame:
    ts = ts.to_frame()
stime, etime = ('08:00:00', '09:00:00')
expected_length = 7
assert len(ts.between_time(stime, etime)) == expected_length
assert len(ts.between_time(stime, etime, axis=0)) == expected_length
msg = f'No axis named {ts.ndim} for object type {type(ts).__name__}'
with pytest.raises(ValueError, match=msg):
    ts.between_time(stime, etime, axis=ts.ndim)
```

## Next Steps


---

*Source: test_between_time.py:146 | Complexity: Intermediate | Last updated: 2026-06-02*