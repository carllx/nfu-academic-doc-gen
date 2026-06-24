# How To: Utc Box Timestamp And Localize

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test utc box timestamp and localize

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tzstr
```

## Step-by-Step Guide

### Step 1: Assign tz = timezones.maybe_get_tz(...)

```python
tz = timezones.maybe_get_tz(tzstr)
```

**Verification:**
```python
assert stamp == expected
```

### Step 2: Assign rng = date_range(...)

```python
rng = date_range('3/11/2012', '3/12/2012', freq='h', tz='utc')
```

**Verification:**
```python
assert stamp.tzinfo == expected.tzinfo
```

### Step 3: Assign rng_eastern = rng.tz_convert(...)

```python
rng_eastern = rng.tz_convert(tzstr)
```

**Verification:**
```python
assert 'EDT' in repr(rng_eastern[0].tzinfo) or 'tzfile' in repr(rng_eastern[0].tzinfo)
```

### Step 4: Assign expected = unknown.astimezone(...)

```python
expected = rng[-1].astimezone(tz)
```

### Step 5: Assign stamp = value

```python
stamp = rng_eastern[-1]
```

**Verification:**
```python
assert stamp == expected
```

### Step 6: Assign rng = date_range(...)

```python
rng = date_range('3/13/2012', '3/14/2012', freq='h', tz='utc')
```

### Step 7: Assign rng_eastern = rng.tz_convert(...)

```python
rng_eastern = rng.tz_convert(tzstr)
```

**Verification:**
```python
assert 'EDT' in repr(rng_eastern[0].tzinfo) or 'tzfile' in repr(rng_eastern[0].tzinfo)
```


## Complete Example

```python
# Setup
# Fixtures: tzstr

# Workflow
tz = timezones.maybe_get_tz(tzstr)
rng = date_range('3/11/2012', '3/12/2012', freq='h', tz='utc')
rng_eastern = rng.tz_convert(tzstr)
expected = rng[-1].astimezone(tz)
stamp = rng_eastern[-1]
assert stamp == expected
assert stamp.tzinfo == expected.tzinfo
rng = date_range('3/13/2012', '3/14/2012', freq='h', tz='utc')
rng_eastern = rng.tz_convert(tzstr)
assert 'EDT' in repr(rng_eastern[0].tzinfo) or 'tzfile' in repr(rng_eastern[0].tzinfo)
```

## Next Steps


---

*Source: test_timezones.py:187 | Complexity: Intermediate | Last updated: 2026-06-02*