# How To: Custom Businesshour Weekmask And Holidays

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test custom businesshour weekmask and holidays

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `__future__`
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas.tests.tseries.offsets.common`
- `pandas.tseries.holiday`

**Setup Required:**
```python
# Fixtures: weekmask, expected_time, mult
```

## Step-by-Step Guide

### Step 1: Assign holidays = value

```python
holidays = ['2018-11-09']
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign bh = CustomBusinessHour(...)

```python
bh = CustomBusinessHour(start='08:00', end='17:00', weekmask=weekmask, holidays=holidays)
```

### Step 3: Assign result = value

```python
result = Timestamp('2018-11-08 08:00') + mult * bh
```

### Step 4: Assign expected = Timestamp(...)

```python
expected = Timestamp(expected_time)
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Setup
# Fixtures: weekmask, expected_time, mult

# Workflow
holidays = ['2018-11-09']
bh = CustomBusinessHour(start='08:00', end='17:00', weekmask=weekmask, holidays=holidays)
result = Timestamp('2018-11-08 08:00') + mult * bh
expected = Timestamp(expected_time)
assert result == expected
```

## Next Steps


---

*Source: test_custom_business_hour.py:321 | Complexity: Intermediate | Last updated: 2026-06-02*