# How To: Interval Array Equal Start Mismatch

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test interval array equal start mismatch

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign kwargs = value

```python
kwargs = {'periods': 4}
```

### Step 2: Assign arr1 = value

```python
arr1 = interval_range(start=0, **kwargs).values
```

### Step 3: Assign arr2 = value

```python
arr2 = interval_range(start=1, **kwargs).values
```

### Step 4: Assign msg = 'IntervalArray.left are different\n\nIntervalArray.left values are different \\(100.0 %\\)\n\\[left\\]:  \\[0, 1, 2, 3\\]\n\\[right\\]: \\[1, 2, 3, 4\\]'

```python
msg = 'IntervalArray.left are different\n\nIntervalArray.left values are different \\(100.0 %\\)\n\\[left\\]:  \\[0, 1, 2, 3\\]\n\\[right\\]: \\[1, 2, 3, 4\\]'
```

### Step 5: Call tm.assert_interval_array_equal()

```python
tm.assert_interval_array_equal(arr1, arr2)
```


## Complete Example

```python
# Workflow
kwargs = {'periods': 4}
arr1 = interval_range(start=0, **kwargs).values
arr2 = interval_range(start=1, **kwargs).values
msg = 'IntervalArray.left are different\n\nIntervalArray.left values are different \\(100.0 %\\)\n\\[left\\]:  \\[0, 1, 2, 3\\]\n\\[right\\]: \\[1, 2, 3, 4\\]'
with pytest.raises(AssertionError, match=msg):
    tm.assert_interval_array_equal(arr1, arr2)
```

## Next Steps


---

*Source: test_assert_interval_array_equal.py:68 | Complexity: Intermediate | Last updated: 2026-06-02*