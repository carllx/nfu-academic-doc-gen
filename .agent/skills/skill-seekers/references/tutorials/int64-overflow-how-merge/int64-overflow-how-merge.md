# How To: Int64 Overflow How Merge

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test int64 overflow how merge

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
# Fixtures: left_right, how
```

## Step-by-Step Guide

### Step 1: Assign unknown = left_right

```python
left, right = left_right
```

### Step 2: Assign out = merge(...)

```python
out = merge(left, right, how='outer')
```

### Step 3: Call out.sort_values()

```python
out.sort_values(out.columns.tolist(), inplace=True)
```

### Step 4: Assign out.index = np.arange(...)

```python
out.index = np.arange(len(out))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(out, merge(left, right, how=how, sort=True))
```


## Complete Example

```python
# Setup
# Fixtures: left_right, how

# Workflow
left, right = left_right
out = merge(left, right, how='outer')
out.sort_values(out.columns.tolist(), inplace=True)
out.index = np.arange(len(out))
tm.assert_frame_equal(out, merge(left, right, how=how, sort=True))
```

## Next Steps


---

*Source: test_sorting.py:222 | Complexity: Intermediate | Last updated: 2026-06-02*