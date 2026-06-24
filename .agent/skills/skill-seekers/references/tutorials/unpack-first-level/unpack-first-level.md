# How To: Unpack First Level

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test unpack first level

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `pytest`
- `pytest`
- `numpy`
- `numpy._core._multiarray_umath`
- `numpy._core._rational_tests`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: arraylike
```

## Step-by-Step Guide

### Step 1: Assign obj = np.array(...)

```python
obj = np.array([None])
```

**Verification:**
```python
assert arr.shape == (1, 1)
```

### Step 2: Assign unknown = np.array(...)

```python
obj[0] = np.array(1.2)
```

**Verification:**
```python
assert arr.dtype == expected
```

### Step 3: Assign length = len(...)

```python
length = len(str(obj[0]))
```

### Step 4: Assign expected = np.dtype(...)

```python
expected = np.dtype(f'S{length}')
```

### Step 5: Assign obj = arraylike(...)

```python
obj = arraylike(obj)
```

### Step 6: Assign arr = np.array(...)

```python
arr = np.array([obj], dtype='S')
```

**Verification:**
```python
assert arr.shape == (1, 1)
```


## Complete Example

```python
# Setup
# Fixtures: arraylike

# Workflow
obj = np.array([None])
obj[0] = np.array(1.2)
length = len(str(obj[0]))
expected = np.dtype(f'S{length}')
obj = arraylike(obj)
arr = np.array([obj], dtype='S')
assert arr.shape == (1, 1)
assert arr.dtype == expected
```

## Next Steps


---

*Source: test_array_coercion.py:181 | Complexity: Intermediate | Last updated: 2026-06-02*