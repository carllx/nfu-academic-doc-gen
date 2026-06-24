# How To: Calendar

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test calendar

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tseries.holiday`

**Setup Required:**
```python
# Fixtures: transform
```

## Step-by-Step Guide

### Step 1: Assign start_date = datetime(...)

```python
start_date = datetime(2012, 1, 1)
```

**Verification:**
```python
assert list(holidays.to_pydatetime()) == expected
```

### Step 2: Assign end_date = datetime(...)

```python
end_date = datetime(2012, 12, 31)
```

### Step 3: Assign calendar = USFederalHolidayCalendar(...)

```python
calendar = USFederalHolidayCalendar()
```

### Step 4: Assign holidays = calendar.holidays(...)

```python
holidays = calendar.holidays(transform(start_date), transform(end_date))
```

### Step 5: Assign expected = value

```python
expected = [datetime(2012, 1, 2), datetime(2012, 1, 16), datetime(2012, 2, 20), datetime(2012, 5, 28), datetime(2012, 7, 4), datetime(2012, 9, 3), datetime(2012, 10, 8), datetime(2012, 11, 12), datetime(2012, 11, 22), datetime(2012, 12, 25)]
```

**Verification:**
```python
assert list(holidays.to_pydatetime()) == expected
```


## Complete Example

```python
# Setup
# Fixtures: transform

# Workflow
start_date = datetime(2012, 1, 1)
end_date = datetime(2012, 12, 31)
calendar = USFederalHolidayCalendar()
holidays = calendar.holidays(transform(start_date), transform(end_date))
expected = [datetime(2012, 1, 2), datetime(2012, 1, 16), datetime(2012, 2, 20), datetime(2012, 5, 28), datetime(2012, 7, 4), datetime(2012, 9, 3), datetime(2012, 10, 8), datetime(2012, 11, 12), datetime(2012, 11, 22), datetime(2012, 12, 25)]
assert list(holidays.to_pydatetime()) == expected
```

## Next Steps


---

*Source: test_calendar.py:26 | Complexity: Intermediate | Last updated: 2026-06-02*