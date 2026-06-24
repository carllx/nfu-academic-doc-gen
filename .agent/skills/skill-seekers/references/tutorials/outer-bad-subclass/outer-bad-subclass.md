# How To: Outer Bad Subclass

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test outer bad subclass

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign arr = np.ones.view(...)

```python
arr = np.ones((2, 3)).view(cls)
```

**Verification:**
```python
assert type(np.add.outer([1, 2], arr)) is cls
```

### Step 2: Assign arr = np.ones.view(...)

```python
arr = np.ones((2, 3)).view(cls)
```

**Verification:**
```python
assert type(np.add.outer([1, 2], arr)) is cls
```

### Step 3: Call np.add.outer()

```python
np.add.outer(arr, [1, 2])
```

### Step 4: Assign self.shape = value

```python
self.shape = self.shape + (1,)
```

### Step 5: Assign self.shape = value

```python
self.shape = self.shape[::-1]
```


## Complete Example

```python
# Workflow
class BadArr1(np.ndarray):

    def __array_finalize__(self, obj):
        if self.ndim == 3:
            self.shape = self.shape + (1,)

class BadArr2(np.ndarray):

    def __array_finalize__(self, obj):
        if isinstance(obj, BadArr2):
            if self.shape[-1] == 1:
                self.shape = self.shape[::-1]
for cls in [BadArr1, BadArr2]:
    arr = np.ones((2, 3)).view(cls)
    with assert_raises(TypeError) as a:
        np.add.outer(arr, [1, 2])
    arr = np.ones((2, 3)).view(cls)
    assert type(np.add.outer([1, 2], arr)) is cls
```

## Next Steps


---

*Source: test_umath.py:4840 | Complexity: Intermediate | Last updated: 2026-06-02*