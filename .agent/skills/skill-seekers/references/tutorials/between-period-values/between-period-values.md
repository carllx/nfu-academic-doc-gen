# How To: Between Period Values

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test between period values

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series(period_range('2000-01-01', periods=10, freq='D'))
```

### Step 2: Assign unknown = value

```python
left, right = ser[[2, 7]]
```

### Step 3: Assign result = ser.between(...)

```python
result = ser.between(left, right)
```

### Step 4: Assign expected = value

```python
expected = (ser >= left) & (ser <= right)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
ser = Series(period_range('2000-01-01', periods=10, freq='D'))
left, right = ser[[2, 7]]
result = ser.between(left, right)
expected = (ser >= left) & (ser <= right)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_between.py:34 | Complexity: Intermediate | Last updated: 2026-06-02*