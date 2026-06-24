# How To: Pi Cmp Period

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pi cmp period

## Prerequisites

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`
- `pandas.core.arrays`
- `pandas.tests.arithmetic.common`


## Step-by-Step Guide

### Step 1: Assign idx = period_range(...)

```python
idx = period_range('2007-01', periods=20, freq='M')
```

### Step 2: Assign per = value

```python
per = idx[10]
```

### Step 3: Assign result = value

```python
result = idx < per
```

### Step 4: Assign exp = value

```python
exp = idx.values < idx.values[10]
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, exp)
```

### Step 6: Assign result = value

```python
result = idx.values.reshape(10, 2) < per
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, exp.reshape(10, 2))
```

### Step 8: Assign result = value

```python
result = idx < np.array(per)
```

### Step 9: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, exp)
```


## Complete Example

```python
# Workflow
idx = period_range('2007-01', periods=20, freq='M')
per = idx[10]
result = idx < per
exp = idx.values < idx.values[10]
tm.assert_numpy_array_equal(result, exp)
result = idx.values.reshape(10, 2) < per
tm.assert_numpy_array_equal(result, exp.reshape(10, 2))
result = idx < np.array(per)
tm.assert_numpy_array_equal(result, exp)
```

## Next Steps


---

*Source: test_period.py:210 | Complexity: Advanced | Last updated: 2026-06-02*