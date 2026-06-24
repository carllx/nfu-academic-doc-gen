# How To: Astype Object

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype object

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
tm.assert_numpy_array_equal(idx.astype(object).values, exp)
```

### Step 4: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx._mpl_repr(), exp)
```

### Step 5: Assign idx = PeriodIndex(...)

```python
idx = PeriodIndex(['2011-01', NaT], freq='M')
```

### Step 6: Assign exp = np.array(...)

```python
exp = np.array([Period('2011-01', freq='M'), NaT], dtype=object)
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.astype(object).values, exp)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx._mpl_repr(), exp)
```

### Step 9: Assign exp = np.array(...)

```python
exp = np.array([Period('2011-01-01', freq='D'), NaT], dtype=object)
```

### Step 10: Assign idx = PeriodIndex(...)

```python
idx = PeriodIndex(['2011-01-01', NaT], freq='D')
```

### Step 11: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx.astype(object).values, exp)
```

### Step 12: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(idx._mpl_repr(), exp)
```


## Complete Example

```python
# Workflow
idx = PeriodIndex([], freq='M')
exp = np.array([], dtype=object)
tm.assert_numpy_array_equal(idx.astype(object).values, exp)
tm.assert_numpy_array_equal(idx._mpl_repr(), exp)
idx = PeriodIndex(['2011-01', NaT], freq='M')
exp = np.array([Period('2011-01', freq='M'), NaT], dtype=object)
tm.assert_numpy_array_equal(idx.astype(object).values, exp)
tm.assert_numpy_array_equal(idx._mpl_repr(), exp)
exp = np.array([Period('2011-01-01', freq='D'), NaT], dtype=object)
idx = PeriodIndex(['2011-01-01', NaT], freq='D')
tm.assert_numpy_array_equal(idx.astype(object).values, exp)
tm.assert_numpy_array_equal(idx._mpl_repr(), exp)
```

## Next Steps


---

*Source: test_astype.py:65 | Complexity: Advanced | Last updated: 2026-06-02*