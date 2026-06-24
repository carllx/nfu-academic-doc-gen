# How To: Astype Float64 To Int Dtype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test astype float64 to int dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign idx = Index(...)

```python
idx = Index([0, 1, 2], dtype=np.float64)
```

### Step 2: Assign result = idx.astype(...)

```python
result = idx.astype(dtype)
```

### Step 3: Assign expected = Index(...)

```python
expected = Index([0, 1, 2], dtype=dtype)
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```

### Step 5: Assign idx = Index(...)

```python
idx = Index([0, 1.1, 2], dtype=np.float64)
```

### Step 6: Assign result = idx.astype(...)

```python
result = idx.astype(dtype)
```

### Step 7: Assign expected = Index(...)

```python
expected = Index([0, 1, 2], dtype=dtype)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected, exact=True)
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
idx = Index([0, 1, 2], dtype=np.float64)
result = idx.astype(dtype)
expected = Index([0, 1, 2], dtype=dtype)
tm.assert_index_equal(result, expected, exact=True)
idx = Index([0, 1.1, 2], dtype=np.float64)
result = idx.astype(dtype)
expected = Index([0, 1, 2], dtype=dtype)
tm.assert_index_equal(result, expected, exact=True)
```

## Next Steps


---

*Source: test_astype.py:41 | Complexity: Advanced | Last updated: 2026-06-02*