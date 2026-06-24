# How To: Isin Period Freq Mismatch

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test isin period freq mismatch

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

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2013-01-01', '2013-01-05')
```

### Step 2: Assign pi = dti.to_period(...)

```python
pi = dti.to_period('M')
```

### Step 3: Assign ser = Series(...)

```python
ser = Series(pi)
```

### Step 4: Assign dtype = value

```python
dtype = dti.to_period('Y').dtype
```

### Step 5: Assign other = PeriodArray._simple_new(...)

```python
other = PeriodArray._simple_new(pi.asi8, dtype=dtype)
```

### Step 6: Assign res = pi.isin(...)

```python
res = pi.isin(other)
```

### Step 7: Assign expected = np.array(...)

```python
expected = np.array([False] * len(pi), dtype=bool)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, expected)
```

### Step 9: Assign res = ser.isin(...)

```python
res = ser.isin(other)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, Series(expected))
```

### Step 11: Assign res = pd.core.algorithms.isin(...)

```python
res = pd.core.algorithms.isin(ser, other)
```

### Step 12: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, expected)
```


## Complete Example

```python
# Workflow
dti = date_range('2013-01-01', '2013-01-05')
pi = dti.to_period('M')
ser = Series(pi)
dtype = dti.to_period('Y').dtype
other = PeriodArray._simple_new(pi.asi8, dtype=dtype)
res = pi.isin(other)
expected = np.array([False] * len(pi), dtype=bool)
tm.assert_numpy_array_equal(res, expected)
res = ser.isin(other)
tm.assert_series_equal(res, Series(expected))
res = pd.core.algorithms.isin(ser, other)
tm.assert_numpy_array_equal(res, expected)
```

## Next Steps


---

*Source: test_isin.py:151 | Complexity: Advanced | Last updated: 2026-06-02*