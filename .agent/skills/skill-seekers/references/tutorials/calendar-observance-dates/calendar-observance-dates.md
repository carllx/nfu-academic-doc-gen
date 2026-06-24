# How To: Calendar Observance Dates

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test calendar observance dates

## Prerequisites

**Required Modules:**
- `datetime`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tseries.holiday`


## Step-by-Step Guide

### Step 1: Assign us_fed_cal = get_calendar(...)

```python
us_fed_cal = get_calendar('USFederalHolidayCalendar')
```

### Step 2: Assign holidays0 = us_fed_cal.holidays(...)

```python
holidays0 = us_fed_cal.holidays(datetime(2015, 7, 3), datetime(2015, 7, 3))
```

### Step 3: Assign holidays1 = us_fed_cal.holidays(...)

```python
holidays1 = us_fed_cal.holidays(datetime(2015, 7, 3), datetime(2015, 7, 6))
```

### Step 4: Assign holidays2 = us_fed_cal.holidays(...)

```python
holidays2 = us_fed_cal.holidays(datetime(2015, 7, 3), datetime(2015, 7, 3))
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(holidays0, holidays1)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(holidays0, holidays2)
```


## Complete Example

```python
# Workflow
us_fed_cal = get_calendar('USFederalHolidayCalendar')
holidays0 = us_fed_cal.holidays(datetime(2015, 7, 3), datetime(2015, 7, 3))
holidays1 = us_fed_cal.holidays(datetime(2015, 7, 3), datetime(2015, 7, 6))
holidays2 = us_fed_cal.holidays(datetime(2015, 7, 3), datetime(2015, 7, 3))
tm.assert_index_equal(holidays0, holidays1)
tm.assert_index_equal(holidays0, holidays2)
```

## Next Steps


---

*Source: test_calendar.py:67 | Complexity: Intermediate | Last updated: 2026-06-02*