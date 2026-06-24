# How To: Shift Dst Beyond

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test shift dst beyond

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: frame_or_series, ex
```

## Step-by-Step Guide

### Step 1: Assign dates = date_range(...)

```python
dates = date_range('2016-11-06', freq='h', periods=10, tz='US/Eastern')
```

**Verification:**
```python
assert tm.get_dtype(res) == 'datetime64[ns, US/Eastern]'
```

### Step 2: Assign obj = frame_or_series(...)

```python
obj = frame_or_series(dates)
```

### Step 3: Assign res = obj.shift(...)

```python
res = obj.shift(ex)
```

### Step 4: Assign exp = frame_or_series(...)

```python
exp = frame_or_series([NaT] * 10, dtype='datetime64[ns, US/Eastern]')
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(res, exp)
```

**Verification:**
```python
assert tm.get_dtype(res) == 'datetime64[ns, US/Eastern]'
```


## Complete Example

```python
# Setup
# Fixtures: frame_or_series, ex

# Workflow
dates = date_range('2016-11-06', freq='h', periods=10, tz='US/Eastern')
obj = frame_or_series(dates)
res = obj.shift(ex)
exp = frame_or_series([NaT] * 10, dtype='datetime64[ns, US/Eastern]')
tm.assert_equal(res, exp)
assert tm.get_dtype(res) == 'datetime64[ns, US/Eastern]'
```

## Next Steps


---

*Source: test_shift.py:180 | Complexity: Intermediate | Last updated: 2026-06-02*