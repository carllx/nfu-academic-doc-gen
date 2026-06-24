# How To: Federal Holiday Inconsistent Returntype

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test federal holiday inconsistent returntype

## Prerequisites

**Required Modules:**
- `datetime`
- `pandas`
- `pandas._testing`
- `pandas.tseries.holiday`


## Step-by-Step Guide

### Step 1: Assign cal1 = USFederalHolidayCalendar(...)

```python
cal1 = USFederalHolidayCalendar()
```

### Step 2: Assign cal2 = USFederalHolidayCalendar(...)

```python
cal2 = USFederalHolidayCalendar()
```

### Step 3: Assign results_2018 = cal1.holidays(...)

```python
results_2018 = cal1.holidays(start=datetime(2018, 8, 1), end=datetime(2018, 8, 31))
```

### Step 4: Assign results_2019 = cal2.holidays(...)

```python
results_2019 = cal2.holidays(start=datetime(2019, 8, 1), end=datetime(2019, 8, 31))
```

### Step 5: Assign expected_results = DatetimeIndex(...)

```python
expected_results = DatetimeIndex([], dtype='datetime64[ns]', freq=None)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(results_2018, expected_results)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(results_2019, expected_results)
```


## Complete Example

```python
# Workflow
cal1 = USFederalHolidayCalendar()
cal2 = USFederalHolidayCalendar()
results_2018 = cal1.holidays(start=datetime(2018, 8, 1), end=datetime(2018, 8, 31))
results_2019 = cal2.holidays(start=datetime(2019, 8, 1), end=datetime(2019, 8, 31))
expected_results = DatetimeIndex([], dtype='datetime64[ns]', freq=None)
tm.assert_index_equal(results_2018, expected_results)
tm.assert_index_equal(results_2019, expected_results)
```

## Next Steps


---

*Source: test_federal.py:45 | Complexity: Intermediate | Last updated: 2026-06-02*