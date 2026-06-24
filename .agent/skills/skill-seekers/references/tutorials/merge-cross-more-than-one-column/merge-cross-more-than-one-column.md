# How To: Merge Cross More Than One Column

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test merge cross more than one column

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.merge`


## Step-by-Step Guide

### Step 1: Assign left = DataFrame(...)

```python
left = DataFrame({'A': list('ab'), 'B': [2, 1]})
```

### Step 2: Assign right = DataFrame(...)

```python
right = DataFrame({'C': range(2), 'D': range(4, 6)})
```

### Step 3: Assign result = merge(...)

```python
result = merge(left, right, how='cross')
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': ['a', 'a', 'b', 'b'], 'B': [2, 2, 1, 1], 'C': [0, 1, 0, 1], 'D': [4, 5, 4, 5]})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
left = DataFrame({'A': list('ab'), 'B': [2, 1]})
right = DataFrame({'C': range(2), 'D': range(4, 6)})
result = merge(left, right, how='cross')
expected = DataFrame({'A': ['a', 'a', 'b', 'b'], 'B': [2, 2, 1, 1], 'C': [0, 1, 0, 1], 'D': [4, 5, 4, 5]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_merge_cross.py:61 | Complexity: Intermediate | Last updated: 2026-06-02*