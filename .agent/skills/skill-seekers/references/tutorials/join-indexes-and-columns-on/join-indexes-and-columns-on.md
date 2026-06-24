# How To: Join Indexes And Columns On

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test join indexes and columns on

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: df1, df2, left_index, join_type
```

## Step-by-Step Guide

### Step 1: Assign left_df = df1.set_index(...)

```python
left_df = df1.set_index(left_index)
```

### Step 2: Assign right_df = df2.set_index(...)

```python
right_df = df2.set_index(['outer', 'inner'])
```

### Step 3: Assign expected = left_df.reset_index.join.set_index(...)

```python
expected = left_df.reset_index().join(right_df, on=['outer', 'inner'], how=join_type, lsuffix='_x', rsuffix='_y').set_index(left_index)
```

### Step 4: Assign result = left_df.join(...)

```python
result = left_df.join(right_df, on=['outer', 'inner'], how=join_type, lsuffix='_x', rsuffix='_y')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected, check_like=True)
```


## Complete Example

```python
# Setup
# Fixtures: df1, df2, left_index, join_type

# Workflow
left_df = df1.set_index(left_index)
right_df = df2.set_index(['outer', 'inner'])
expected = left_df.reset_index().join(right_df, on=['outer', 'inner'], how=join_type, lsuffix='_x', rsuffix='_y').set_index(left_index)
result = left_df.join(right_df, on=['outer', 'inner'], how=join_type, lsuffix='_x', rsuffix='_y')
tm.assert_frame_equal(result, expected, check_like=True)
```

## Next Steps


---

*Source: test_merge_index_as_string.py:165 | Complexity: Intermediate | Last updated: 2026-06-02*