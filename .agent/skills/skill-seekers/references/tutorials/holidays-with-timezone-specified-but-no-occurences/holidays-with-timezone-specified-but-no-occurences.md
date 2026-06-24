# How To: Holidays With Timezone Specified But No Occurences

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test holidays with timezone specified but no occurences

## Prerequisites

**Required Modules:**
- `datetime`
- `pytest`
- `pytz`
- `pandas`
- `pandas._testing`
- `pandas.tseries.holiday`


## Step-by-Step Guide

### Step 1: Assign start_date = Timestamp(...)

```python
start_date = Timestamp('2018-01-01', tz='America/Chicago')
```

### Step 2: Assign end_date = Timestamp(...)

```python
end_date = Timestamp('2018-01-11', tz='America/Chicago')
```

### Step 3: Assign test_case = USFederalHolidayCalendar.holidays(...)

```python
test_case = USFederalHolidayCalendar().holidays(start_date, end_date, return_name=True)
```

### Step 4: Assign expected_results = Series(...)

```python
expected_results = Series("New Year's Day", index=[start_date])
```

### Step 5: Assign expected_results.index = expected_results.index.as_unit(...)

```python
expected_results.index = expected_results.index.as_unit('ns')
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(test_case, expected_results)
```


## Complete Example

```python
# Workflow
start_date = Timestamp('2018-01-01', tz='America/Chicago')
end_date = Timestamp('2018-01-11', tz='America/Chicago')
test_case = USFederalHolidayCalendar().holidays(start_date, end_date, return_name=True)
expected_results = Series("New Year's Day", index=[start_date])
expected_results.index = expected_results.index.as_unit('ns')
tm.assert_equal(test_case, expected_results)
```

## Next Steps


---

*Source: test_holiday.py:320 | Complexity: Intermediate | Last updated: 2026-06-02*