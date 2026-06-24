# How To: Left By Length Equals To Right Shape0

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test left by length equals to right shape0

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign left = DataFrame(...)

```python
left = DataFrame([['g', 'h', 1], ['g', 'h', 3]], columns=list('GHE'))
```

### Step 2: Assign right = DataFrame(...)

```python
right = DataFrame([[2, 1]], columns=list('ET'))
```

### Step 3: Assign result = merge_ordered(...)

```python
result = merge_ordered(left, right, on='E', left_by=['G', 'H'])
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'G': ['g'] * 3, 'H': ['h'] * 3, 'E': [1, 2, 3], 'T': [np.nan, 1.0, np.nan]})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
left = DataFrame([['g', 'h', 1], ['g', 'h', 3]], columns=list('GHE'))
right = DataFrame([[2, 1]], columns=list('ET'))
result = merge_ordered(left, right, on='E', left_by=['G', 'H'])
expected = DataFrame({'G': ['g'] * 3, 'H': ['h'] * 3, 'E': [1, 2, 3], 'T': [np.nan, 1.0, np.nan]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_merge_ordered.py:196 | Complexity: Intermediate | Last updated: 2026-06-02*