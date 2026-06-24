# How To: Dti Tz Localize Pass Dates To Utc

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dti tz localize pass dates to utc

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas._testing`
- `zoneinfo`

**Setup Required:**
```python
# Fixtures: tzstr
```

## Step-by-Step Guide

### Step 1: Assign strdates = value

```python
strdates = ['1/1/2012', '3/1/2012', '4/1/2012']
```

**Verification:**
```python
assert conv.tz == fromdates.tz
```

### Step 2: Assign idx = DatetimeIndex(...)

```python
idx = DatetimeIndex(strdates)
```

### Step 3: Assign conv = idx.tz_localize(...)

```python
conv = idx.tz_localize(tzstr)
```

### Step 4: Assign fromdates = DatetimeIndex(...)

```python
fromdates = DatetimeIndex(strdates, tz=tzstr)
```

**Verification:**
```python
assert conv.tz == fromdates.tz
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(conv.values, fromdates.values)
```


## Complete Example

```python
# Setup
# Fixtures: tzstr

# Workflow
strdates = ['1/1/2012', '3/1/2012', '4/1/2012']
idx = DatetimeIndex(strdates)
conv = idx.tz_localize(tzstr)
fromdates = DatetimeIndex(strdates, tz=tzstr)
assert conv.tz == fromdates.tz
tm.assert_numpy_array_equal(conv.values, fromdates.values)
```

## Next Steps


---

*Source: test_tz_localize.py:150 | Complexity: Intermediate | Last updated: 2026-06-02*