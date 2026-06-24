# How To: Binary Ufunc Reduceat Fuzz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test binary ufunc reduceat fuzz

## Prerequisites

**Required Modules:**
- `itertools`
- `pytest`
- `numpy`
- `numpy._core`
- `numpy._core._multiarray_tests`
- `numpy.lib.stride_tricks`
- `numpy.testing`
- `numpy.lib._stride_tricks_impl`


## Step-by-Step Guide

### Step 1: Call self.check_unary_fuzz()

```python
self.check_unary_fuzz(do_reduceat, get_out_axis_size, dtype=np.int16, count=500)
```

### Step 2: Assign idx = np.arange(...)

```python
idx = np.arange(0, size, step)
```

### Step 3: Assign size = len(...)

```python
size = len(a)
```

### Step 4: Assign step = value

```python
step = size // len(out)
```

### Step 5: Assign size = value

```python
size = a.shape[axis]
```

### Step 6: Assign step = value

```python
step = a.shape[axis] // out.shape[axis]
```


## Complete Example

```python
# Workflow
def get_out_axis_size(a, b, axis):
    if axis is None:
        if a.ndim == 1:
            return (a.size, False)
        else:
            return ('skip', False)
    else:
        return (a.shape[axis], False)

def do_reduceat(a, out, axis):
    if axis is None:
        size = len(a)
        step = size // len(out)
    else:
        size = a.shape[axis]
        step = a.shape[axis] // out.shape[axis]
    idx = np.arange(0, size, step)
    return np.add.reduceat(a, idx, out=out, axis=axis)
self.check_unary_fuzz(do_reduceat, get_out_axis_size, dtype=np.int16, count=500)
```

## Next Steps


---

*Source: test_mem_overlap.py:696 | Complexity: Intermediate | Last updated: 2026-06-02*