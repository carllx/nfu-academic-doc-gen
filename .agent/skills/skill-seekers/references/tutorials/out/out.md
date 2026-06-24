# How To: Out

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test out

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
assert ret is out
```

### Step 2: Assign unknown = value

```python
ar[:5] = np.nan
```

**Verification:**
```python
assert ret == reference
```

### Step 3: Assign out = np.zeros(...)

```python
out = np.zeros((), dtype=np.intp)
```

### Step 4: Assign reference = value

```python
reference = 5 if f is np.nanargmin else 8
```

### Step 5: Assign ret = f(...)

```python
ret = f(ar, out=out)
```

**Verification:**
```python
assert ret is out
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
ar = np.arange(9).astype(dtype)
ar[:5] = np.nan
for f in self.nanfuncs:
    out = np.zeros((), dtype=np.intp)
    reference = 5 if f is np.nanargmin else 8
    ret = f(ar, out=out)
    assert ret is out
    assert ret == reference
```

## Next Steps


---

*Source: test_nanfunctions.py:354 | Complexity: Intermediate | Last updated: 2026-06-02*