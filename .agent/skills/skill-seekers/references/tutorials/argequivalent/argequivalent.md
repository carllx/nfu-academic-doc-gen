# How To: Argequivalent

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test it translates from arg<func> to <func> 

## Prerequisites

**Required Modules:**
- `functools`
- `sys`
- `pytest`
- `numpy`
- `numpy`
- `numpy.exceptions`
- `numpy.testing`
- `numpy.random`
- `numpy.random`
- `numpy.random`


## Step-by-Step Guide

### Step 1: ' Test it translates from arg<func> to <func> '

```python
' Test it translates from arg<func> to <func> '
```

**Verification:**
```python
assert_equal(a_func, take_along_axis(a, ai_func, axis=axis))
```

### Step 2: Assign a = rand(...)

```python
a = rand(3, 4, 5)
```

### Step 3: Assign funcs = value

```python
funcs = [(np.sort, np.argsort, {}), (_add_keepdims(np.min), _add_keepdims(np.argmin), {}), (_add_keepdims(np.max), _add_keepdims(np.argmax), {})]
```

### Step 4: Assign a_func = func(...)

```python
a_func = func(a, axis=axis, **kwargs)
```

### Step 5: Assign ai_func = argfunc(...)

```python
ai_func = argfunc(a, axis=axis, **kwargs)
```

### Step 6: Call assert_equal()

```python
assert_equal(a_func, take_along_axis(a, ai_func, axis=axis))
```


## Complete Example

```python
# Workflow
' Test it translates from arg<func> to <func> '
from numpy.random import rand
a = rand(3, 4, 5)
funcs = [(np.sort, np.argsort, {}), (_add_keepdims(np.min), _add_keepdims(np.argmin), {}), (_add_keepdims(np.max), _add_keepdims(np.argmax), {})]
for func, argfunc, kwargs in funcs:
    for axis in list(range(a.ndim)) + [None]:
        a_func = func(a, axis=axis, **kwargs)
        ai_func = argfunc(a, axis=axis, **kwargs)
        assert_equal(a_func, take_along_axis(a, ai_func, axis=axis))
```

## Next Steps


---

*Source: test_shape_base.py:41 | Complexity: Intermediate | Last updated: 2026-06-02*