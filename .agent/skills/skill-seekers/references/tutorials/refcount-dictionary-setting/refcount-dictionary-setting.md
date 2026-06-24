# How To: Refcount Dictionary Setting

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test refcount dictionary setting

## Prerequisites

**Required Modules:**
- `contextlib`
- `ctypes`
- `gc`
- `inspect`
- `operator`
- `pickle`
- `sys`
- `types`
- `itertools`
- `typing`
- `hypothesis`
- `pytest`
- `hypothesis.extra`
- `numpy`
- `numpy.dtypes`
- `numpy._core._multiarray_tests`
- `numpy._core._rational_tests`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign names = value

```python
names = ['name1']
```

**Verification:**
```python
assert refcounts == refcounts_new
```

### Step 2: Assign formats = value

```python
formats = ['f8']
```

### Step 3: Assign titles = value

```python
titles = ['t1']
```

### Step 4: Assign offsets = value

```python
offsets = [0]
```

### Step 5: Assign d = value

```python
d = {'names': names, 'formats': formats, 'titles': titles, 'offsets': offsets}
```

### Step 6: Assign refcounts = value

```python
refcounts = {k: sys.getrefcount(i) for k, i in d.items()}
```

### Step 7: Call np.dtype()

```python
np.dtype(d)
```

### Step 8: Assign refcounts_new = value

```python
refcounts_new = {k: sys.getrefcount(i) for k, i in d.items()}
```

**Verification:**
```python
assert refcounts == refcounts_new
```


## Complete Example

```python
# Workflow
names = ['name1']
formats = ['f8']
titles = ['t1']
offsets = [0]
d = {'names': names, 'formats': formats, 'titles': titles, 'offsets': offsets}
refcounts = {k: sys.getrefcount(i) for k, i in d.items()}
np.dtype(d)
refcounts_new = {k: sys.getrefcount(i) for k, i in d.items()}
assert refcounts == refcounts_new
```

## Next Steps


---

*Source: test_dtype.py:288 | Complexity: Advanced | Last updated: 2026-06-02*