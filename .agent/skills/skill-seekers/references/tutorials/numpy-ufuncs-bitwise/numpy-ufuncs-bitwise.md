# How To: Numpy Ufuncs Bitwise

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test numpy ufuncs bitwise

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.arrays`
- `pandas.core.indexes.datetimelike`

**Setup Required:**
```python
# Fixtures: func
```

## Step-by-Step Guide

### Step 1: Assign idx1 = Index(...)

```python
idx1 = Index([1, 2, 3, 4], dtype='int64')
```

### Step 2: Assign idx2 = Index(...)

```python
idx2 = Index([3, 4, 5, 6], dtype='int64')
```

### Step 3: Assign expected = Index(...)

```python
expected = Index(func(idx1.values, idx2.values))
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign result = func(...)

```python
result = func(idx1, idx2)
```


## Complete Example

```python
# Setup
# Fixtures: func

# Workflow
idx1 = Index([1, 2, 3, 4], dtype='int64')
idx2 = Index([3, 4, 5, 6], dtype='int64')
with tm.assert_produces_warning(None):
    result = func(idx1, idx2)
expected = Index(func(idx1.values, idx2.values))
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_numpy_compat.py:180 | Complexity: Intermediate | Last updated: 2026-06-02*