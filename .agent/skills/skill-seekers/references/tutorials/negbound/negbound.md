# How To: Negbound

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test negbound

## Prerequisites

**Required Modules:**
- `os`
- `platform`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign xvec = np.arange(...)

```python
xvec = np.arange(12)
```

**Verification:**
```python
assert np.allclose(rval, expval)
```

### Step 2: Assign xlow = value

```python
xlow = -6
```

### Step 3: Assign xhigh = 4

```python
xhigh = 4
```

### Step 4: Assign rval = self.module.foo(...)

```python
rval = self.module.foo(is_=xlow, ie_=xhigh, arr=xvec[:ubound(xlow, xhigh)])
```

### Step 5: Assign expval = np.arange(...)

```python
expval = np.arange(11, dtype=np.float32)
```

**Verification:**
```python
assert np.allclose(rval, expval)
```


## Complete Example

```python
# Workflow
xvec = np.arange(12)
xlow = -6
xhigh = 4

def ubound(xl, xh):
    return xh - xl + 1
rval = self.module.foo(is_=xlow, ie_=xhigh, arr=xvec[:ubound(xlow, xhigh)])
expval = np.arange(11, dtype=np.float32)
assert np.allclose(rval, expval)
```

## Next Steps


---

*Source: test_regression.py:55 | Complexity: Intermediate | Last updated: 2026-06-02*