# How To: Date Range Timedelta

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test date range timedelta

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign start = '2020-01-01'

```python
start = '2020-01-01'
```

### Step 2: Assign end = '2020-01-11'

```python
end = '2020-01-11'
```

### Step 3: Assign rng1 = date_range(...)

```python
rng1 = date_range(start, end, freq='3D')
```

### Step 4: Assign rng2 = date_range(...)

```python
rng2 = date_range(start, end, freq=timedelta(days=3))
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(rng1, rng2)
```


## Complete Example

```python
# Workflow
start = '2020-01-01'
end = '2020-01-11'
rng1 = date_range(start, end, freq='3D')
rng2 = date_range(start, end, freq=timedelta(days=3))
tm.assert_index_equal(rng1, rng2)
```

## Next Steps


---

*Source: test_date_range.py:404 | Complexity: Intermediate | Last updated: 2026-06-02*