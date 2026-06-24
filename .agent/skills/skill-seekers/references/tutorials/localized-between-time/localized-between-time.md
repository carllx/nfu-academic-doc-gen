# How To: Localized Between Time

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test localized between time

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
# Fixtures: tzstr, frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign tz = timezones.maybe_get_tz(...)

```python
tz = timezones.maybe_get_tz(tzstr)
```

**Verification:**
```python
assert timezones.tz_compare(result.index.tz, tz)
```

### Step 2: Assign rng = date_range(...)

```python
rng = date_range('4/16/2012', '5/1/2012', freq='h')
```

### Step 3: Assign ts = Series(...)

```python
ts = Series(np.random.default_rng(2).standard_normal(len(rng)), index=rng)
```

### Step 4: Assign ts_local = ts.tz_localize(...)

```python
ts_local = ts.tz_localize(tzstr)
```

### Step 5: Assign unknown = value

```python
t1, t2 = (time(10, 0), time(11, 0))
```

### Step 6: Assign result = ts_local.between_time(...)

```python
result = ts_local.between_time(t1, t2)
```

### Step 7: Assign expected = ts.between_time.tz_localize(...)

```python
expected = ts.between_time(t1, t2).tz_localize(tzstr)
```

### Step 8: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

**Verification:**
```python
assert timezones.tz_compare(result.index.tz, tz)
```

### Step 9: Assign ts = ts.to_frame(...)

```python
ts = ts.to_frame()
```


## Complete Example

```python
# Setup
# Fixtures: tzstr, frame_or_series

# Workflow
tz = timezones.maybe_get_tz(tzstr)
rng = date_range('4/16/2012', '5/1/2012', freq='h')
ts = Series(np.random.default_rng(2).standard_normal(len(rng)), index=rng)
if frame_or_series is DataFrame:
    ts = ts.to_frame()
ts_local = ts.tz_localize(tzstr)
t1, t2 = (time(10, 0), time(11, 0))
result = ts_local.between_time(t1, t2)
expected = ts.between_time(t1, t2).tz_localize(tzstr)
tm.assert_equal(result, expected)
assert timezones.tz_compare(result.index.tz, tz)
```

## Next Steps


---

*Source: test_between_time.py:46 | Complexity: Advanced | Last updated: 2026-06-02*