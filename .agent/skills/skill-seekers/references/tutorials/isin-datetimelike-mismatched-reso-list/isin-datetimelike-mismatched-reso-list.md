# How To: Isin Datetimelike Mismatched Reso List

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test isin datetimelike mismatched reso list

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

### Step 3: Assign dta = unknown._values.astype(...)

```python
dta = ser[:2]._values.astype('M8[s]')
```

### Step 4: Assign result = ser.isin(...)

```python
result = ser.isin(list(dta))
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
expected = Series([True, True, False, False, False])
ser = Series(date_range('jan-01-2013', 'jan-05-2013'))
dta = ser[:2]._values.astype('M8[s]')
result = ser.isin(list(dta))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_isin.py:61 | Complexity: Intermediate | Last updated: 2026-06-02*