# How To: Delete Preserves Rangeindex Middle

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test delete preserves rangeindex middle

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = Index(...)

```python
idx = Index(range(3), name='foo')
```

### Step 2: Assign result = idx.delete(...)

```python
result = idx.delete(1)
```

### Step 3: Assign expected = value

```python
expected = idx[::2]
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```

### Step 5: Assign result = idx.delete(...)

```python
result = idx.delete(-2)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```


## Complete Example

```python
# Workflow
idx = Index(range(3), name='foo')
result = idx.delete(1)
expected = idx[::2]
tm.assert_index_equal(result, expected, exact=True)
result = idx.delete(-2)
tm.assert_index_equal(result, expected, exact=True)
```

## Next Steps


---

*Source: test_range.py:141 | Complexity: Intermediate | Last updated: 2026-06-02*