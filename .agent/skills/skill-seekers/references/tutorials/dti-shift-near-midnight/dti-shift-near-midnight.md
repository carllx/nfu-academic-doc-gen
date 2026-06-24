# How To: Dti Shift Near Midnight

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dti shift near midnight

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `pytest`
- `pytz`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: shift, result_time, unit
```

## Step-by-Step Guide

### Step 1: Assign dt = datetime(...)

```python
dt = datetime(2014, 11, 14, 0)
```

### Step 2: Assign dt_est = pytz.timezone.localize(...)

```python
dt_est = pytz.timezone('EST').localize(dt)
```

### Step 3: Assign idx = DatetimeIndex.as_unit(...)

```python
idx = DatetimeIndex([dt_est]).as_unit(unit)
```

### Step 4: Assign ser = Series(...)

```python
ser = Series(data=[1], index=idx)
```

### Step 5: Assign result = ser.shift(...)

```python
result = ser.shift(shift, freq='h')
```

### Step 6: Assign exp_index = DatetimeIndex.as_unit(...)

```python
exp_index = DatetimeIndex([result_time], tz='EST').as_unit(unit)
```

### Step 7: Assign expected = Series(...)

```python
expected = Series(1, index=exp_index)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: shift, result_time, unit

# Workflow
dt = datetime(2014, 11, 14, 0)
dt_est = pytz.timezone('EST').localize(dt)
idx = DatetimeIndex([dt_est]).as_unit(unit)
ser = Series(data=[1], index=idx)
result = ser.shift(shift, freq='h')
exp_index = DatetimeIndex([result_time], tz='EST').as_unit(unit)
expected = Series(1, index=exp_index)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_shift.py:123 | Complexity: Advanced | Last updated: 2026-06-02*