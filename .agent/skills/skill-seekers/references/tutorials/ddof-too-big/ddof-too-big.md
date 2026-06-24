# How To: Ddof Too Big

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ddof too big

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
assert_equal(np.isnan(res), tgt)
```

### Step 2: Assign stdfuncs = value

```python
stdfuncs = [np.var, np.std]
```

**Verification:**
```python
assert_(len(w) == 1)
```

### Step 3: Assign dsize = value

```python
dsize = [len(d) for d in _rdat]
```

**Verification:**
```python
assert_(len(w) == 0)
```

### Step 4: Call warnings.simplefilter()

```python
warnings.simplefilter('always')
```

### Step 5: Call warnings.simplefilter()

```python
warnings.simplefilter('ignore', ComplexWarning)
```

### Step 6: Assign tgt = value

```python
tgt = [ddof >= d for d in dsize]
```

### Step 7: Assign res = nf(...)

```python
res = nf(_ndat, axis=1, ddof=ddof)
```

### Step 8: Call assert_equal()

```python
assert_equal(np.isnan(res), tgt)
```

### Step 9: Call assert_()

```python
assert_(len(w) == 1)
```

### Step 10: Call assert_()

```python
assert_(len(w) == 0)
```


## Complete Example

```python
# Workflow
nanfuncs = [np.nanvar, np.nanstd]
stdfuncs = [np.var, np.std]
dsize = [len(d) for d in _rdat]
for nf, rf in zip(nanfuncs, stdfuncs):
    for ddof in range(5):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')
            warnings.simplefilter('ignore', ComplexWarning)
            tgt = [ddof >= d for d in dsize]
            res = nf(_ndat, axis=1, ddof=ddof)
            assert_equal(np.isnan(res), tgt)
        if any(tgt):
            assert_(len(w) == 1)
        else:
            assert_(len(w) == 0)
```

## Next Steps


---

*Source: test_nanfunctions.py:726 | Complexity: Advanced | Last updated: 2026-06-02*