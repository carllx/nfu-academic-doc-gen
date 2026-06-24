# How To: Merge Duplicate Suffix

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test merge duplicate suffix

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.concat`
- `pandas.core.reshape.merge`

**Setup Required:**
```python
# Fixtures: how, expected
```

## Step-by-Step Guide

### Step 1: Assign left_df = DataFrame(...)

```python
left_df = DataFrame({'A': [100, 200, 1], 'B': [60, 70, 80]})
```

### Step 2: Assign right_df = DataFrame(...)

```python
right_df = DataFrame({'A': [100, 200, 300], 'B': [600, 700, 800]})
```

### Step 3: Assign result = merge(...)

```python
result = merge(left_df, right_df, on='A', how=how, suffixes=('_x', '_x'))
```

### Step 4: Assign expected.columns = value

```python
expected.columns = ['A', 'B_x', 'B_x']
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: how, expected

# Workflow
left_df = DataFrame({'A': [100, 200, 1], 'B': [60, 70, 80]})
right_df = DataFrame({'A': [100, 200, 300], 'B': [600, 700, 800]})
result = merge(left_df, right_df, on='A', how=how, suffixes=('_x', '_x'))
expected.columns = ['A', 'B_x', 'B_x']
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_merge.py:2366 | Complexity: Intermediate | Last updated: 2026-06-02*