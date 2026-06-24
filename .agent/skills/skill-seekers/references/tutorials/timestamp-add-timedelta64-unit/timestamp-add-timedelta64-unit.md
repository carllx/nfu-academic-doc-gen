# How To: Timestamp Add Timedelta64 Unit

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test timestamp add timedelta64 unit

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
# Fixtures: other, expected_difference
```

## Step-by-Step Guide

### Step 1: Assign now = datetime.now(...)

```python
now = datetime.now(timezone.utc)
```

**Verification:**
```python
assert valdiff == expected_difference
```

### Step 2: Assign ts = Timestamp.as_unit(...)

```python
ts = Timestamp(now).as_unit('ns')
```

**Verification:**
```python
assert ts2 + other == result
```

### Step 3: Assign result = value

```python
result = ts + other
```

### Step 4: Assign valdiff = value

```python
valdiff = result._value - ts._value
```

**Verification:**
```python
assert valdiff == expected_difference
```

### Step 5: Assign ts2 = Timestamp(...)

```python
ts2 = Timestamp(now)
```

**Verification:**
```python
assert ts2 + other == result
```


## Complete Example

```python
# Setup
# Fixtures: other, expected_difference

# Workflow
now = datetime.now(timezone.utc)
ts = Timestamp(now).as_unit('ns')
result = ts + other
valdiff = result._value - ts._value
assert valdiff == expected_difference
ts2 = Timestamp(now)
assert ts2 + other == result
```

## Next Steps


---

*Source: test_arithmetic.py:196 | Complexity: Intermediate | Last updated: 2026-06-02*