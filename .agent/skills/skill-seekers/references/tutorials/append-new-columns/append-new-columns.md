# How To: Append New Columns

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test append new columns

## Prerequisites

**Required Modules:**
- `datetime`
- `itertools`
- `dateutil`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': {'x': 1, 'y': 2}, 'b': {'x': 3, 'y': 4}})
```

### Step 2: Assign row = Series(...)

```python
row = Series([5, 6, 7], index=['a', 'b', 'c'], name='z')
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': {'x': 1, 'y': 2, 'z': 5}, 'b': {'x': 3, 'y': 4, 'z': 6}, 'c': {'z': 7}})
```

### Step 4: Assign result = df._append(...)

```python
result = df._append(row)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': {'x': 1, 'y': 2}, 'b': {'x': 3, 'y': 4}})
row = Series([5, 6, 7], index=['a', 'b', 'c'], name='z')
expected = DataFrame({'a': {'x': 1, 'y': 2, 'z': 5}, 'b': {'x': 3, 'y': 4, 'z': 6}, 'c': {'z': 7}})
result = df._append(row)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_append.py:71 | Complexity: Intermediate | Last updated: 2026-06-02*