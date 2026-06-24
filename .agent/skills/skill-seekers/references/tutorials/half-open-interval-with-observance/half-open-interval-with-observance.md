# How To: Half Open Interval With Observance

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test half open interval with observance

## Prerequisites

**Required Modules:**
- `datetime`
- `pytest`
- `pytz`
- `pandas`
- `pandas._testing`
- `pandas.tseries.holiday`


## Step-by-Step Guide

### Step 1: Assign holiday_1 = Holiday(...)

```python
holiday_1 = Holiday('Arbitrary Holiday - start 2022-03-14', start_date=datetime(2022, 3, 14), month=3, day=14, observance=next_monday)
```

### Step 2: Assign holiday_2 = Holiday(...)

```python
holiday_2 = Holiday('Arbitrary Holiday 2 - end 2022-03-20', end_date=datetime(2022, 3, 20), month=3, day=20, observance=next_monday)
```

### Step 3: Assign start = Timestamp(...)

```python
start = Timestamp('2022-08-01')
```

### Step 4: Assign end = Timestamp(...)

```python
end = Timestamp('2022-08-31')
```

### Step 5: Assign year_offset = DateOffset(...)

```python
year_offset = DateOffset(years=5)
```

### Step 6: Assign expected_results = DatetimeIndex(...)

```python
expected_results = DatetimeIndex([], dtype='datetime64[ns]', freq=None)
```

### Step 7: Assign test_cal = TestHolidayCalendar(...)

```python
test_cal = TestHolidayCalendar()
```

### Step 8: Assign date_interval_low = test_cal.holidays(...)

```python
date_interval_low = test_cal.holidays(start - year_offset, end - year_offset)
```

### Step 9: Assign date_window_edge = test_cal.holidays(...)

```python
date_window_edge = test_cal.holidays(start, end)
```

### Step 10: Assign date_interval_high = test_cal.holidays(...)

```python
date_interval_high = test_cal.holidays(start + year_offset, end + year_offset)
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(date_interval_low, expected_results)
```

### Step 12: Call tm.assert_index_equal()

```python
tm.assert_index_equal(date_window_edge, expected_results)
```

### Step 13: Call tm.assert_index_equal()

```python
tm.assert_index_equal(date_interval_high, expected_results)
```

### Step 14: Assign rules = value

```python
rules = [USMartinLutherKingJr, holiday_1, holiday_2, USLaborDay]
```


## Complete Example

```python
# Workflow
holiday_1 = Holiday('Arbitrary Holiday - start 2022-03-14', start_date=datetime(2022, 3, 14), month=3, day=14, observance=next_monday)
holiday_2 = Holiday('Arbitrary Holiday 2 - end 2022-03-20', end_date=datetime(2022, 3, 20), month=3, day=20, observance=next_monday)

class TestHolidayCalendar(AbstractHolidayCalendar):
    rules = [USMartinLutherKingJr, holiday_1, holiday_2, USLaborDay]
start = Timestamp('2022-08-01')
end = Timestamp('2022-08-31')
year_offset = DateOffset(years=5)
expected_results = DatetimeIndex([], dtype='datetime64[ns]', freq=None)
test_cal = TestHolidayCalendar()
date_interval_low = test_cal.holidays(start - year_offset, end - year_offset)
date_window_edge = test_cal.holidays(start, end)
date_interval_high = test_cal.holidays(start + year_offset, end + year_offset)
tm.assert_index_equal(date_interval_low, expected_results)
tm.assert_index_equal(date_window_edge, expected_results)
tm.assert_index_equal(date_interval_high, expected_results)
```

## Next Steps


---

*Source: test_holiday.py:274 | Complexity: Advanced | Last updated: 2026-06-02*