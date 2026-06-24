# How To: Integer Array Constructor Copy

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test integer array constructor copy

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.arrays`
- `pandas.core.arrays.integer`


## Step-by-Step Guide

### Step 1: Assign values = np.array(...)

```python
values = np.array([1, 2, 3, 4], dtype='int64')
```

**Verification:**
```python
assert result._data is values
```

### Step 2: Assign mask = np.array(...)

```python
mask = np.array([False, False, False, True], dtype='bool')
```

**Verification:**
```python
assert result._mask is mask
```

### Step 3: Assign result = IntegerArray(...)

```python
result = IntegerArray(values, mask)
```

**Verification:**
```python
assert result._data is not values
```

### Step 4: Assign result = IntegerArray(...)

```python
result = IntegerArray(values, mask, copy=True)
```

**Verification:**
```python
assert result._mask is not mask
```


## Complete Example

```python
# Workflow
values = np.array([1, 2, 3, 4], dtype='int64')
mask = np.array([False, False, False, True], dtype='bool')
result = IntegerArray(values, mask)
assert result._data is values
assert result._mask is mask
result = IntegerArray(values, mask, copy=True)
assert result._data is not values
assert result._mask is not mask
```

## Next Steps


---

*Source: test_construction.py:97 | Complexity: Intermediate | Last updated: 2026-06-02*