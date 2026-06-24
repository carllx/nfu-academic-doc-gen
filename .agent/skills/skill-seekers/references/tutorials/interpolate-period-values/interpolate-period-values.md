# How To: Interpolate Period Values

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test interpolate period values

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign orig = Series(...)

```python
orig = Series(date_range('2012-01-01', periods=5))
```

### Step 2: Assign ser = orig.copy(...)

```python
ser = orig.copy()
```

### Step 3: Assign unknown = value

```python
ser[2] = pd.NaT
```

### Step 4: Assign ser_per = ser.dt.to_period(...)

```python
ser_per = ser.dt.to_period('D')
```

### Step 5: Assign res_per = ser_per.interpolate(...)

```python
res_per = ser_per.interpolate()
```

### Step 6: Assign expected_per = orig.dt.to_period(...)

```python
expected_per = orig.dt.to_period('D')
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res_per, expected_per)
```


## Complete Example

```python
# Workflow
orig = Series(date_range('2012-01-01', periods=5))
ser = orig.copy()
ser[2] = pd.NaT
ser_per = ser.dt.to_period('D')
res_per = ser_per.interpolate()
expected_per = orig.dt.to_period('D')
tm.assert_series_equal(res_per, expected_per)
```

## Next Steps


---

*Source: test_interpolate.py:82 | Complexity: Intermediate | Last updated: 2026-06-02*