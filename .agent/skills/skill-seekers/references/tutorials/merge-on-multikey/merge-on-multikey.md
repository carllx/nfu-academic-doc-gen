# How To: Merge On Multikey

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test merge on multikey

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
# Fixtures: left, right, join_type
```

## Step-by-Step Guide

### Step 1: Assign on_cols = value

```python
on_cols = ['key1', 'key2']
```

### Step 2: Assign result = left.join.reset_index(...)

```python
result = left.join(right, on=on_cols, how=join_type).reset_index(drop=True)
```

### Step 3: Assign expected = merge(...)

```python
expected = merge(left, right.reset_index(), on=on_cols, how=join_type)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 5: Assign result = left.join.reset_index(...)

```python
result = left.join(right, on=on_cols, how=join_type, sort=True).reset_index(drop=True)
```

### Step 6: Assign expected = merge(...)

```python
expected = merge(left, right.reset_index(), on=on_cols, how=join_type, sort=True)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: left, right, join_type

# Workflow
on_cols = ['key1', 'key2']
result = left.join(right, on=on_cols, how=join_type).reset_index(drop=True)
expected = merge(left, right.reset_index(), on=on_cols, how=join_type)
tm.assert_frame_equal(result, expected)
result = left.join(right, on=on_cols, how=join_type, sort=True).reset_index(drop=True)
expected = merge(left, right.reset_index(), on=on_cols, how=join_type, sort=True)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_multi.py:76 | Complexity: Intermediate | Last updated: 2026-06-02*