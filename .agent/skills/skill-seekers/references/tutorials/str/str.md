# How To: Str

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test str

## Prerequisites

**Required Modules:**
- `gc`
- `sys`
- `textwrap`
- `pytest`
- `hypothesis`
- `hypothesis.extra`
- `numpy`
- `numpy._core.arrayprint`
- `numpy.testing`
- `numpy.testing._private.utils`


## Step-by-Step Guide

### Step 1: Assign rvals = value

```python
rvals = [0, 1, -1, np.inf, -np.inf, np.nan]
```

**Verification:**
```python
assert_equal(res, val)
```

### Step 2: Assign cvals = value

```python
cvals = [complex(rp, ip) for rp in rvals for ip in rvals]
```

### Step 3: Assign dtypes = value

```python
dtypes = [np.complex64, np.cdouble, np.clongdouble]
```

### Step 4: Assign actual = value

```python
actual = [str(np.array([c], dt)) for c in cvals for dt in dtypes]
```

### Step 5: Assign wanted = value

```python
wanted = ['[0.+0.j]', '[0.+0.j]', '[0.+0.j]', '[0.+1.j]', '[0.+1.j]', '[0.+1.j]', '[0.-1.j]', '[0.-1.j]', '[0.-1.j]', '[0.+infj]', '[0.+infj]', '[0.+infj]', '[0.-infj]', '[0.-infj]', '[0.-infj]', '[0.+nanj]', '[0.+nanj]', '[0.+nanj]', '[1.+0.j]', '[1.+0.j]', '[1.+0.j]', '[1.+1.j]', '[1.+1.j]', '[1.+1.j]', '[1.-1.j]', '[1.-1.j]', '[1.-1.j]', '[1.+infj]', '[1.+infj]', '[1.+infj]', '[1.-infj]', '[1.-infj]', '[1.-infj]', '[1.+nanj]', '[1.+nanj]', '[1.+nanj]', '[-1.+0.j]', '[-1.+0.j]', '[-1.+0.j]', '[-1.+1.j]', '[-1.+1.j]', '[-1.+1.j]', '[-1.-1.j]', '[-1.-1.j]', '[-1.-1.j]', '[-1.+infj]', '[-1.+infj]', '[-1.+infj]', '[-1.-infj]', '[-1.-infj]', '[-1.-infj]', '[-1.+nanj]', '[-1.+nanj]', '[-1.+nanj]', '[inf+0.j]', '[inf+0.j]', '[inf+0.j]', '[inf+1.j]', '[inf+1.j]', '[inf+1.j]', '[inf-1.j]', '[inf-1.j]', '[inf-1.j]', '[inf+infj]', '[inf+infj]', '[inf+infj]', '[inf-infj]', '[inf-infj]', '[inf-infj]', '[inf+nanj]', '[inf+nanj]', '[inf+nanj]', '[-inf+0.j]', '[-inf+0.j]', '[-inf+0.j]', '[-inf+1.j]', '[-inf+1.j]', '[-inf+1.j]', '[-inf-1.j]', '[-inf-1.j]', '[-inf-1.j]', '[-inf+infj]', '[-inf+infj]', '[-inf+infj]', '[-inf-infj]', '[-inf-infj]', '[-inf-infj]', '[-inf+nanj]', '[-inf+nanj]', '[-inf+nanj]', '[nan+0.j]', '[nan+0.j]', '[nan+0.j]', '[nan+1.j]', '[nan+1.j]', '[nan+1.j]', '[nan-1.j]', '[nan-1.j]', '[nan-1.j]', '[nan+infj]', '[nan+infj]', '[nan+infj]', '[nan-infj]', '[nan-infj]', '[nan-infj]', '[nan+nanj]', '[nan+nanj]', '[nan+nanj]']
```

### Step 6: Call assert_equal()

```python
assert_equal(res, val)
```


## Complete Example

```python
# Workflow
rvals = [0, 1, -1, np.inf, -np.inf, np.nan]
cvals = [complex(rp, ip) for rp in rvals for ip in rvals]
dtypes = [np.complex64, np.cdouble, np.clongdouble]
actual = [str(np.array([c], dt)) for c in cvals for dt in dtypes]
wanted = ['[0.+0.j]', '[0.+0.j]', '[0.+0.j]', '[0.+1.j]', '[0.+1.j]', '[0.+1.j]', '[0.-1.j]', '[0.-1.j]', '[0.-1.j]', '[0.+infj]', '[0.+infj]', '[0.+infj]', '[0.-infj]', '[0.-infj]', '[0.-infj]', '[0.+nanj]', '[0.+nanj]', '[0.+nanj]', '[1.+0.j]', '[1.+0.j]', '[1.+0.j]', '[1.+1.j]', '[1.+1.j]', '[1.+1.j]', '[1.-1.j]', '[1.-1.j]', '[1.-1.j]', '[1.+infj]', '[1.+infj]', '[1.+infj]', '[1.-infj]', '[1.-infj]', '[1.-infj]', '[1.+nanj]', '[1.+nanj]', '[1.+nanj]', '[-1.+0.j]', '[-1.+0.j]', '[-1.+0.j]', '[-1.+1.j]', '[-1.+1.j]', '[-1.+1.j]', '[-1.-1.j]', '[-1.-1.j]', '[-1.-1.j]', '[-1.+infj]', '[-1.+infj]', '[-1.+infj]', '[-1.-infj]', '[-1.-infj]', '[-1.-infj]', '[-1.+nanj]', '[-1.+nanj]', '[-1.+nanj]', '[inf+0.j]', '[inf+0.j]', '[inf+0.j]', '[inf+1.j]', '[inf+1.j]', '[inf+1.j]', '[inf-1.j]', '[inf-1.j]', '[inf-1.j]', '[inf+infj]', '[inf+infj]', '[inf+infj]', '[inf-infj]', '[inf-infj]', '[inf-infj]', '[inf+nanj]', '[inf+nanj]', '[inf+nanj]', '[-inf+0.j]', '[-inf+0.j]', '[-inf+0.j]', '[-inf+1.j]', '[-inf+1.j]', '[-inf+1.j]', '[-inf-1.j]', '[-inf-1.j]', '[-inf-1.j]', '[-inf+infj]', '[-inf+infj]', '[-inf+infj]', '[-inf-infj]', '[-inf-infj]', '[-inf-infj]', '[-inf+nanj]', '[-inf+nanj]', '[-inf+nanj]', '[nan+0.j]', '[nan+0.j]', '[nan+0.j]', '[nan+1.j]', '[nan+1.j]', '[nan+1.j]', '[nan-1.j]', '[nan-1.j]', '[nan-1.j]', '[nan+infj]', '[nan+infj]', '[nan+infj]', '[nan-infj]', '[nan-infj]', '[nan-infj]', '[nan+nanj]', '[nan+nanj]', '[nan+nanj]']
for res, val in zip(actual, wanted):
    assert_equal(res, val)
```

## Next Steps


---

*Source: test_arrayprint.py:172 | Complexity: Intermediate | Last updated: 2026-06-02*