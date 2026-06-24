# How To: Values

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test values

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
exp = np.array([], dtype=object)
```

### Step 3: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.values, exp)
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.to_numpy(), exp)
```

### Step 5: Assign exp = np.array(...)

```python
exp = np.array([], dtype=np.int64)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.asi8, exp)
```

### Step 7: Assign idx = PeriodIndex(...)

```python
idx = PeriodIndex(['2011-01', NaT], freq='M')
```

### Step 8: Assign exp = np.array(...)

```python
exp = np.array([Period('2011-01', freq='M'), NaT], dtype=object)
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.values, exp)
```

### Step 10: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.to_numpy(), exp)
```

### Step 11: Assign exp = np.array(...)

```python
exp = np.array([492, -9223372036854775808], dtype=np.int64)
```

### Step 12: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.asi8, exp)
```

### Step 13: Assign idx = PeriodIndex(...)

```python
idx = PeriodIndex(['2011-01-01', NaT], freq='D')
```

### Step 14: Assign exp = np.array(...)

```python
exp = np.array([Period('2011-01-01', freq='D'), NaT], dtype=object)
```

### Step 15: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.values, exp)
```

### Step 16: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.to_numpy(), exp)
```

### Step 17: Assign exp = np.array(...)

```python
exp = np.array([14975, -9223372036854775808], dtype=np.int64)
```

### Step 18: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.asi8, exp)
```


## Complete Example

```python
# Workflow
idx = PeriodIndex([], freq='M')
exp = np.array([], dtype=object)
tm.assert_numpy_array_equal(idx.values, exp)
tm.assert_numpy_array_equal(idx.to_numpy(), exp)
exp = np.array([], dtype=np.int64)
tm.assert_numpy_array_equal(idx.asi8, exp)
idx = PeriodIndex(['2011-01', NaT], freq='M')
exp = np.array([Period('2011-01', freq='M'), NaT], dtype=object)
tm.assert_numpy_array_equal(idx.values, exp)
tm.assert_numpy_array_equal(idx.to_numpy(), exp)
exp = np.array([492, -9223372036854775808], dtype=np.int64)
tm.assert_numpy_array_equal(idx.asi8, exp)
idx = PeriodIndex(['2011-01-01', NaT], freq='D')
exp = np.array([Period('2011-01-01', freq='D'), NaT], dtype=object)
tm.assert_numpy_array_equal(idx.values, exp)
tm.assert_numpy_array_equal(idx.to_numpy(), exp)
exp = np.array([14975, -9223372036854775808], dtype=np.int64)
tm.assert_numpy_array_equal(idx.asi8, exp)
```

## Next Steps


---

*Source: test_period.py:36 | Complexity: Advanced | Last updated: 2026-06-02*