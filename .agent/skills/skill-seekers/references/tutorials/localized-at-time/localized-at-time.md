# How To: Localized At Time

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test localized at time

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

### Step 3: Assign ts = frame_or_series(...)

```python
ts = frame_or_series(np.random.default_rng(2).standard_normal(len(rng)), index=rng)
```

### Step 4: Assign ts_local = ts.tz_localize(...)

```python
ts_local = ts.tz_localize(tzstr)
```

### Step 5: Assign result = ts_local.at_time(...)

```python
result = ts_local.at_time(time(10, 0))
```

### Step 6: Assign expected = ts.at_time.tz_localize(...)

```python
expected = ts.at_time(time(10, 0)).tz_localize(tzstr)
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

**Verification:**
```python
assert timezones.tz_compare(result.index.tz, tz)
```


## Complete Example

```python
# Setup
# Fixtures: tzstr, frame_or_series

# Workflow
tz = timezones.maybe_get_tz(tzstr)
rng = date_range('4/16/2012', '5/1/2012', freq='h')
ts = frame_or_series(np.random.default_rng(2).standard_normal(len(rng)), index=rng)
ts_local = ts.tz_localize(tzstr)
result = ts_local.at_time(time(10, 0))
expected = ts.at_time(time(10, 0)).tz_localize(tzstr)
tm.assert_equal(result, expected)
assert timezones.tz_compare(result.index.tz, tz)
```

## Next Steps


---

*Source: test_at_time.py:18 | Complexity: Intermediate | Last updated: 2026-06-02*