# How To: Int64 Overflow Sort False Order

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test int64 overflow sort false order

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.algorithms`
- `pandas.core.common`
- `pandas.core.sorting`

**Setup Required:**
```python
# Fixtures: left_right
```

## Step-by-Step Guide

### Step 1: Assign unknown = left_right

```python
left, right = left_right
```

### Step 2: Assign out = merge(...)

```python
out = merge(left, right, how='left', sort=False)
```

### Step 3: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(left, out[left.columns.tolist()])
```

### Step 4: Assign out = merge(...)

```python
out = merge(right, left, how='left', sort=False)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(right, out[right.columns.tolist()])
```


## Complete Example

```python
# Setup
# Fixtures: left_right

# Workflow
left, right = left_right
out = merge(left, right, how='left', sort=False)
tm.assert_frame_equal(left, out[left.columns.tolist()])
out = merge(right, left, how='left', sort=False)
tm.assert_frame_equal(right, out[right.columns.tolist()])
```

## Next Steps


---

*Source: test_sorting.py:231 | Complexity: Intermediate | Last updated: 2026-06-02*