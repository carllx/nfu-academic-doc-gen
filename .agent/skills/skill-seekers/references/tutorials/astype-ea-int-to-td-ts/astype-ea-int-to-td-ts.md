# How To: Astype Ea Int To Td Ts

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype ea int to td ts

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([1, None], dtype='Int64')
```

### Step 2: Assign result = ser.astype(...)

```python
result = ser.astype('m8[ns]')
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([1, Timedelta('nat')], dtype='m8[ns]')
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = ser.astype(...)

```python
result = ser.astype('M8[ns]')
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([1, Timedelta('nat')], dtype='M8[ns]')
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
ser = Series([1, None], dtype='Int64')
result = ser.astype('m8[ns]')
expected = Series([1, Timedelta('nat')], dtype='m8[ns]')
tm.assert_series_equal(result, expected)
result = ser.astype('M8[ns]')
expected = Series([1, Timedelta('nat')], dtype='M8[ns]')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_to_numpy.py:40 | Complexity: Intermediate | Last updated: 2026-06-02*