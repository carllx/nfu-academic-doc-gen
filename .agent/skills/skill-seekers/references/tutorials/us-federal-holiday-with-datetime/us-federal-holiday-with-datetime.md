# How To: Us Federal Holiday With Datetime

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test us federal holiday with datetime

## Prerequisites

**Required Modules:**
- `__future__`
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas.tests.tseries.offsets.common`
- `pandas.tseries.holiday`


## Step-by-Step Guide

### Step 1: Assign bhour_us = CustomBusinessHour(...)

```python
bhour_us = CustomBusinessHour(calendar=USFederalHolidayCalendar())
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign t0 = datetime(...)

```python
t0 = datetime(2014, 1, 17, 15)
```

### Step 3: Assign result = value

```python
result = t0 + bhour_us * 8
```

### Step 4: Assign expected = Timestamp(...)

```python
expected = Timestamp('2014-01-21 15:00:00')
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
bhour_us = CustomBusinessHour(calendar=USFederalHolidayCalendar())
t0 = datetime(2014, 1, 17, 15)
result = t0 + bhour_us * 8
expected = Timestamp('2014-01-21 15:00:00')
assert result == expected
```

## Next Steps


---

*Source: test_custom_business_hour.py:305 | Complexity: Intermediate | Last updated: 2026-06-02*