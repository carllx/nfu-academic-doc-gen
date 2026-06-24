# How To: Integer Values And Tz Interpreted As Utc

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test integer values and tz interpreted as utc

## Prerequisites

**Required Modules:**
- `__future__`
- `datetime`
- `functools`
- `operator`
- `dateutil`
- `dateutil.tz`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign val = np.datetime64(...)

```python
val = np.datetime64('2000-01-01 00:00:00', 'ns')
```

### Step 2: Assign values = np.array(...)

```python
values = np.array([val.view('i8')])
```

### Step 3: Assign result = DatetimeIndex.tz_localize(...)

```python
result = DatetimeIndex(values).tz_localize('US/Central')
```

### Step 4: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex(['2000-01-01T00:00:00'], dtype='M8[ns, US/Central]')
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 6: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex(['2000-01-01T00:00:00'], dtype='M8[ns, UTC]')
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 8: Assign result = DatetimeIndex(...)

```python
result = DatetimeIndex(values, tz='UTC')
```


## Complete Example

```python
# Workflow
val = np.datetime64('2000-01-01 00:00:00', 'ns')
values = np.array([val.view('i8')])
result = DatetimeIndex(values).tz_localize('US/Central')
expected = DatetimeIndex(['2000-01-01T00:00:00'], dtype='M8[ns, US/Central]')
tm.assert_index_equal(result, expected)
with tm.assert_produces_warning(None):
    result = DatetimeIndex(values, tz='UTC')
expected = DatetimeIndex(['2000-01-01T00:00:00'], dtype='M8[ns, UTC]')
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_constructors.py:585 | Complexity: Advanced | Last updated: 2026-06-02*