# How To: Float Slice Getitem With Integer Index Raises

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test float slice getitem with integer index raises

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: idx, index
```

## Step-by-Step Guide

### Step 1: Assign s = DataFrame(...)

```python
s = DataFrame(np.random.default_rng(2).standard_normal((5, 2)), index=index)
```

**Verification:**
```python
assert (result == 0).all()
```

### Step 2: Assign sc = s.copy(...)

```python
sc = s.copy()
```

### Step 3: Assign unknown = 0

```python
sc.loc[idx] = 0
```

### Step 4: Assign result = unknown.values.ravel(...)

```python
result = sc.loc[idx].values.ravel()
```

**Verification:**
```python
assert (result == 0).all()
```

### Step 5: Assign msg = value

```python
msg = f'cannot do slice indexing on {type(index).__name__} with these indexers \\[(3|4)\\.0\\] of type float'
```

### Step 6: Assign unknown = 0

```python
s[idx] = 0
```

### Step 7: s[idx]

```python
s[idx]
```


## Complete Example

```python
# Setup
# Fixtures: idx, index

# Workflow
s = DataFrame(np.random.default_rng(2).standard_normal((5, 2)), index=index)
sc = s.copy()
sc.loc[idx] = 0
result = sc.loc[idx].values.ravel()
assert (result == 0).all()
msg = f'cannot do slice indexing on {type(index).__name__} with these indexers \\[(3|4)\\.0\\] of type float'
with pytest.raises(TypeError, match=msg):
    s[idx] = 0
with pytest.raises(TypeError, match=msg):
    s[idx]
```

## Next Steps


---

*Source: test_floats.py:412 | Complexity: Intermediate | Last updated: 2026-06-02*