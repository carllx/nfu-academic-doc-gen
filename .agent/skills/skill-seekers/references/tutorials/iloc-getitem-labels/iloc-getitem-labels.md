# How To: Iloc Getitem Labels

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test iloc getitem labels

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign arr = np.random.default_rng.standard_normal(...)

```python
arr = np.random.default_rng(2).standard_normal((4, 3))
```

**Verification:**
```python
assert result == expected
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(arr, columns=[['i', 'i', 'j'], ['A', 'A', 'B']], index=[['i', 'i', 'j', 'k'], ['X', 'X', 'Y', 'Y']])
```

### Step 3: Assign result = value

```python
result = df.iloc[2, 2]
```

### Step 4: Assign expected = value

```python
expected = arr[2, 2]
```

**Verification:**
```python
assert result == expected
```


## Complete Example

```python
# Workflow
arr = np.random.default_rng(2).standard_normal((4, 3))
df = DataFrame(arr, columns=[['i', 'i', 'j'], ['A', 'A', 'B']], index=[['i', 'i', 'j', 'k'], ['X', 'X', 'Y', 'Y']])
result = df.iloc[2, 2]
expected = arr[2, 2]
assert result == expected
```

## Next Steps


---

*Source: test_iloc.py:76 | Complexity: Intermediate | Last updated: 2026-06-02*