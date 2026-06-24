# How To: Timestamp Timetz Equivalent With Datetime Tz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test timestamp timetz equivalent with datetime tz

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `pandas._libs.tslibs`
- `pandas`

**Setup Required:**
```python
# Fixtures: tz_naive_fixture
```

## Step-by-Step Guide

### Step 1: Assign tz = timezones.maybe_get_tz(...)

```python
tz = timezones.maybe_get_tz(tz_naive_fixture)
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign stamp = Timestamp(...)

```python
stamp = Timestamp('2018-06-04 10:20:30', tz=tz)
```

### Step 3: Assign _datetime = datetime(...)

```python
_datetime = datetime(2018, 6, 4, hour=10, minute=20, second=30, tzinfo=tz)
```

### Step 4: Assign result = stamp.timetz(...)

```python
result = stamp.timetz()
```

### Step 5: Assign expected = _datetime.timetz(...)

```python
expected = _datetime.timetz()
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Setup
# Fixtures: tz_naive_fixture

# Workflow
tz = timezones.maybe_get_tz(tz_naive_fixture)
stamp = Timestamp('2018-06-04 10:20:30', tz=tz)
_datetime = datetime(2018, 6, 4, hour=10, minute=20, second=30, tzinfo=tz)
result = stamp.timetz()
expected = _datetime.timetz()
assert result == expected
```

## Next Steps


---

*Source: test_timezones.py:14 | Complexity: Intermediate | Last updated: 2026-06-02*