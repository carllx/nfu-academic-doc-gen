# How To: Equality Comparison Broadcasts Over Array

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test equality comparison broadcasts over array

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign interval = Interval(...)

```python
interval = Interval(0, 1)
```

### Step 2: Assign arr = np.array(...)

```python
arr = np.array([interval, interval])
```

### Step 3: Assign result = value

```python
result = interval == arr
```

### Step 4: Assign expected = np.array(...)

```python
expected = np.array([True, True])
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(result, expected)
```


## Complete Example

```python
# Workflow
interval = Interval(0, 1)
arr = np.array([interval, interval])
result = interval == arr
expected = np.array([True, True])
tm.assert_numpy_array_equal(result, expected)
```

## Next Steps


---

*Source: test_arithmetic.py:186 | Complexity: Intermediate | Last updated: 2026-06-02*