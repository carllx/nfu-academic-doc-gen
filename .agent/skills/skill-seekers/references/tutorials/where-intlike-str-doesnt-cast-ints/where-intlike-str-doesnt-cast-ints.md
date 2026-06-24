# How To: Where Intlike Str Doesnt Cast Ints

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test where intlike str doesnt cast ints

## Prerequisites

**Required Modules:**
- `numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = Index(...)

```python
idx = Index(range(3))
```

### Step 2: Assign mask = np.array(...)

```python
mask = np.array([True, False, True])
```

### Step 3: Assign res = idx.where(...)

```python
res = idx.where(mask, '2')
```

### Step 4: Assign expected = Index(...)

```python
expected = Index([0, '2', 2])
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, expected)
```


## Complete Example

```python
# Workflow
idx = Index(range(3))
mask = np.array([True, False, True])
res = idx.where(mask, '2')
expected = Index([0, '2', 2])
tm.assert_index_equal(res, expected)
```

## Next Steps


---

*Source: test_where.py:8 | Complexity: Intermediate | Last updated: 2026-06-02*