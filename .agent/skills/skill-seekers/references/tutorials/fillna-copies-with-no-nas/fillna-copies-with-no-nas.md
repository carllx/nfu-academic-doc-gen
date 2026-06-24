# How To: Fillna Copies With No Nas

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fillna copies with no nas

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ci = CategoricalIndex(...)

```python
ci = CategoricalIndex([0, 1, 1])
```

**Verification:**
```python
assert result is not ci
```

### Step 2: Assign result = ci.fillna(...)

```python
result = ci.fillna(0)
```

**Verification:**
```python
assert tm.shares_memory(result, ci)
```

### Step 3: Assign cat = value

```python
cat = ci._data
```

**Verification:**
```python
assert result._ndarray is not cat._ndarray
```

### Step 4: Assign result = cat.fillna(...)

```python
result = cat.fillna(0)
```

**Verification:**
```python
assert result._ndarray.base is None
```


## Complete Example

```python
# Workflow
ci = CategoricalIndex([0, 1, 1])
result = ci.fillna(0)
assert result is not ci
assert tm.shares_memory(result, ci)
cat = ci._data
result = cat.fillna(0)
assert result._ndarray is not cat._ndarray
assert result._ndarray.base is None
assert not tm.shares_memory(result, cat)
```

## Next Steps


---

*Source: test_fillna.py:27 | Complexity: Intermediate | Last updated: 2026-06-02*