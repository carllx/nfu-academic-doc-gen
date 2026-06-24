# How To: Union Sort Special True

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test union sort special true

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
# Fixtures: slice_
```

## Step-by-Step Guide

### Step 1: Assign idx = Index(...)

```python
idx = Index([1, 0, 2])
```

### Step 2: Assign other = value

```python
other = idx[slice_]
```

### Step 3: Assign result = idx.union(...)

```python
result = idx.union(other, sort=True)
```

### Step 4: Assign expected = Index(...)

```python
expected = Index([0, 1, 2])
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: slice_

# Workflow
idx = Index([1, 0, 2])
other = idx[slice_]
result = idx.union(other, sort=True)
expected = Index([0, 1, 2])
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_setops.py:161 | Complexity: Intermediate | Last updated: 2026-06-02*