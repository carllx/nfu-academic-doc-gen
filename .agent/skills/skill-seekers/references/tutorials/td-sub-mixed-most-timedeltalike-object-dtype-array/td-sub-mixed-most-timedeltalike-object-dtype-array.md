# How To: Td Sub Mixed Most Timedeltalike Object Dtype Array

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test td sub mixed most timedeltalike object dtype array

## Prerequisites

**Required Modules:**
- `datetime`
- `operator`
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core`


## Step-by-Step Guide

### Step 1: Assign now = Timestamp(...)

```python
now = Timestamp('2021-11-09 09:54:00')
```

### Step 2: Assign arr = np.array(...)

```python
arr = np.array([now, Timedelta('1D'), np.timedelta64(2, 'h')])
```

### Step 3: Assign exp = np.array(...)

```python
exp = np.array([now - Timedelta('1D'), Timedelta('0D'), np.timedelta64(2, 'h') - Timedelta('1D')])
```

### Step 4: Assign res = value

```python
res = arr - Timedelta('1D')
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, exp)
```


## Complete Example

```python
# Workflow
now = Timestamp('2021-11-09 09:54:00')
arr = np.array([now, Timedelta('1D'), np.timedelta64(2, 'h')])
exp = np.array([now - Timedelta('1D'), Timedelta('0D'), np.timedelta64(2, 'h') - Timedelta('1D')])
res = arr - Timedelta('1D')
tm.assert_numpy_array_equal(res, exp)
```

## Next Steps


---

*Source: test_arithmetic.py:255 | Complexity: Intermediate | Last updated: 2026-06-02*