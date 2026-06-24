# How To: Sort Index Multi Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test sort index multi index

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [3, 1, 2], 'b': [0, 0, 0], 'c': [0, 1, 2], 'd': list('abc')})
```

### Step 2: Assign result = df.set_index.sort_index(...)

```python
result = df.set_index(list('abc')).sort_index(level=list('ba'))
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1, 2, 3], 'b': [0, 0, 0], 'c': [1, 2, 0], 'd': list('bca')})
```

### Step 4: Assign expected = expected.set_index(...)

```python
expected = expected.set_index(list('abc'))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [3, 1, 2], 'b': [0, 0, 0], 'c': [0, 1, 2], 'd': list('abc')})
result = df.set_index(list('abc')).sort_index(level=list('ba'))
expected = DataFrame({'a': [1, 2, 3], 'b': [0, 0, 0], 'c': [1, 2, 0], 'd': list('bca')})
expected = expected.set_index(list('abc'))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_sort_index.py:204 | Complexity: Intermediate | Last updated: 2026-06-02*