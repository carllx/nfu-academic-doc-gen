# How To: Td Add Mixed Timedeltalike Object Dtype Array

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test td add mixed timedeltalike object dtype array

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: op
```

## Step-by-Step Guide

### Step 1: Assign now = Timestamp(...)

```python
now = Timestamp('2021-11-09 09:54:00')
```

### Step 2: Assign arr = np.array(...)

```python
arr = np.array([now, Timedelta('1D')])
```

### Step 3: Assign exp = np.array(...)

```python
exp = np.array([now + Timedelta('1D'), Timedelta('2D')])
```

### Step 4: Assign res = op(...)

```python
res = op(arr, Timedelta('1D'))
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res, exp)
```


## Complete Example

```python
# Setup
# Fixtures: op

# Workflow
now = Timestamp('2021-11-09 09:54:00')
arr = np.array([now, Timedelta('1D')])
exp = np.array([now + Timedelta('1D'), Timedelta('2D')])
res = op(arr, Timedelta('1D'))
tm.assert_numpy_array_equal(res, exp)
```

## Next Steps


---

*Source: test_arithmetic.py:286 | Complexity: Intermediate | Last updated: 2026-06-02*