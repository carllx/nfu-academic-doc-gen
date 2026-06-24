# How To: Nep50 Weak Integers

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test nep50 weak integers

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `hypothesis`
- `pytest`
- `hypothesis`
- `numpy`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign scalar_type = value

```python
scalar_type = np.dtype(dtype).type
```

**Verification:**
```python
assert res.dtype == dtype
```

### Step 2: Assign maxint = int(...)

```python
maxint = int(np.iinfo(dtype).max)
```

**Verification:**
```python
assert res.dtype == dtype
```

### Step 3: Assign res = value

```python
res = np.array(100, dtype=dtype) + maxint
```

**Verification:**
```python
assert res.dtype == dtype
```

### Step 4: Assign res = value

```python
res = scalar_type(100) + maxint
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
scalar_type = np.dtype(dtype).type
maxint = int(np.iinfo(dtype).max)
with np.errstate(over='warn'):
    with pytest.warns(RuntimeWarning):
        res = scalar_type(100) + maxint
assert res.dtype == dtype
res = np.array(100, dtype=dtype) + maxint
assert res.dtype == dtype
```

## Next Steps


---

*Source: test_nep50_promotions.py:49 | Complexity: Intermediate | Last updated: 2026-06-02*