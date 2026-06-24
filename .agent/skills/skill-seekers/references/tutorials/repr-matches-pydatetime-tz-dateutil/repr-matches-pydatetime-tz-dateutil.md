# How To: Repr Matches Pydatetime Tz Dateutil

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test repr matches pydatetime tz dateutil

## Prerequisites

**Required Modules:**
- `datetime`
- `pprint`
- `dateutil.tz`
- `pytest`
- `pytz`
- `pandas`


## Step-by-Step Guide

### Step 1: Assign utc = dateutil.tz.tzutc(...)

```python
utc = dateutil.tz.tzutc()
```

**Verification:**
```python
assert str(dt_date) == str(Timestamp(dt_date))
```

### Step 2: Assign dt_date = datetime(...)

```python
dt_date = datetime(2013, 1, 2, tzinfo=utc)
```

**Verification:**
```python
assert str(dt_datetime) == str(Timestamp(dt_datetime))
```

### Step 3: Assign dt_datetime = datetime(...)

```python
dt_datetime = datetime(2013, 1, 2, 12, 1, 3, tzinfo=utc)
```

**Verification:**
```python
assert str(dt_datetime_us) == str(Timestamp(dt_datetime_us))
```

### Step 4: Assign dt_datetime_us = datetime(...)

```python
dt_datetime_us = datetime(2013, 1, 2, 12, 1, 3, 45, tzinfo=utc)
```

**Verification:**
```python
assert str(dt_datetime_us) == str(Timestamp(dt_datetime_us))
```


## Complete Example

```python
# Workflow
utc = dateutil.tz.tzutc()
dt_date = datetime(2013, 1, 2, tzinfo=utc)
assert str(dt_date) == str(Timestamp(dt_date))
dt_datetime = datetime(2013, 1, 2, 12, 1, 3, tzinfo=utc)
assert str(dt_datetime) == str(Timestamp(dt_datetime))
dt_datetime_us = datetime(2013, 1, 2, 12, 1, 3, 45, tzinfo=utc)
assert str(dt_datetime_us) == str(Timestamp(dt_datetime_us))
```

## Next Steps


---

*Source: test_formats.py:191 | Complexity: Intermediate | Last updated: 2026-06-02*