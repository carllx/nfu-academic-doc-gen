# How To: View Asi8

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test view asi8

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = PeriodIndex(...)

```python
idx = PeriodIndex([], freq='M')
```

### Step 2: Assign exp = np.array(...)

```python
exp = np.array([], dtype=np.int64)
```

### Step 3: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.view('i8'), exp)
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.asi8, exp)
```

### Step 5: Assign idx = PeriodIndex(...)

```python
idx = PeriodIndex(['2011-01', NaT], freq='M')
```

### Step 6: Assign exp = np.array(...)

```python
exp = np.array([492, -9223372036854775808], dtype=np.int64)
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.view('i8'), exp)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.asi8, exp)
```

### Step 9: Assign exp = np.array(...)

```python
exp = np.array([14975, -9223372036854775808], dtype=np.int64)
```

### Step 10: Assign idx = PeriodIndex(...)

```python
idx = PeriodIndex(['2011-01-01', NaT], freq='D')
```

### Step 11: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.view('i8'), exp)
```

### Step 12: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.asi8, exp)
```


## Complete Example

```python
# Workflow
idx = PeriodIndex([], freq='M')
exp = np.array([], dtype=np.int64)
tm.assert_numpy_array_equal(idx.view('i8'), exp)
tm.assert_numpy_array_equal(idx.asi8, exp)
idx = PeriodIndex(['2011-01', NaT], freq='M')
exp = np.array([492, -9223372036854775808], dtype=np.int64)
tm.assert_numpy_array_equal(idx.view('i8'), exp)
tm.assert_numpy_array_equal(idx.asi8, exp)
exp = np.array([14975, -9223372036854775808], dtype=np.int64)
idx = PeriodIndex(['2011-01-01', NaT], freq='D')
tm.assert_numpy_array_equal(idx.view('i8'), exp)
tm.assert_numpy_array_equal(idx.asi8, exp)
```

## Next Steps


---

*Source: test_period.py:18 | Complexity: Advanced | Last updated: 2026-06-02*