# How To: Droplevel List

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test droplevel list

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign index = MultiIndex(...)

```python
index = MultiIndex(levels=[Index(range(4)), Index(range(4)), Index(range(4))], codes=[np.array([0, 0, 1, 2, 2, 2, 3, 3]), np.array([0, 1, 0, 0, 0, 1, 0, 1]), np.array([1, 0, 1, 1, 0, 0, 1, 0])], names=['one', 'two', 'three'])
```

**Verification:**
```python
assert dropped.equals(expected)
```

### Step 2: Assign dropped = unknown.droplevel(...)

```python
dropped = index[:2].droplevel(['three', 'one'])
```

**Verification:**
```python
assert dropped.equals(expected)
```

### Step 3: Assign expected = unknown.droplevel.droplevel(...)

```python
expected = index[:2].droplevel(2).droplevel(0)
```

**Verification:**
```python
assert dropped.equals(expected)
```

### Step 4: Assign dropped = unknown.droplevel(...)

```python
dropped = index[:2].droplevel([])
```

### Step 5: Assign expected = value

```python
expected = index[:2]
```

**Verification:**
```python
assert dropped.equals(expected)
```

### Step 6: Assign msg = 'Cannot remove 3 levels from an index with 3 levels: at least one level must be left'

```python
msg = 'Cannot remove 3 levels from an index with 3 levels: at least one level must be left'
```

### Step 7: Call unknown.droplevel()

```python
index[:2].droplevel(['one', 'two', 'three'])
```

### Step 8: Call unknown.droplevel()

```python
index[:2].droplevel(['one', 'four'])
```


## Complete Example

```python
# Workflow
index = MultiIndex(levels=[Index(range(4)), Index(range(4)), Index(range(4))], codes=[np.array([0, 0, 1, 2, 2, 2, 3, 3]), np.array([0, 1, 0, 0, 0, 1, 0, 1]), np.array([1, 0, 1, 1, 0, 0, 1, 0])], names=['one', 'two', 'three'])
dropped = index[:2].droplevel(['three', 'one'])
expected = index[:2].droplevel(2).droplevel(0)
assert dropped.equals(expected)
dropped = index[:2].droplevel([])
expected = index[:2]
assert dropped.equals(expected)
msg = 'Cannot remove 3 levels from an index with 3 levels: at least one level must be left'
with pytest.raises(ValueError, match=msg):
    index[:2].droplevel(['one', 'two', 'three'])
with pytest.raises(KeyError, match="'Level four not found'"):
    index[:2].droplevel(['one', 'four'])
```

## Next Steps


---

*Source: test_drop.py:94 | Complexity: Advanced | Last updated: 2026-06-02*