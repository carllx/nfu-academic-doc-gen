# How To: Mode Extension Dtype

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test mode extension dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: as_period
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([pd.Timestamp(1979, 4, n) for n in range(1, 5)])
```

**Verification:**
```python
assert res.dtype == ser.dtype
```

### Step 2: Assign res = ser.mode(...)

```python
res = ser.mode()
```

**Verification:**
```python
assert res.dtype == ser.dtype
```

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, ser)
```

### Step 4: Assign ser = ser.dt.to_period(...)

```python
ser = ser.dt.to_period('D')
```

### Step 5: Assign ser = ser.dt.tz_localize(...)

```python
ser = ser.dt.tz_localize('US/Central')
```


## Complete Example

```python
# Setup
# Fixtures: as_period

# Workflow
ser = Series([pd.Timestamp(1979, 4, n) for n in range(1, 5)])
if as_period:
    ser = ser.dt.to_period('D')
else:
    ser = ser.dt.tz_localize('US/Central')
res = ser.mode()
assert res.dtype == ser.dtype
tm.assert_series_equal(res, ser)
```

## Next Steps


---

*Source: test_reductions.py:18 | Complexity: Intermediate | Last updated: 2026-06-02*