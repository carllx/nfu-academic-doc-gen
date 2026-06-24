# How To: Boolean Array Constructor Copy

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test boolean array constructor copy

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.arrays`
- `pandas.core.arrays.boolean`


## Step-by-Step Guide

### Step 1: Assign values = np.array(...)

```python
values = np.array([True, False, True, False], dtype='bool')
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

### Step 3: Assign result = BooleanArray(...)

```python
result = BooleanArray(values, mask)
```

**Verification:**
```python
assert result._data is not values
```

### Step 4: Assign result = BooleanArray(...)

```python
result = BooleanArray(values, mask, copy=True)
```

**Verification:**
```python
assert result._mask is not mask
```


## Complete Example

```python
# Workflow
values = np.array([True, False, True, False], dtype='bool')
mask = np.array([False, False, False, True], dtype='bool')
result = BooleanArray(values, mask)
assert result._data is values
assert result._mask is mask
result = BooleanArray(values, mask, copy=True)
assert result._data is not values
assert result._mask is not mask
```

## Next Steps


---

*Source: test_construction.py:37 | Complexity: Intermediate | Last updated: 2026-06-02*