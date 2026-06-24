# How To: Dti To Pydatetime Fizedtz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dti to pydatetime fizedtz

## Prerequisites

**Required Modules:**
- `datetime`
- `dateutil.parser`
- `dateutil.tz`
- `dateutil.tz`
- `numpy`
- `pandas`
- `pandas._testing`
- `pandas.tests.indexes.datetimes.test_timezones`


## Step-by-Step Guide

### Step 1: Assign dates = np.array(...)

```python
dates = np.array([datetime(2000, 1, 1, tzinfo=fixed_off), datetime(2000, 1, 2, tzinfo=fixed_off), datetime(2000, 1, 3, tzinfo=fixed_off)])
```

### Step 2: Assign dti = DatetimeIndex(...)

```python
dti = DatetimeIndex(dates)
```

### Step 3: Assign result = dti.to_pydatetime(...)

```python
result = dti.to_pydatetime()
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(dates, result)
```

### Step 5: Assign result = dti._mpl_repr(...)

```python
result = dti._mpl_repr()
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(dates, result)
```


## Complete Example

```python
# Workflow
dates = np.array([datetime(2000, 1, 1, tzinfo=fixed_off), datetime(2000, 1, 2, tzinfo=fixed_off), datetime(2000, 1, 3, tzinfo=fixed_off)])
dti = DatetimeIndex(dates)
result = dti.to_pydatetime()
tm.assert_numpy_array_equal(dates, result)
result = dti._mpl_repr()
tm.assert_numpy_array_equal(dates, result)
```

## Next Steps


---

*Source: test_to_pydatetime.py:37 | Complexity: Intermediate | Last updated: 2026-06-02*