# How To: Maybe Get Tz Offset Only

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test maybe get tz offset only

## Prerequisites

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas.compat`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign tz = timezones.maybe_get_tz(...)

```python
tz = timezones.maybe_get_tz(timezone.utc)
```

**Verification:**
```python
assert tz == timezone(timedelta(hours=0, minutes=0))
```

### Step 2: Assign tz = timezones.maybe_get_tz(...)

```python
tz = timezones.maybe_get_tz('+01:15')
```

**Verification:**
```python
assert tz == timezone(timedelta(hours=1, minutes=15))
```

### Step 3: Assign tz = timezones.maybe_get_tz(...)

```python
tz = timezones.maybe_get_tz('-01:15')
```

**Verification:**
```python
assert tz == timezone(-timedelta(hours=1, minutes=15))
```

### Step 4: Assign tz = timezones.maybe_get_tz(...)

```python
tz = timezones.maybe_get_tz('UTC+02:45')
```

**Verification:**
```python
assert tz == timezone(timedelta(hours=2, minutes=45))
```

### Step 5: Assign tz = timezones.maybe_get_tz(...)

```python
tz = timezones.maybe_get_tz('UTC-02:45')
```

**Verification:**
```python
assert tz == timezone(-timedelta(hours=2, minutes=45))
```


## Complete Example

```python
# Workflow
tz = timezones.maybe_get_tz(timezone.utc)
assert tz == timezone(timedelta(hours=0, minutes=0))
tz = timezones.maybe_get_tz('+01:15')
assert tz == timezone(timedelta(hours=1, minutes=15))
tz = timezones.maybe_get_tz('-01:15')
assert tz == timezone(-timedelta(hours=1, minutes=15))
tz = timezones.maybe_get_tz('UTC+02:45')
assert tz == timezone(timedelta(hours=2, minutes=45))
tz = timezones.maybe_get_tz('UTC-02:45')
assert tz == timezone(-timedelta(hours=2, minutes=45))
```

## Next Steps


---

*Source: test_timezones.py:149 | Complexity: Intermediate | Last updated: 2026-06-02*