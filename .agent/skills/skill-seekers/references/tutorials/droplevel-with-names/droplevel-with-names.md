# How To: Droplevel With Names

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test droplevel with names

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: idx
```

## Step-by-Step Guide

### Step 1: Assign index = value

```python
index = idx[idx.get_loc('foo')]
```

**Verification:**
```python
assert dropped.name == 'second'
```

### Step 2: Assign dropped = index.droplevel(...)

```python
dropped = index.droplevel(0)
```

**Verification:**
```python
assert dropped.names == ('two', 'three')
```

### Step 3: Assign index = MultiIndex(...)

```python
index = MultiIndex(levels=[Index(range(4)), Index(range(4)), Index(range(4))], codes=[np.array([0, 0, 1, 2, 2, 2, 3, 3]), np.array([0, 1, 0, 0, 0, 1, 0, 1]), np.array([1, 0, 1, 1, 0, 0, 1, 0])], names=['one', 'two', 'three'])
```

**Verification:**
```python
assert dropped.equals(expected)
```

### Step 4: Assign dropped = index.droplevel(...)

```python
dropped = index.droplevel(0)
```

**Verification:**
```python
assert dropped.names == ('two', 'three')
```

### Step 5: Assign dropped = index.droplevel(...)

```python
dropped = index.droplevel('two')
```

### Step 6: Assign expected = index.droplevel(...)

```python
expected = index.droplevel(1)
```

**Verification:**
```python
assert dropped.equals(expected)
```


## Complete Example

```python
# Setup
# Fixtures: idx

# Workflow
index = idx[idx.get_loc('foo')]
dropped = index.droplevel(0)
assert dropped.name == 'second'
index = MultiIndex(levels=[Index(range(4)), Index(range(4)), Index(range(4))], codes=[np.array([0, 0, 1, 2, 2, 2, 3, 3]), np.array([0, 1, 0, 0, 0, 1, 0, 1]), np.array([1, 0, 1, 1, 0, 0, 1, 0])], names=['one', 'two', 'three'])
dropped = index.droplevel(0)
assert dropped.names == ('two', 'three')
dropped = index.droplevel('two')
expected = index.droplevel(1)
assert dropped.equals(expected)
```

## Next Steps


---

*Source: test_drop.py:72 | Complexity: Intermediate | Last updated: 2026-06-02*