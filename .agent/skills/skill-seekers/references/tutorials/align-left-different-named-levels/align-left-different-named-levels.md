# How To: Align Left Different Named Levels

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test align left different named levels

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign left = Series(...)

```python
left = Series([2], index=pd.MultiIndex.from_tuples([(1, 4, 3)], names=['a', 'd', 'c']))
```

### Step 2: Assign right = Series(...)

```python
right = Series([1], index=pd.MultiIndex.from_tuples([(1, 2, 3)], names=['a', 'b', 'c']))
```

### Step 3: Assign unknown = left.align(...)

```python
result_left, result_right = left.align(right)
```

### Step 4: Assign expected_left = Series(...)

```python
expected_left = Series([2], index=pd.MultiIndex.from_tuples([(1, 4, 3, 2)], names=['a', 'd', 'c', 'b']))
```

### Step 5: Assign expected_right = Series(...)

```python
expected_right = Series([1], index=pd.MultiIndex.from_tuples([(1, 4, 3, 2)], names=['a', 'd', 'c', 'b']))
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result_left, expected_left)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result_right, expected_right)
```


## Complete Example

```python
# Workflow
left = Series([2], index=pd.MultiIndex.from_tuples([(1, 4, 3)], names=['a', 'd', 'c']))
right = Series([1], index=pd.MultiIndex.from_tuples([(1, 2, 3)], names=['a', 'b', 'c']))
result_left, result_right = left.align(right)
expected_left = Series([2], index=pd.MultiIndex.from_tuples([(1, 4, 3, 2)], names=['a', 'd', 'c', 'b']))
expected_right = Series([1], index=pd.MultiIndex.from_tuples([(1, 4, 3, 2)], names=['a', 'd', 'c', 'b']))
tm.assert_series_equal(result_left, expected_left)
tm.assert_series_equal(result_right, expected_right)
```

## Next Steps


---

*Source: test_align.py:245 | Complexity: Intermediate | Last updated: 2026-06-02*