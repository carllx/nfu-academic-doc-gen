# How To: To Period 2D

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to period 2d

## Prerequisites

**Required Modules:**
- `__future__`
- `re`
- `warnings`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.tslibs.dtypes`
- `pandas.compat.numpy`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign arr2d = arr1d.reshape(...)

```python
arr2d = arr1d.reshape(1, -1)
```

### Step 2: Assign warn = value

```python
warn = None if arr1d.tz is None else UserWarning
```

### Step 3: Call tm.assert_period_array_equal()

```python
tm.assert_period_array_equal(result, expected)
```

### Step 4: Assign result = arr2d.to_period(...)

```python
result = arr2d.to_period('D')
```

### Step 5: Assign expected = arr1d.to_period.reshape(...)

```python
expected = arr1d.to_period('D').reshape(1, -1)
```


## Complete Example

```python
# Workflow
arr2d = arr1d.reshape(1, -1)
warn = None if arr1d.tz is None else UserWarning
with tm.assert_produces_warning(warn):
    result = arr2d.to_period('D')
    expected = arr1d.to_period('D').reshape(1, -1)
tm.assert_period_array_equal(result, expected)
```

## Next Steps


---

*Source: test_datetimelike.py:777 | Complexity: Intermediate | Last updated: 2026-06-02*