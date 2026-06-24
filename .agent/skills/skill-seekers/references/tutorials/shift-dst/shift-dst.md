# How To: Shift Dst

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test shift dst

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
# Fixtures: frame_or_series
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

**Verification:**
```python
assert tm.get_dtype(res) == 'datetime64[ns, US/Eastern]'
```

### Step 3: Assign res = obj.shift(...)

```python
res = obj.shift(0)
```

**Verification:**
```python
assert tm.get_dtype(res) == 'datetime64[ns, US/Eastern]'
```

### Step 4: Call tm.assert_equal()

```python
tm.assert_equal(res, obj)
```

**Verification:**
```python
assert tm.get_dtype(res) == 'datetime64[ns, US/Eastern]'
```

### Step 5: Assign res = obj.shift(...)

```python
res = obj.shift(1)
```

### Step 6: Assign exp_vals = value

```python
exp_vals = [NaT] + dates.astype(object).values.tolist()[:9]
```

### Step 7: Assign exp = frame_or_series(...)

```python
exp = frame_or_series(exp_vals)
```

### Step 8: Call tm.assert_equal()

```python
tm.assert_equal(res, exp)
```

**Verification:**
```python
assert tm.get_dtype(res) == 'datetime64[ns, US/Eastern]'
```

### Step 9: Assign res = obj.shift(...)

```python
res = obj.shift(-2)
```

### Step 10: Assign exp_vals = value

```python
exp_vals = dates.astype(object).values.tolist()[2:] + [NaT, NaT]
```

### Step 11: Assign exp = frame_or_series(...)

```python
exp = frame_or_series(exp_vals)
```

### Step 12: Call tm.assert_equal()

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
# Fixtures: frame_or_series

# Workflow
dates = date_range('2016-11-06', freq='h', periods=10, tz='US/Eastern')
obj = frame_or_series(dates)
res = obj.shift(0)
tm.assert_equal(res, obj)
assert tm.get_dtype(res) == 'datetime64[ns, US/Eastern]'
res = obj.shift(1)
exp_vals = [NaT] + dates.astype(object).values.tolist()[:9]
exp = frame_or_series(exp_vals)
tm.assert_equal(res, exp)
assert tm.get_dtype(res) == 'datetime64[ns, US/Eastern]'
res = obj.shift(-2)
exp_vals = dates.astype(object).values.tolist()[2:] + [NaT, NaT]
exp = frame_or_series(exp_vals)
tm.assert_equal(res, exp)
assert tm.get_dtype(res) == 'datetime64[ns, US/Eastern]'
```

## Next Steps


---

*Source: test_shift.py:158 | Complexity: Advanced | Last updated: 2026-06-02*