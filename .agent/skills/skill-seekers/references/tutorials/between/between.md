# How To: Between

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test between

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign series = Series(...)

```python
series = Series(date_range('1/1/2000', periods=10))
```

### Step 2: Assign unknown = value

```python
left, right = series[[2, 7]]
```

### Step 3: Assign result = series.between(...)

```python
result = series.between(left, right)
```

### Step 4: Assign expected = value

```python
expected = (series >= left) & (series <= right)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
series = Series(date_range('1/1/2000', periods=10))
left, right = series[[2, 7]]
result = series.between(left, right)
expected = (series >= left) & (series <= right)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_between.py:14 | Complexity: Intermediate | Last updated: 2026-06-02*