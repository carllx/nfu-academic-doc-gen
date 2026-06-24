# How To: Merge Cross

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test merge cross

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.merge`

**Setup Required:**
```python
# Fixtures: input_col, output_cols
```

## Step-by-Step Guide

### Step 1: Assign left = DataFrame(...)

```python
left = DataFrame({'a': [1, 3]})
```

### Step 2: Assign right = DataFrame(...)

```python
right = DataFrame({input_col: [3, 4]})
```

### Step 3: Assign left_copy = left.copy(...)

```python
left_copy = left.copy()
```

### Step 4: Assign right_copy = right.copy(...)

```python
right_copy = right.copy()
```

### Step 5: Assign result = merge(...)

```python
result = merge(left, right, how='cross')
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame({output_cols[0]: [1, 1, 3, 3], output_cols[1]: [3, 4, 3, 4]})
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(left, left_copy)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(right, right_copy)
```


## Complete Example

```python
# Setup
# Fixtures: input_col, output_cols

# Workflow
left = DataFrame({'a': [1, 3]})
right = DataFrame({input_col: [3, 4]})
left_copy = left.copy()
right_copy = right.copy()
result = merge(left, right, how='cross')
expected = DataFrame({output_cols[0]: [1, 1, 3, 3], output_cols[1]: [3, 4, 3, 4]})
tm.assert_frame_equal(result, expected)
tm.assert_frame_equal(left, left_copy)
tm.assert_frame_equal(right, right_copy)
```

## Next Steps


---

*Source: test_merge_cross.py:17 | Complexity: Advanced | Last updated: 2026-06-02*