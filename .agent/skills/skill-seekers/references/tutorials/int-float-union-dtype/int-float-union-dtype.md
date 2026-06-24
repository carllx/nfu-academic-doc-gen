# How To: Int Float Union Dtype

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test int float union dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._testing`
- `pandas.core.indexes.api`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign index = Index(...)

```python
index = Index([0, 2, 3], dtype=dtype)
```

### Step 2: Assign other = Index(...)

```python
other = Index([0.5, 1.5], dtype=np.float64)
```

### Step 3: Assign expected = Index(...)

```python
expected = Index([0.0, 0.5, 1.5, 2.0, 3.0], dtype=np.float64)
```

### Step 4: Assign result = index.union(...)

```python
result = index.union(other)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 6: Assign result = other.union(...)

```python
result = other.union(index)
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
index = Index([0, 2, 3], dtype=dtype)
other = Index([0.5, 1.5], dtype=np.float64)
expected = Index([0.0, 0.5, 1.5, 2.0, 3.0], dtype=np.float64)
result = index.union(other)
tm.assert_index_equal(result, expected)
result = other.union(index)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_setops.py:54 | Complexity: Intermediate | Last updated: 2026-06-02*