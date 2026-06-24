# How To: Merge Asof Read Only Ndarray

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test merge asof read only ndarray

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.merge`


## Step-by-Step Guide

### Step 1: Assign left = pd.Series(...)

```python
left = pd.Series([2], index=[2], name='left')
```

### Step 2: Assign right = pd.Series(...)

```python
right = pd.Series([1], index=[1], name='right')
```

### Step 3: Assign left.index.values.flags.writeable = False

```python
left.index.values.flags.writeable = False
```

### Step 4: Assign right.index.values.flags.writeable = False

```python
right.index.values.flags.writeable = False
```

### Step 5: Assign result = merge_asof(...)

```python
result = merge_asof(left, right, left_index=True, right_index=True)
```

### Step 6: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'left': [2], 'right': [1]}, index=[2])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
left = pd.Series([2], index=[2], name='left')
right = pd.Series([1], index=[1], name='right')
left.index.values.flags.writeable = False
right.index.values.flags.writeable = False
result = merge_asof(left, right, left_index=True, right_index=True)
expected = pd.DataFrame({'left': [2], 'right': [1]}, index=[2])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_merge_asof.py:3607 | Complexity: Intermediate | Last updated: 2026-06-02*