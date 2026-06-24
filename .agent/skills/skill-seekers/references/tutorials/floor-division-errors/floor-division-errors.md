# How To: Floor Division Errors

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test floor division errors

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `fnmatch`
- `inspect`
- `itertools`
- `operator`
- `platform`
- `sys`
- `warnings`
- `collections`
- `fractions`
- `functools`
- `pytest`
- `numpy`
- `numpy._core.umath`
- `numpy._core`
- `numpy.testing`
- `numpy.testing._private.utils`
- `operator`
- `platform`
- `decimal`
- `cmath`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign fnan = np.array(...)

```python
fnan = np.array(np.nan, dtype=dtype)
```

**Verification:**
```python
assert_raises(FloatingPointError, np.floor_divide, fone, fzer)
```

### Step 2: Assign fone = np.array(...)

```python
fone = np.array(1.0, dtype=dtype)
```

### Step 3: Assign fzer = np.array(...)

```python
fzer = np.array(0.0, dtype=dtype)
```

### Step 4: Assign finf = np.array(...)

```python
finf = np.array(np.inf, dtype=dtype)
```

### Step 5: Call assert_raises()

```python
assert_raises(FloatingPointError, np.floor_divide, fone, fzer)
```

### Step 6: Call np.floor_divide()

```python
np.floor_divide(fone, fzer)
```

### Step 7: Call np.floor_divide()

```python
np.floor_divide(fnan, fone)
```

### Step 8: Call np.floor_divide()

```python
np.floor_divide(fone, fnan)
```

### Step 9: Call np.floor_divide()

```python
np.floor_divide(fnan, fzer)
```

### Step 10: Call np.floor_divide()

```python
np.floor_divide(fzer, fnan)
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
fnan = np.array(np.nan, dtype=dtype)
fone = np.array(1.0, dtype=dtype)
fzer = np.array(0.0, dtype=dtype)
finf = np.array(np.inf, dtype=dtype)
with np.errstate(divide='raise', invalid='ignore'):
    assert_raises(FloatingPointError, np.floor_divide, fone, fzer)
with np.errstate(divide='ignore', invalid='raise'):
    np.floor_divide(fone, fzer)
with np.errstate(all='raise'):
    np.floor_divide(fnan, fone)
    np.floor_divide(fone, fnan)
    np.floor_divide(fnan, fzer)
    np.floor_divide(fzer, fnan)
```

## Next Steps


---

*Source: test_umath.py:679 | Complexity: Advanced | Last updated: 2026-06-02*