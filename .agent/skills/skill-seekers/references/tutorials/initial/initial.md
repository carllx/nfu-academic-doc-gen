# How To: Initial

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test initial

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign ar = np.arange.astype(...)

```python
ar = np.arange(9).astype(dtype)
```

**Verification:**
```python
assert ret.dtype == dtype
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
reference = 28 if f is np.nansum else 3360
```

### Step 4: Assign ret = f(...)

```python
ret = f(ar, initial=2)
```

**Verification:**
```python
assert ret.dtype == dtype
```


## Complete Example

```python
# Workflow
ar = np.arange(9).astype(dtype)
ar[:5] = np.nan
for f in self.nanfuncs:
    reference = 28 if f is np.nansum else 3360
    ret = f(ar, initial=2)
    assert ret.dtype == dtype
    assert ret == reference
```

## Next Steps


---

*Source: test_nanfunctions.py:604 | Complexity: Intermediate | Last updated: 2026-06-02*