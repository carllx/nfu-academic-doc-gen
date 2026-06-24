# How To: Reindex Preserves Names When Target Is List Or Ndarray

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reindex preserves names when target is list or ndarray

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: idx
```

## Step-by-Step Guide

### Step 1: Assign idx = idx.copy(...)

```python
idx = idx.copy()
```

**Verification:**
```python
assert idx.reindex([])[0].names == [None, None]
```

### Step 2: Assign target = idx.copy(...)

```python
target = idx.copy()
```

**Verification:**
```python
assert idx.reindex(np.array([]))[0].names == [None, None]
```

### Step 3: Assign idx.names, target.names = value

```python
idx.names = target.names = [None, None]
```

**Verification:**
```python
assert idx.reindex(target.tolist())[0].names == [None, None]
```

### Step 4: Assign other_dtype = MultiIndex.from_product(...)

```python
other_dtype = MultiIndex.from_product([[1, 2], [3, 4]])
```

**Verification:**
```python
assert idx.reindex(target.values)[0].names == [None, None]
```

### Step 5: Assign idx.names = value

```python
idx.names = ['foo', 'bar']
```

**Verification:**
```python
assert idx.reindex(other_dtype.tolist())[0].names == [None, None]
```


## Complete Example

```python
# Setup
# Fixtures: idx

# Workflow
idx = idx.copy()
target = idx.copy()
idx.names = target.names = [None, None]
other_dtype = MultiIndex.from_product([[1, 2], [3, 4]])
assert idx.reindex([])[0].names == [None, None]
assert idx.reindex(np.array([]))[0].names == [None, None]
assert idx.reindex(target.tolist())[0].names == [None, None]
assert idx.reindex(target.values)[0].names == [None, None]
assert idx.reindex(other_dtype.tolist())[0].names == [None, None]
assert idx.reindex(other_dtype.values)[0].names == [None, None]
idx.names = ['foo', 'bar']
assert idx.reindex([])[0].names == ['foo', 'bar']
assert idx.reindex(np.array([]))[0].names == ['foo', 'bar']
assert idx.reindex(target.tolist())[0].names == ['foo', 'bar']
assert idx.reindex(target.values)[0].names == ['foo', 'bar']
assert idx.reindex(other_dtype.tolist())[0].names == ['foo', 'bar']
assert idx.reindex(other_dtype.values)[0].names == ['foo', 'bar']
```

## Next Steps


---

*Source: test_reindex.py:46 | Complexity: Intermediate | Last updated: 2026-06-02*