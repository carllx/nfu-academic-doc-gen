# How To: Invalid

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test invalid inputs 

## Prerequisites

**Required Modules:**
- `functools`
- `sys`
- `pytest`
- `numpy`
- `numpy`
- `numpy.exceptions`
- `numpy.testing`
- `numpy.random`
- `numpy.random`
- `numpy.random`


## Step-by-Step Guide

### Step 1: ' Test invalid inputs '

```python
' Test invalid inputs '
```

**Verification:**
```python
assert np.all(a == [[2, 2, 2], [1, 1, 1]])
```

### Step 2: Assign a_base = np.array(...)

```python
a_base = np.array([[10, 30, 20], [60, 40, 50]])
```

**Verification:**
```python
assert 'single dimension' in str(exc.exception)
```

### Step 3: Assign indices = np.array(...)

```python
indices = np.array([[0], [1]])
```

### Step 4: Assign values = np.array(...)

```python
values = np.array([[2], [1]])
```

### Step 5: Assign a = a_base.copy(...)

```python
a = a_base.copy()
```

### Step 6: Call put_along_axis()

```python
put_along_axis(a, indices, values, axis=0)
```

**Verification:**
```python
assert np.all(a == [[2, 2, 2], [1, 1, 1]])
```

### Step 7: Assign a = a_base.copy(...)

```python
a = a_base.copy()
```

**Verification:**
```python
assert 'single dimension' in str(exc.exception)
```

### Step 8: Call put_along_axis()

```python
put_along_axis(a, indices, values, axis=None)
```


## Complete Example

```python
# Workflow
' Test invalid inputs '
a_base = np.array([[10, 30, 20], [60, 40, 50]])
indices = np.array([[0], [1]])
values = np.array([[2], [1]])
a = a_base.copy()
put_along_axis(a, indices, values, axis=0)
assert np.all(a == [[2, 2, 2], [1, 1, 1]])
a = a_base.copy()
with assert_raises(ValueError) as exc:
    put_along_axis(a, indices, values, axis=None)
assert 'single dimension' in str(exc.exception)
```

## Next Steps


---

*Source: test_shape_base.py:118 | Complexity: Advanced | Last updated: 2026-06-02*