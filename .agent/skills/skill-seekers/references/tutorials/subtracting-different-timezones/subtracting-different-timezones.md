# How To: Subtracting Different Timezones

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test subtracting different timezones

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz_aware_fixture
```

## Step-by-Step Guide

### Step 1: Assign t_raw = Timestamp(...)

```python
t_raw = Timestamp('20130101')
```

**Verification:**
```python
assert isinstance(result, Timedelta)
```

### Step 2: Assign t_UTC = t_raw.tz_localize(...)

```python
t_UTC = t_raw.tz_localize('UTC')
```

**Verification:**
```python
assert result == Timedelta('0 days 05:00:00')
```

### Step 3: Assign t_diff = value

```python
t_diff = t_UTC.tz_convert(tz_aware_fixture) + Timedelta('0 days 05:00:00')
```

### Step 4: Assign result = value

```python
result = t_diff - t_UTC
```

**Verification:**
```python
assert isinstance(result, Timedelta)
```


## Complete Example

```python
# Setup
# Fixtures: tz_aware_fixture

# Workflow
t_raw = Timestamp('20130101')
t_UTC = t_raw.tz_localize('UTC')
t_diff = t_UTC.tz_convert(tz_aware_fixture) + Timedelta('0 days 05:00:00')
result = t_diff - t_UTC
assert isinstance(result, Timedelta)
assert result == Timedelta('0 days 05:00:00')
```

## Next Steps


---

*Source: test_arithmetic.py:143 | Complexity: Intermediate | Last updated: 2026-06-02*