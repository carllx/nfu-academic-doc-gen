# How To: Insert Edges Preserves Rangeindex

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test insert edges preserves rangeindex

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
idx = Index(range(4, 9, 2))
```

### Step 2: Assign result = idx.insert(...)

```python
result = idx.insert(0, 2)
```

### Step 3: Assign expected = Index(...)

```python
expected = Index(range(2, 9, 2))
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```

### Step 5: Assign result = idx.insert(...)

```python
result = idx.insert(3, 10)
```

### Step 6: Assign expected = Index(...)

```python
expected = Index(range(4, 11, 2))
```

### Step 7: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```


## Complete Example

```python
# Workflow
idx = Index(range(4, 9, 2))
result = idx.insert(0, 2)
expected = Index(range(2, 9, 2))
tm.assert_index_equal(result, expected, exact=True)
result = idx.insert(3, 10)
expected = Index(range(4, 11, 2))
tm.assert_index_equal(result, expected, exact=True)
```

## Next Steps


---

*Source: test_range.py:91 | Complexity: Intermediate | Last updated: 2026-06-02*