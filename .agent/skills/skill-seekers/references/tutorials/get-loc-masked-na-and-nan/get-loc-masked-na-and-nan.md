# How To: Get Loc Masked Na And Nan

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test get loc masked na and nan

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign idx = Index(...)

```python
idx = Index(FloatingArray(np.array([1, 2, 1, np.nan]), mask=np.array([False, False, True, False])))
```

**Verification:**
```python
assert result == 2
```

### Step 2: Assign result = idx.get_loc(...)

```python
result = idx.get_loc(NA)
```

**Verification:**
```python
assert result == 3
```

### Step 3: Assign result = idx.get_loc(...)

```python
result = idx.get_loc(np.nan)
```

**Verification:**
```python
assert result == 2
```

### Step 4: Assign idx = Index(...)

```python
idx = Index(FloatingArray(np.array([1, 2, 1.0]), mask=np.array([False, False, True])))
```

**Verification:**
```python
assert result == 2
```

### Step 5: Assign result = idx.get_loc(...)

```python
result = idx.get_loc(NA)
```

**Verification:**
```python
assert result == 2
```

### Step 6: Assign idx = Index(...)

```python
idx = Index(FloatingArray(np.array([1, 2, np.nan]), mask=np.array([False, False, False])))
```

### Step 7: Assign result = idx.get_loc(...)

```python
result = idx.get_loc(np.nan)
```

**Verification:**
```python
assert result == 2
```

### Step 8: Call idx.get_loc()

```python
idx.get_loc(np.nan)
```

### Step 9: Call idx.get_loc()

```python
idx.get_loc(NA)
```


## Complete Example

```python
# Workflow
idx = Index(FloatingArray(np.array([1, 2, 1, np.nan]), mask=np.array([False, False, True, False])))
result = idx.get_loc(NA)
assert result == 2
result = idx.get_loc(np.nan)
assert result == 3
idx = Index(FloatingArray(np.array([1, 2, 1.0]), mask=np.array([False, False, True])))
result = idx.get_loc(NA)
assert result == 2
with pytest.raises(KeyError, match='nan'):
    idx.get_loc(np.nan)
idx = Index(FloatingArray(np.array([1, 2, np.nan]), mask=np.array([False, False, False])))
result = idx.get_loc(np.nan)
assert result == 2
with pytest.raises(KeyError, match='NA'):
    idx.get_loc(NA)
```

## Next Steps


---

*Source: test_indexing.py:346 | Complexity: Advanced | Last updated: 2026-06-02*