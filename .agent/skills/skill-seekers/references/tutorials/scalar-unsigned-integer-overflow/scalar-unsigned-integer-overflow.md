# How To: Scalar Unsigned Integer Overflow

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test scalar unsigned integer overflow

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `contextlib`
- `itertools`
- `operator`
- `platform`
- `sys`
- `warnings`
- `pytest`
- `hypothesis`
- `hypothesis.extra`
- `hypothesis.strategies`
- `numpy`
- `numpy._core._rational_tests`
- `numpy._utils`
- `numpy.exceptions`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign val = np.dtype.type(...)

```python
val = np.dtype(dtype).type(8)
```

### Step 2: Assign zero = np.dtype.type(...)

```python
zero = np.dtype(dtype).type(0)
```

### Step 3: -zero

```python
-zero
```

### Step 4: -val

```python
-val
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
val = np.dtype(dtype).type(8)
with pytest.warns(RuntimeWarning, match='overflow encountered'):
    -val
zero = np.dtype(dtype).type(0)
-zero
```

## Next Steps


---

*Source: test_scalarmath.py:990 | Complexity: Intermediate | Last updated: 2026-06-02*