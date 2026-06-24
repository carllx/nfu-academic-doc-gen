# How To: Keepdims

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test keepdims

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `inspect`
- `warnings`
- `functools`
- `pytest`
- `numpy`
- `numpy._core.numeric`
- `numpy.exceptions`
- `numpy.lib._nanfunctions_impl`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign ar = np.arange.astype(...)

```python
ar = np.arange(9).astype(dtype)
```

**Verification:**
```python
assert ret.ndim == ar.ndim
```

### Step 2: Assign unknown = value

```python
ar[:5] = np.nan
```

**Verification:**
```python
assert ret == reference
```

### Step 3: Assign reference = value

```python
reference = 5 if f is np.nanargmin else 8
```

### Step 4: Assign ret = f(...)

```python
ret = f(ar, keepdims=True)
```

**Verification:**
```python
assert ret.ndim == ar.ndim
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
ar = np.arange(9).astype(dtype)
ar[:5] = np.nan
for f in self.nanfuncs:
    reference = 5 if f is np.nanargmin else 8
    ret = f(ar, keepdims=True)
    assert ret.ndim == ar.ndim
    assert ret == reference
```

## Next Steps


---

*Source: test_nanfunctions.py:343 | Complexity: Intermediate | Last updated: 2026-06-02*