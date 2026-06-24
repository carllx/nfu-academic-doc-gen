# How To: Get Indexer Methods

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test get indexer methods

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: reverse, expected, method
```

## Step-by-Step Guide

### Step 1: Assign index1 = Index(...)

```python
index1 = Index([1, 2, 3, 4, 5])
```

### Step 2: Assign index2 = Index(...)

```python
index2 = Index([2, 4, 6])
```

### Step 3: Assign result = index2.get_indexer(...)

```python
result = index2.get_indexer(index1, method=method)
```

### Step 4: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```

### Step 5: Assign index1 = value

```python
index1 = index1[::-1]
```

### Step 6: Assign expected = value

```python
expected = expected[::-1]
```


## Complete Example

```python
# Setup
# Fixtures: reverse, expected, method

# Workflow
index1 = Index([1, 2, 3, 4, 5])
index2 = Index([2, 4, 6])
if reverse:
    index1 = index1[::-1]
    expected = expected[::-1]
result = index2.get_indexer(index1, method=method)
tm.assert_almost_equal(result, expected)
```

## Next Steps


---

*Source: test_indexing.py:126 | Complexity: Intermediate | Last updated: 2026-06-02*