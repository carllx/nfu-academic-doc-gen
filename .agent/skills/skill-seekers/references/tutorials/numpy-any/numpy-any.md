# How To: Numpy Any

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test numpy any

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas.core.arrays.sparse`

**Setup Required:**
```python
# Fixtures: data, pos, neg
```

## Step-by-Step Guide

### Step 1: Assign out = np.any(...)

```python
out = np.any(SparseArray(data))
```

**Verification:**
```python
assert out
```

### Step 2: Assign out = np.any(...)

```python
out = np.any(SparseArray(data, fill_value=pos))
```

**Verification:**
```python
assert out
```

### Step 3: Assign unknown = neg

```python
data[1] = neg
```

**Verification:**
```python
assert not out
```

### Step 4: Assign out = np.any(...)

```python
out = np.any(SparseArray(data))
```

**Verification:**
```python
assert not out
```

### Step 5: Assign out = np.any(...)

```python
out = np.any(SparseArray(data, fill_value=pos))
```

**Verification:**
```python
assert not out
```

### Step 6: Assign msg = "the 'out' parameter is not supported"

```python
msg = "the 'out' parameter is not supported"
```

### Step 7: Call np.any()

```python
np.any(SparseArray(data), out=out)
```


## Complete Example

```python
# Setup
# Fixtures: data, pos, neg

# Workflow
out = np.any(SparseArray(data))
assert out
out = np.any(SparseArray(data, fill_value=pos))
assert out
data[1] = neg
out = np.any(SparseArray(data))
assert not out
out = np.any(SparseArray(data, fill_value=pos))
assert not out
msg = "the 'out' parameter is not supported"
with pytest.raises(ValueError, match=msg):
    np.any(SparseArray(data), out=out)
```

## Next Steps


---

*Source: test_reductions.py:96 | Complexity: Intermediate | Last updated: 2026-06-02*