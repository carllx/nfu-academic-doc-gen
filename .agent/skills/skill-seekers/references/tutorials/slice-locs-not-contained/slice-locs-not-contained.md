# How To: Slice Locs Not Contained

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test slice locs not contained

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index = MultiIndex(...)

```python
index = MultiIndex(levels=[[0, 2, 4, 6], [0, 2, 4]], codes=[[0, 0, 0, 1, 1, 2, 3, 3, 3], [0, 1, 2, 1, 2, 2, 0, 1, 2]])
```

**Verification:**
```python
assert result == (3, 6)
```

### Step 2: Assign result = index.slice_locs(...)

```python
result = index.slice_locs((1, 0), (5, 2))
```

**Verification:**
```python
assert result == (3, 6)
```

### Step 3: Assign result = index.slice_locs(...)

```python
result = index.slice_locs(1, 5)
```

**Verification:**
```python
assert result == (3, 6)
```

### Step 4: Assign result = index.slice_locs(...)

```python
result = index.slice_locs((2, 2), (5, 2))
```

**Verification:**
```python
assert result == (3, 6)
```

### Step 5: Assign result = index.slice_locs(...)

```python
result = index.slice_locs(2, 5)
```

**Verification:**
```python
assert result == (3, 8)
```

### Step 6: Assign result = index.slice_locs(...)

```python
result = index.slice_locs((1, 0), (6, 3))
```

**Verification:**
```python
assert result == (0, len(index))
```

### Step 7: Assign result = index.slice_locs(...)

```python
result = index.slice_locs(-1, 10)
```

**Verification:**
```python
assert result == (0, len(index))
```


## Complete Example

```python
# Workflow
index = MultiIndex(levels=[[0, 2, 4, 6], [0, 2, 4]], codes=[[0, 0, 0, 1, 1, 2, 3, 3, 3], [0, 1, 2, 1, 2, 2, 0, 1, 2]])
result = index.slice_locs((1, 0), (5, 2))
assert result == (3, 6)
result = index.slice_locs(1, 5)
assert result == (3, 6)
result = index.slice_locs((2, 2), (5, 2))
assert result == (3, 6)
result = index.slice_locs(2, 5)
assert result == (3, 6)
result = index.slice_locs((1, 0), (6, 3))
assert result == (3, 8)
result = index.slice_locs(-1, 10)
assert result == (0, len(index))
```

## Next Steps


---

*Source: test_indexing.py:107 | Complexity: Intermediate | Last updated: 2026-06-02*