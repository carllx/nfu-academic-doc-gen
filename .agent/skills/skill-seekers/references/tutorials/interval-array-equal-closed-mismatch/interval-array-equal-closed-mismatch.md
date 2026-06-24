# How To: Interval Array Equal Closed Mismatch

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test interval array equal closed mismatch

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
arr1 = interval_range(closed='left', **kwargs).values
```

### Step 3: Assign arr2 = value

```python
arr2 = interval_range(closed='right', **kwargs).values
```

### Step 4: Assign msg = 'IntervalArray are different\n\nAttribute "closed" are different\n\\[left\\]:  left\n\\[right\\]: right'

```python
msg = 'IntervalArray are different\n\nAttribute "closed" are different\n\\[left\\]:  left\n\\[right\\]: right'
```

### Step 5: Call tm.assert_interval_array_equal()

```python
tm.assert_interval_array_equal(arr1, arr2)
```


## Complete Example

```python
# Workflow
kwargs = {'start': 0, 'periods': 5}
arr1 = interval_range(closed='left', **kwargs).values
arr2 = interval_range(closed='right', **kwargs).values
msg = 'IntervalArray are different\n\nAttribute "closed" are different\n\\[left\\]:  left\n\\[right\\]: right'
with pytest.raises(AssertionError, match=msg):
    tm.assert_interval_array_equal(arr1, arr2)
```

## Next Steps


---

*Source: test_assert_interval_array_equal.py:20 | Complexity: Intermediate | Last updated: 2026-06-02*