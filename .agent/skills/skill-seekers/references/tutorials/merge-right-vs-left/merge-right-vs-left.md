# How To: Merge Right Vs Left

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test merge right vs left

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.concat`
- `pandas.core.reshape.merge`

**Setup Required:**
```python
# Fixtures: left, right, sort
```

## Step-by-Step Guide

### Step 1: Assign on_cols = value

```python
on_cols = ['key1', 'key2']
```

### Step 2: Assign merged_left_right = left.merge(...)

```python
merged_left_right = left.merge(right, left_on=on_cols, right_index=True, how='left', sort=sort)
```

### Step 3: Assign merge_right_left = right.merge(...)

```python
merge_right_left = right.merge(left, right_on=on_cols, left_index=True, how='right', sort=sort)
```

### Step 4: Assign merge_right_left = value

```python
merge_right_left = merge_right_left[merged_left_right.columns]
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(merged_left_right, merge_right_left)
```


## Complete Example

```python
# Setup
# Fixtures: left, right, sort

# Workflow
on_cols = ['key1', 'key2']
merged_left_right = left.merge(right, left_on=on_cols, right_index=True, how='left', sort=sort)
merge_right_left = right.merge(left, right_on=on_cols, left_index=True, how='right', sort=sort)
merge_right_left = merge_right_left[merged_left_right.columns]
tm.assert_frame_equal(merged_left_right, merge_right_left)
```

## Next Steps


---

*Source: test_multi.py:161 | Complexity: Intermediate | Last updated: 2026-06-02*