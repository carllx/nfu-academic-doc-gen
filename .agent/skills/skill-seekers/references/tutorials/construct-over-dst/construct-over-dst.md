# How To: Construct Over Dst

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test construct over dst

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

### Step 1: Assign pre_dst = Timestamp.tz_localize(...)

```python
pre_dst = Timestamp('2010-11-07 01:00:00').tz_localize('US/Pacific', ambiguous=True)
```

### Step 2: Assign pst_dst = Timestamp.tz_localize(...)

```python
pst_dst = Timestamp('2010-11-07 01:00:00').tz_localize('US/Pacific', ambiguous=False)
```

### Step 3: Assign expect_data = value

```python
expect_data = [Timestamp('2010-11-07 00:00:00', tz='US/Pacific'), pre_dst, pst_dst]
```

### Step 4: Assign expected = DatetimeIndex.as_unit(...)

```python
expected = DatetimeIndex(expect_data, freq='h').as_unit(unit)
```

### Step 5: Assign result = date_range(...)

```python
result = date_range(start='2010-11-7', periods=3, freq='h', tz='US/Pacific', unit=unit)
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
pre_dst = Timestamp('2010-11-07 01:00:00').tz_localize('US/Pacific', ambiguous=True)
pst_dst = Timestamp('2010-11-07 01:00:00').tz_localize('US/Pacific', ambiguous=False)
expect_data = [Timestamp('2010-11-07 00:00:00', tz='US/Pacific'), pre_dst, pst_dst]
expected = DatetimeIndex(expect_data, freq='h').as_unit(unit)
result = date_range(start='2010-11-7', periods=3, freq='h', tz='US/Pacific', unit=unit)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_date_range.py:452 | Complexity: Intermediate | Last updated: 2026-06-02*