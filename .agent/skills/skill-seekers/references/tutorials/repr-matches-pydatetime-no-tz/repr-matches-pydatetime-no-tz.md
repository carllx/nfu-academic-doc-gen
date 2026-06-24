# How To: Repr Matches Pydatetime No Tz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test repr matches pydatetime no tz

## Prerequisites

**Required Modules:**
- `datetime`
- `pprint`
- `dateutil.tz`
- `pytest`
- `pytz`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign dt_date = datetime(...)

```python
dt_date = datetime(2013, 1, 2)
```

**Verification:**
```python
assert str(dt_date) == str(Timestamp(dt_date))
```

### Step 2: Assign dt_datetime = datetime(...)

```python
dt_datetime = datetime(2013, 1, 2, 12, 1, 3)
```

**Verification:**
```python
assert str(dt_datetime) == str(Timestamp(dt_datetime))
```

### Step 3: Assign dt_datetime_us = datetime(...)

```python
dt_datetime_us = datetime(2013, 1, 2, 12, 1, 3, 45)
```

**Verification:**
```python
assert str(dt_datetime_us) == str(Timestamp(dt_datetime_us))
```

### Step 4: Assign ts_nanos_only = Timestamp(...)

```python
ts_nanos_only = Timestamp(200)
```

**Verification:**
```python
assert str(ts_nanos_only) == '1970-01-01 00:00:00.000000200'
```

### Step 5: Assign ts_nanos_micros = Timestamp(...)

```python
ts_nanos_micros = Timestamp(1200)
```

**Verification:**
```python
assert str(ts_nanos_micros) == '1970-01-01 00:00:00.000001200'
```


## Complete Example

```python
# Workflow
dt_date = datetime(2013, 1, 2)
assert str(dt_date) == str(Timestamp(dt_date))
dt_datetime = datetime(2013, 1, 2, 12, 1, 3)
assert str(dt_datetime) == str(Timestamp(dt_datetime))
dt_datetime_us = datetime(2013, 1, 2, 12, 1, 3, 45)
assert str(dt_datetime_us) == str(Timestamp(dt_datetime_us))
ts_nanos_only = Timestamp(200)
assert str(ts_nanos_only) == '1970-01-01 00:00:00.000000200'
ts_nanos_micros = Timestamp(1200)
assert str(ts_nanos_micros) == '1970-01-01 00:00:00.000001200'
```

## Next Steps


---

*Source: test_formats.py:165 | Complexity: Intermediate | Last updated: 2026-06-02*