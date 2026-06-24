# How To: View I8 To Datetimelike

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test view i8 to datetimelike

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2000', periods=4, tz='US/Central')
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(dti.asi8)
```

### Step 3: Assign result = ser.view(...)

```python
result = ser.view(dti.dtype)
```

### Step 4: Call tm.assert_datetime_array_equal()

```python
tm.assert_datetime_array_equal(result._values, dti._data._with_freq(None))
```

### Step 5: Assign pi = dti.tz_localize.to_period(...)

```python
pi = dti.tz_localize(None).to_period('D')
```

### Step 6: Assign ser = Series(...)

```python
ser = Series(pi.asi8)
```

### Step 7: Assign result = ser.view(...)

```python
result = ser.view(pi.dtype)
```

### Step 8: Call tm.assert_period_array_equal()

```python
tm.assert_period_array_equal(result._values, pi._data)
```


## Complete Example

```python
# Workflow
dti = date_range('2000', periods=4, tz='US/Central')
ser = Series(dti.asi8)
result = ser.view(dti.dtype)
tm.assert_datetime_array_equal(result._values, dti._data._with_freq(None))
pi = dti.tz_localize(None).to_period('D')
ser = Series(pi.asi8)
result = ser.view(pi.dtype)
tm.assert_period_array_equal(result._values, pi._data)
```

## Next Steps


---

*Source: test_view.py:18 | Complexity: Advanced | Last updated: 2026-06-02*