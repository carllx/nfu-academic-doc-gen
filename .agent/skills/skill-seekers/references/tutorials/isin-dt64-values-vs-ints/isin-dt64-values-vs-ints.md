# How To: Isin Dt64 Values Vs Ints

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test isin dt64 values vs ints

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2013-01-01', '2013-01-05')
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(dti)
```

### Step 3: Assign comps = np.asarray(...)

```python
comps = np.asarray([1356998400000000000], dtype=dtype)
```

### Step 4: Assign res = dti.isin(...)

```python
res = dti.isin(comps)
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
res = ser.isin(comps)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, Series(expected))
```

### Step 9: Assign res = pd.core.algorithms.isin(...)

```python
res = pd.core.algorithms.isin(ser, comps)
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
dti = date_range('2013-01-01', '2013-01-05')
ser = Series(dti)
comps = np.asarray([1356998400000000000], dtype=dtype)
res = dti.isin(comps)
expected = np.array([False] * len(dti), dtype=bool)
tm.assert_numpy_array_equal(res, expected)
res = ser.isin(comps)
tm.assert_series_equal(res, Series(expected))
res = pd.core.algorithms.isin(ser, comps)
tm.assert_numpy_array_equal(res, expected)
```

## Next Steps


---

*Source: test_isin.py:118 | Complexity: Advanced | Last updated: 2026-06-02*