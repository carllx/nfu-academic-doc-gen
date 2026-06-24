# How To: Isin Datetimelike Mismatched Reso

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test isin datetimelike mismatched reso

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign expected = Series(...)

```python
expected = Series([True, True, False, False, False])
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(date_range('jan-01-2013', 'jan-05-2013'))
```

### Step 3: Assign day_values = np.asarray.astype(...)

```python
day_values = np.asarray(ser[0:2].values).astype('datetime64[D]')
```

### Step 4: Assign result = ser.isin(...)

```python
result = ser.isin(day_values)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign dta = unknown._values.astype(...)

```python
dta = ser[:2]._values.astype('M8[s]')
```

### Step 7: Assign result = ser.isin(...)

```python
result = ser.isin(dta)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
expected = Series([True, True, False, False, False])
ser = Series(date_range('jan-01-2013', 'jan-05-2013'))
day_values = np.asarray(ser[0:2].values).astype('datetime64[D]')
result = ser.isin(day_values)
tm.assert_series_equal(result, expected)
dta = ser[:2]._values.astype('M8[s]')
result = ser.isin(dta)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_isin.py:47 | Complexity: Advanced | Last updated: 2026-06-02*