# How To: Truncate Multiindex

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test truncate multiindex

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign major_axis = Index(...)

```python
major_axis = Index(list(range(4)))
```

**Verification:**
```python
assert 'foo' not in result.levels[0]
```

### Step 2: Assign minor_axis = Index(...)

```python
minor_axis = Index(list(range(2)))
```

**Verification:**
```python
assert 1 in result.levels[0]
```

### Step 3: Assign major_codes = np.array(...)

```python
major_codes = np.array([0, 0, 1, 2, 3, 3])
```

**Verification:**
```python
assert index.names == result.names
```

### Step 4: Assign minor_codes = np.array(...)

```python
minor_codes = np.array([0, 1, 0, 1, 0, 1])
```

**Verification:**
```python
assert 2 not in result.levels[0]
```

### Step 5: Assign index = MultiIndex(...)

```python
index = MultiIndex(levels=[major_axis, minor_axis], codes=[major_codes, minor_codes], names=['L1', 'L2'])
```

**Verification:**
```python
assert 1 in result.levels[0]
```

### Step 6: Assign result = index.truncate(...)

```python
result = index.truncate(before=1)
```

**Verification:**
```python
assert index.names == result.names
```

### Step 7: Assign result = index.truncate(...)

```python
result = index.truncate(after=1)
```

**Verification:**
```python
assert len(result.levels[0]) == 2
```

### Step 8: Assign result = index.truncate(...)

```python
result = index.truncate(before=1, after=2)
```

**Verification:**
```python
assert index.names == result.names
```

### Step 9: Assign msg = 'after < before'

```python
msg = 'after < before'
```

### Step 10: Call index.truncate()

```python
index.truncate(3, 1)
```


## Complete Example

```python
# Workflow
major_axis = Index(list(range(4)))
minor_axis = Index(list(range(2)))
major_codes = np.array([0, 0, 1, 2, 3, 3])
minor_codes = np.array([0, 1, 0, 1, 0, 1])
index = MultiIndex(levels=[major_axis, minor_axis], codes=[major_codes, minor_codes], names=['L1', 'L2'])
result = index.truncate(before=1)
assert 'foo' not in result.levels[0]
assert 1 in result.levels[0]
assert index.names == result.names
result = index.truncate(after=1)
assert 2 not in result.levels[0]
assert 1 in result.levels[0]
assert index.names == result.names
result = index.truncate(before=1, after=2)
assert len(result.levels[0]) == 2
assert index.names == result.names
msg = 'after < before'
with pytest.raises(ValueError, match=msg):
    index.truncate(3, 1)
```

## Next Steps


---

*Source: test_analytics.py:43 | Complexity: Advanced | Last updated: 2026-06-02*