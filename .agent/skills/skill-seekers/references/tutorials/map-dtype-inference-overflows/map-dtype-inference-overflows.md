# How To: Map Dtype Inference Overflows

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test map dtype inference overflows

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = Index(...)

```python
idx = Index(np.array([1, 2, 3], dtype=np.int8))
```

### Step 2: Assign result = idx.map(...)

```python
result = idx.map(lambda x: x * 1000)
```

### Step 3: Assign expected = Index(...)

```python
expected = Index([1000, 2000, 3000], dtype=np.int64)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```


## Complete Example

```python
# Workflow
idx = Index(np.array([1, 2, 3], dtype=np.int8))
result = idx.map(lambda x: x * 1000)
expected = Index([1000, 2000, 3000], dtype=np.int64)
tm.assert_index_equal(result, expected)
```

## Next Steps


---

*Source: test_numeric.py:531 | Complexity: Intermediate | Last updated: 2026-06-02*