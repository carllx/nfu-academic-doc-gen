# How To: Argument Types

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test argument types

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `pytest`
- `pytz`
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
start_date = datetime(2011, 1, 1)
```

### Step 2: Assign end_date = datetime(...)

```python
end_date = datetime(2020, 12, 31)
```

### Step 3: Assign holidays = USThanksgivingDay.dates(...)

```python
holidays = USThanksgivingDay.dates(start_date, end_date)
```

### Step 4: Assign holidays2 = USThanksgivingDay.dates(...)

```python
holidays2 = USThanksgivingDay.dates(transform(start_date), transform(end_date))
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(holidays, holidays2)
```


## Complete Example

```python
# Setup
# Fixtures: transform

# Workflow
start_date = datetime(2011, 1, 1)
end_date = datetime(2020, 12, 31)
holidays = USThanksgivingDay.dates(start_date, end_date)
holidays2 = USThanksgivingDay.dates(transform(start_date), transform(end_date))
tm.assert_index_equal(holidays, holidays2)
```

## Next Steps


---

*Source: test_holiday.py:204 | Complexity: Intermediate | Last updated: 2026-06-02*