# How To: Interval Array Equal Periods Mismatch

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test interval array equal periods mismatch

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign kwargs = value

```python
kwargs = {'start': 0}
```

### Step 2: Assign arr1 = value

```python
arr1 = interval_range(periods=5, **kwargs).values
```

### Step 3: Assign arr2 = value

```python
arr2 = interval_range(periods=6, **kwargs).values
```

### Step 4: Assign msg = 'IntervalArray.left are different\n\nIntervalArray.left shapes are different\n\\[left\\]:  \\(5,\\)\n\\[right\\]: \\(6,\\)'

```python
msg = 'IntervalArray.left are different\n\nIntervalArray.left shapes are different\n\\[left\\]:  \\(5,\\)\n\\[right\\]: \\(6,\\)'
```

### Step 5: Call tm.assert_interval_array_equal()

```python
tm.assert_interval_array_equal(arr1, arr2)
```


## Complete Example

```python
# Workflow
kwargs = {'start': 0}
arr1 = interval_range(periods=5, **kwargs).values
arr2 = interval_range(periods=6, **kwargs).values
msg = 'IntervalArray.left are different\n\nIntervalArray.left shapes are different\n\\[left\\]:  \\(5,\\)\n\\[right\\]: \\(6,\\)'
with pytest.raises(AssertionError, match=msg):
    tm.assert_interval_array_equal(arr1, arr2)
```

## Next Steps


---

*Source: test_assert_interval_array_equal.py:36 | Complexity: Intermediate | Last updated: 2026-06-02*