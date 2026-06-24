# How To: Astype Float64 To Uint64

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype float64 to uint64

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign idx = Index(...)

```python
idx = Index([0.0, 5.0, 10.0, 15.0, 20.0], dtype=np.float64)
```

### Step 2: Assign result = idx.astype(...)

```python
result = idx.astype('u8')
```

### Step 3: Assign expected = Index(...)

```python
expected = Index([0, 5, 10, 15, 20], dtype=np.uint64)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```

### Step 5: Assign idx_with_negatives = value

```python
idx_with_negatives = idx - 10
```

### Step 6: Call idx_with_negatives.astype()

```python
idx_with_negatives.astype(np.uint64)
```


## Complete Example

```python
# Workflow
idx = Index([0.0, 5.0, 10.0, 15.0, 20.0], dtype=np.float64)
result = idx.astype('u8')
expected = Index([0, 5, 10, 15, 20], dtype=np.uint64)
tm.assert_index_equal(result, expected, exact=True)
idx_with_negatives = idx - 10
with pytest.raises(ValueError, match='losslessly'):
    idx_with_negatives.astype(np.uint64)
```

## Next Steps


---

*Source: test_astype.py:13 | Complexity: Intermediate | Last updated: 2026-06-02*