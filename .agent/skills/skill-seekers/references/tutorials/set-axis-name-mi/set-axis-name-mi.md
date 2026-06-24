# How To: Set Axis Name Mi

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test set axis name mi

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `copy`
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: func
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(np.empty((3, 3)), index=MultiIndex.from_tuples([('A', x) for x in list('aBc')]), columns=MultiIndex.from_tuples([('C', x) for x in list('xyz')]))
```

**Verification:**
```python
assert result.index.names == level_names
```

### Step 2: Assign level_names = value

```python
level_names = ['L1', 'L2']
```

**Verification:**
```python
assert result.columns.names == [None, None]
```

### Step 3: Assign result = methodcaller(...)

```python
result = methodcaller(func, level_names)(df)
```

**Verification:**
```python
assert result.columns.names == ['L1', 'L2']
```

### Step 4: Assign result = methodcaller(...)

```python
result = methodcaller(func, level_names, axis=1)(df)
```

**Verification:**
```python
assert result.index.names == [None, None]
```


## Complete Example

```python
# Setup
# Fixtures: func

# Workflow
df = DataFrame(np.empty((3, 3)), index=MultiIndex.from_tuples([('A', x) for x in list('aBc')]), columns=MultiIndex.from_tuples([('C', x) for x in list('xyz')]))
level_names = ['L1', 'L2']
result = methodcaller(func, level_names)(df)
assert result.index.names == level_names
assert result.columns.names == [None, None]
result = methodcaller(func, level_names, axis=1)(df)
assert result.columns.names == ['L1', 'L2']
assert result.index.names == [None, None]
```

## Next Steps


---

*Source: test_frame.py:31 | Complexity: Intermediate | Last updated: 2026-06-02*