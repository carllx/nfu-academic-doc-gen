# How To: Equals Multi

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test equals multi

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: idx
```

## Step-by-Step Guide

### Step 1: Assign index = MultiIndex(...)

```python
index = MultiIndex(levels=[Index(list(range(4))), Index(list(range(4))), Index(list(range(4)))], codes=[np.array([0, 0, 1, 2, 2, 2, 3, 3]), np.array([0, 1, 0, 0, 0, 1, 0, 1]), np.array([1, 0, 1, 1, 0, 0, 1, 0])])
```

**Verification:**
```python
assert idx.equals(idx)
```

### Step 2: Assign index2 = MultiIndex(...)

```python
index2 = MultiIndex(levels=index.levels[:-1], codes=index.codes[:-1])
```

**Verification:**
```python
assert not idx.equals(idx.values)
```

### Step 3: Assign major_axis = Index(...)

```python
major_axis = Index(list(range(4)))
```

**Verification:**
```python
assert idx.equals(Index(idx.values))
```

### Step 4: Assign minor_axis = Index(...)

```python
minor_axis = Index(list(range(2)))
```

**Verification:**
```python
assert idx.equal_levels(idx)
```

### Step 5: Assign major_codes = np.array(...)

```python
major_codes = np.array([0, 0, 1, 2, 2, 3])
```

**Verification:**
```python
assert not idx.equals(idx[:-1])
```

### Step 6: Assign minor_codes = np.array(...)

```python
minor_codes = np.array([0, 1, 0, 0, 1, 0])
```

**Verification:**
```python
assert not idx.equals(idx[-1])
```

### Step 7: Assign index = MultiIndex(...)

```python
index = MultiIndex(levels=[major_axis, minor_axis], codes=[major_codes, minor_codes])
```

**Verification:**
```python
assert not index.equals(index2)
```

### Step 8: Assign major_axis = Index(...)

```python
major_axis = Index(['foo', 'bar', 'baz', 'qux'])
```

**Verification:**
```python
assert not index.equal_levels(index2)
```

### Step 9: Assign minor_axis = Index(...)

```python
minor_axis = Index(['one', 'two'])
```

**Verification:**
```python
assert not idx.equals(index)
```

### Step 10: Assign major_codes = np.array(...)

```python
major_codes = np.array([0, 0, 2, 2, 3, 3])
```

**Verification:**
```python
assert not idx.equal_levels(index)
```

### Step 11: Assign minor_codes = np.array(...)

```python
minor_codes = np.array([0, 1, 0, 1, 0, 1])
```

**Verification:**
```python
assert not idx.equals(index)
```

### Step 12: Assign index = MultiIndex(...)

```python
index = MultiIndex(levels=[major_axis, minor_axis], codes=[major_codes, minor_codes])
```

**Verification:**
```python
assert not idx.equals(index)
```


## Complete Example

```python
# Setup
# Fixtures: idx

# Workflow
assert idx.equals(idx)
assert not idx.equals(idx.values)
assert idx.equals(Index(idx.values))
assert idx.equal_levels(idx)
assert not idx.equals(idx[:-1])
assert not idx.equals(idx[-1])
index = MultiIndex(levels=[Index(list(range(4))), Index(list(range(4))), Index(list(range(4)))], codes=[np.array([0, 0, 1, 2, 2, 2, 3, 3]), np.array([0, 1, 0, 0, 0, 1, 0, 1]), np.array([1, 0, 1, 1, 0, 0, 1, 0])])
index2 = MultiIndex(levels=index.levels[:-1], codes=index.codes[:-1])
assert not index.equals(index2)
assert not index.equal_levels(index2)
major_axis = Index(list(range(4)))
minor_axis = Index(list(range(2)))
major_codes = np.array([0, 0, 1, 2, 2, 3])
minor_codes = np.array([0, 1, 0, 0, 1, 0])
index = MultiIndex(levels=[major_axis, minor_axis], codes=[major_codes, minor_codes])
assert not idx.equals(index)
assert not idx.equal_levels(index)
major_axis = Index(['foo', 'bar', 'baz', 'qux'])
minor_axis = Index(['one', 'two'])
major_codes = np.array([0, 0, 2, 2, 3, 3])
minor_codes = np.array([0, 1, 0, 1, 0, 1])
index = MultiIndex(levels=[major_axis, minor_axis], codes=[major_codes, minor_codes])
assert not idx.equals(index)
```

## Next Steps


---

*Source: test_equivalence.py:135 | Complexity: Advanced | Last updated: 2026-06-02*