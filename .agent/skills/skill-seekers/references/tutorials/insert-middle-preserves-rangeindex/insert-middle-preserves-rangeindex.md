# How To: Insert Middle Preserves Rangeindex

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test insert middle preserves rangeindex

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
idx = Index(range(0, 3, 2))
```

### Step 2: Assign result = idx.insert(...)

```python
result = idx.insert(1, 1)
```

### Step 3: Assign expected = Index(...)

```python
expected = Index(range(3))
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```

### Step 5: Assign idx = value

```python
idx = idx * 2
```

### Step 6: Assign result = idx.insert(...)

```python
result = idx.insert(1, 2)
```

### Step 7: Assign expected = value

```python
expected = expected * 2
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```


## Complete Example

```python
# Workflow
idx = Index(range(0, 3, 2))
result = idx.insert(1, 1)
expected = Index(range(3))
tm.assert_index_equal(result, expected, exact=True)
idx = idx * 2
result = idx.insert(1, 2)
expected = expected * 2
tm.assert_index_equal(result, expected, exact=True)
```

## Next Steps


---

*Source: test_range.py:102 | Complexity: Advanced | Last updated: 2026-06-02*