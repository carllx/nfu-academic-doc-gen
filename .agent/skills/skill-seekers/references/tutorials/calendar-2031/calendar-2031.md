# How To: Calendar 2031

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test calendar 2031

## Prerequisites

**Required Modules:**
- `datetime`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tseries.holiday`


## Step-by-Step Guide

### Step 1: Assign cal = testCalendar(...)

```python
cal = testCalendar()
```

**Verification:**
```python
assert next_working_day == to_datetime('2031-09-02')
```

### Step 2: Assign workDay = offsets.CustomBusinessDay(...)

```python
workDay = offsets.CustomBusinessDay(calendar=cal)
```

### Step 3: Assign Sat_before_Labor_Day_2031 = to_datetime(...)

```python
Sat_before_Labor_Day_2031 = to_datetime('2031-08-30')
```

### Step 4: Assign next_working_day = value

```python
next_working_day = Sat_before_Labor_Day_2031 + 0 * workDay
```

**Verification:**
```python
assert next_working_day == to_datetime('2031-09-02')
```

### Step 5: Assign rules = value

```python
rules = [USLaborDay]
```


## Complete Example

```python
# Workflow
class testCalendar(AbstractHolidayCalendar):
    rules = [USLaborDay]
cal = testCalendar()
workDay = offsets.CustomBusinessDay(calendar=cal)
Sat_before_Labor_Day_2031 = to_datetime('2031-08-30')
next_working_day = Sat_before_Labor_Day_2031 + 0 * workDay
assert next_working_day == to_datetime('2031-09-02')
```

## Next Steps


---

*Source: test_calendar.py:94 | Complexity: Intermediate | Last updated: 2026-06-02*