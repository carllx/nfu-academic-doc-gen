# How To: Ddof

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ddof

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

### Step 1: Assign nanfuncs = value

```python
nanfuncs = [np.nanvar, np.nanstd]
```

**Verification:**
```python
assert_almost_equal(res, tgt)
```

### Step 2: Assign stdfuncs = value

```python
stdfuncs = [np.var, np.std]
```

### Step 3: Assign tgt = value

```python
tgt = [rf(d, ddof=ddof) for d in _rdat]
```

### Step 4: Assign res = nf(...)

```python
res = nf(_ndat, axis=1, ddof=ddof)
```

### Step 5: Call assert_almost_equal()

```python
assert_almost_equal(res, tgt)
```


## Complete Example

```python
# Workflow
nanfuncs = [np.nanvar, np.nanstd]
stdfuncs = [np.var, np.std]
for nf, rf in zip(nanfuncs, stdfuncs):
    for ddof in [0, 1]:
        tgt = [rf(d, ddof=ddof) for d in _rdat]
        res = nf(_ndat, axis=1, ddof=ddof)
        assert_almost_equal(res, tgt)
```

## Next Steps


---

*Source: test_nanfunctions.py:717 | Complexity: Intermediate | Last updated: 2026-06-02*