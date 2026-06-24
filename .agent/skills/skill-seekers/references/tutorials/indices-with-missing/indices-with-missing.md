# How To: Indices With Missing

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test indices with missing

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 1, np.nan], 'b': [2, 3, 4], 'c': [5, 6, 7]})
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign g = df.groupby(...)

```python
g = df.groupby(['a', 'b'])
```

### Step 3: Assign result = value

```python
result = g.indices
```

### Step 4: Assign expected = value

```python
expected = {(1.0, 2): np.array([0]), (1.0, 3): np.array([1])}
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
df = DataFrame({'a': [1, 1, np.nan], 'b': [2, 3, 4], 'c': [5, 6, 7]})
g = df.groupby(['a', 'b'])
result = g.indices
expected = {(1.0, 2): np.array([0]), (1.0, 3): np.array([1])}
assert result == expected
```

## Next Steps


---

*Source: test_missing.py:157 | Complexity: Intermediate | Last updated: 2026-06-02*