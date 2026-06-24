# How To: Doc Example

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test doc example

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
left = DataFrame({'group': list('aaabbb'), 'key': ['a', 'c', 'e', 'a', 'c', 'e'], 'lvalue': [1, 2, 3] * 2})
```

### Step 2: Assign right = DataFrame(...)

```python
right = DataFrame({'key': ['b', 'c', 'd'], 'rvalue': [1, 2, 3]})
```

### Step 3: Assign result = merge_ordered(...)

```python
result = merge_ordered(left, right, fill_method='ffill', left_by='group')
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'group': list('aaaaabbbbb'), 'key': ['a', 'b', 'c', 'd', 'e'] * 2, 'lvalue': [1, 1, 2, 2, 3] * 2, 'rvalue': [np.nan, 1, 2, 3, 3] * 2})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
left = DataFrame({'group': list('aaabbb'), 'key': ['a', 'c', 'e', 'a', 'c', 'e'], 'lvalue': [1, 2, 3] * 2})
right = DataFrame({'key': ['b', 'c', 'd'], 'rvalue': [1, 2, 3]})
result = merge_ordered(left, right, fill_method='ffill', left_by='group')
expected = DataFrame({'group': list('aaaaabbbbb'), 'key': ['a', 'b', 'c', 'd', 'e'] * 2, 'lvalue': [1, 1, 2, 2, 3] * 2, 'rvalue': [np.nan, 1, 2, 3, 3] * 2})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_merge_ordered.py:110 | Complexity: Intermediate | Last updated: 2026-06-02*