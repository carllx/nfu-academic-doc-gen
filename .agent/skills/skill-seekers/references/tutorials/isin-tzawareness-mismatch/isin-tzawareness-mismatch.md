# How To: Isin Tzawareness Mismatch

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test isin tzawareness mismatch

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

### Step 2: Assign ser = Series(...)

```python
ser = Series(dti)
```

### Step 3: Assign other = dti.tz_localize(...)

```python
other = dti.tz_localize('UTC')
```

### Step 4: Assign res = dti.isin(...)

```python
res = dti.isin(other)
```

### Step 5: Assign expected = np.array(...)

```python
expected = np.array([False] * len(dti), dtype=bool)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, expected)
```

### Step 7: Assign res = ser.isin(...)

```python
res = ser.isin(other)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, Series(expected))
```

### Step 9: Assign res = pd.core.algorithms.isin(...)

```python
res = pd.core.algorithms.isin(ser, other)
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, expected)
```


## Complete Example

```python
# Workflow
dti = date_range('2013-01-01', '2013-01-05')
ser = Series(dti)
other = dti.tz_localize('UTC')
res = dti.isin(other)
expected = np.array([False] * len(dti), dtype=bool)
tm.assert_numpy_array_equal(res, expected)
res = ser.isin(other)
tm.assert_series_equal(res, Series(expected))
res = pd.core.algorithms.isin(ser, other)
tm.assert_numpy_array_equal(res, expected)
```

## Next Steps


---

*Source: test_isin.py:135 | Complexity: Advanced | Last updated: 2026-06-02*