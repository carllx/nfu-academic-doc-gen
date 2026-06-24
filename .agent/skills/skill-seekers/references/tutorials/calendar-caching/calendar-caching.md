# How To: Calendar Caching

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test calendar caching

## Prerequisites

**Required Modules:**
- `datetime`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.tseries.holiday`


## Step-by-Step Guide

### Step 1: Assign jan1 = TestCalendar(...)

```python
jan1 = TestCalendar(rules=[Holiday('jan1', year=2015, month=1, day=1)])
```

### Step 2: Assign jan2 = TestCalendar(...)

```python
jan2 = TestCalendar(rules=[Holiday('jan2', year=2015, month=1, day=2)])
```

### Step 3: Assign expected = DatetimeIndex.as_unit(...)

```python
expected = DatetimeIndex(['01-Jan-2015']).as_unit('ns')
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(jan1.holidays(), expected)
```

### Step 5: Assign expected2 = DatetimeIndex.as_unit(...)

```python
expected2 = DatetimeIndex(['02-Jan-2015']).as_unit('ns')
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(jan2.holidays(), expected2)
```

### Step 7: Call super.__init__()

```python
super().__init__(name=name, rules=rules)
```


## Complete Example

```python
# Workflow
class TestCalendar(AbstractHolidayCalendar):

    def __init__(self, name=None, rules=None) -> None:
        super().__init__(name=name, rules=rules)
jan1 = TestCalendar(rules=[Holiday('jan1', year=2015, month=1, day=1)])
jan2 = TestCalendar(rules=[Holiday('jan2', year=2015, month=1, day=2)])
expected = DatetimeIndex(['01-Jan-2015']).as_unit('ns')
tm.assert_index_equal(jan1.holidays(), expected)
expected2 = DatetimeIndex(['02-Jan-2015']).as_unit('ns')
tm.assert_index_equal(jan2.holidays(), expected2)
```

## Next Steps


---

*Source: test_calendar.py:49 | Complexity: Intermediate | Last updated: 2026-06-02*