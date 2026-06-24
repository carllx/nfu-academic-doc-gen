# How To: Interval Array Equal End Mismatch

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test interval array equal end mismatch

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign kwargs = value

```python
kwargs = {'start': 0, 'periods': 5}
```

### Step 2: Assign arr1 = value

```python
arr1 = interval_range(end=10, **kwargs).values
```

### Step 3: Assign arr2 = value

```python
arr2 = interval_range(end=20, **kwargs).values
```

### Step 4: Assign msg = 'IntervalArray.left are different\n\nIntervalArray.left values are different \\(80.0 %\\)\n\\[left\\]:  \\[0, 2, 4, 6, 8\\]\n\\[right\\]: \\[0, 4, 8, 12, 16\\]'

```python
msg = 'IntervalArray.left are different\n\nIntervalArray.left values are different \\(80.0 %\\)\n\\[left\\]:  \\[0, 2, 4, 6, 8\\]\n\\[right\\]: \\[0, 4, 8, 12, 16\\]'
```

### Step 5: Call tm.assert_interval_array_equal()

```python
tm.assert_interval_array_equal(arr1, arr2)
```


## Complete Example

```python
# Workflow
kwargs = {'start': 0, 'periods': 5}
arr1 = interval_range(end=10, **kwargs).values
arr2 = interval_range(end=20, **kwargs).values
msg = 'IntervalArray.left are different\n\nIntervalArray.left values are different \\(80.0 %\\)\n\\[left\\]:  \\[0, 2, 4, 6, 8\\]\n\\[right\\]: \\[0, 4, 8, 12, 16\\]'
with pytest.raises(AssertionError, match=msg):
    tm.assert_interval_array_equal(arr1, arr2)
```

## Next Steps


---

*Source: test_assert_interval_array_equal.py:52 | Complexity: Intermediate | Last updated: 2026-06-02*