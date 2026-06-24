# How To: Date Range Convenience Periods

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test date range convenience periods

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pytz`
- `pytz`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.datetimes`
- `pandas.tests.indexes.datetimes.test_timezones`
- `pandas.tseries.holiday`
- `pandas._libs.tslibs.timezones`
- `pandas._libs.tslibs.timezones`

**Setup Required:**
```python
# Fixtures: unit
```

## Step-by-Step Guide

### Step 1: Assign result = date_range(...)

```python
result = date_range('2018-04-24', '2018-04-27', periods=3, unit=unit)
```

### Step 2: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex(['2018-04-24 00:00:00', '2018-04-25 12:00:00', '2018-04-27 00:00:00'], dtype=f'M8[{unit}]', freq=None)
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 4: Assign result = date_range(...)

```python
result = date_range('2018-04-01 01:00:00', '2018-04-01 04:00:00', tz='Australia/Sydney', periods=3, unit=unit)
```

### Step 5: Assign expected = DatetimeIndex.as_unit(...)

```python
expected = DatetimeIndex([Timestamp('2018-04-01 01:00:00+1100', tz='Australia/Sydney'), Timestamp('2018-04-01 02:00:00+1000', tz='Australia/Sydney'), Timestamp('2018-04-01 04:00:00+1000', tz='Australia/Sydney')]).as_unit(unit)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
result = date_range('2018-04-24', '2018-04-27', periods=3, unit=unit)
expected = DatetimeIndex(['2018-04-24 00:00:00', '2018-04-25 12:00:00', '2018-04-27 00:00:00'], dtype=f'M8[{unit}]', freq=None)
tm.assert_index_equal(result, expected)
result = date_range('2018-04-01 01:00:00', '2018-04-01 04:00:00', tz='Australia/Sydney', periods=3, unit=unit)
expected = DatetimeIndex([Timestamp('2018-04-01 01:00:00+1100', tz='Australia/Sydney'), Timestamp('2018-04-01 02:00:00+1000', tz='Australia/Sydney'), Timestamp('2018-04-01 04:00:00+1000', tz='Australia/Sydney')]).as_unit(unit)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_date_range.py:324 | Complexity: Intermediate | Last updated: 2026-06-02*