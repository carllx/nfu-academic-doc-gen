# How To: Subtracting Involving Datetime With Different Tz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test subtracting involving datetime with different tz

## Prerequisites

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign t1 = datetime(...)

```python
t1 = datetime(2013, 1, 1, tzinfo=timezone(timedelta(hours=-5)))
```

**Verification:**
```python
assert isinstance(result, Timedelta)
```

### Step 2: Assign t2 = Timestamp.tz_localize(...)

```python
t2 = Timestamp('20130101').tz_localize('CET')
```

**Verification:**
```python
assert result == Timedelta('0 days 06:00:00')
```

### Step 3: Assign result = value

```python
result = t1 - t2
```

**Verification:**
```python
assert isinstance(result, Timedelta)
```

### Step 4: Assign result = value

```python
result = t2 - t1
```

**Verification:**
```python
assert result == Timedelta('-1 days +18:00:00')
```


## Complete Example

```python
# Workflow
t1 = datetime(2013, 1, 1, tzinfo=timezone(timedelta(hours=-5)))
t2 = Timestamp('20130101').tz_localize('CET')
result = t1 - t2
assert isinstance(result, Timedelta)
assert result == Timedelta('0 days 06:00:00')
result = t2 - t1
assert isinstance(result, Timedelta)
assert result == Timedelta('-1 days +18:00:00')
```

## Next Steps


---

*Source: test_arithmetic.py:130 | Complexity: Intermediate | Last updated: 2026-06-02*