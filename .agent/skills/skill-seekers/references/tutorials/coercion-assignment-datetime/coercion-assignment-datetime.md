# How To: Coercion Assignment Datetime

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test coercion assignment datetime

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
# Fixtures: val, unit, dtype
```

## Step-by-Step Guide

### Step 1: Assign scalar = np.datetime64(...)

```python
scalar = np.datetime64(val, unit)
```

**Verification:**
```python
assert arr[()] == cut_string
```

### Step 2: Assign dtype = np.dtype(...)

```python
dtype = np.dtype(dtype)
```

**Verification:**
```python
assert ass[()] == cut_string
```

### Step 3: Assign cut_string = dtype.type(...)

```python
cut_string = dtype.type(str(scalar)[:6])
```

### Step 4: Assign arr = np.array(...)

```python
arr = np.array(scalar, dtype=dtype)
```

**Verification:**
```python
assert arr[()] == cut_string
```

### Step 5: Assign ass = np.ones(...)

```python
ass = np.ones((), dtype=dtype)
```

### Step 6: Assign unknown = scalar

```python
ass[()] = scalar
```

**Verification:**
```python
assert ass[()] == cut_string
```

### Step 7: Call np.array.astype()

```python
np.array(scalar).astype(dtype)
```


## Complete Example

```python
# Setup
# Fixtures: val, unit, dtype

# Workflow
scalar = np.datetime64(val, unit)
dtype = np.dtype(dtype)
cut_string = dtype.type(str(scalar)[:6])
arr = np.array(scalar, dtype=dtype)
assert arr[()] == cut_string
ass = np.ones((), dtype=dtype)
ass[()] = scalar
assert ass[()] == cut_string
with pytest.raises(RuntimeError):
    np.array(scalar).astype(dtype)
```

## Next Steps


---

*Source: test_array_coercion.py:442 | Complexity: Intermediate | Last updated: 2026-06-02*