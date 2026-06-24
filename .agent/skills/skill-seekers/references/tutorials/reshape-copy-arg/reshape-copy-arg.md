# How To: Reshape Copy Arg

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reshape copy arg

## Prerequisites

**Required Modules:**
- `inspect`
- `itertools`
- `math`
- `platform`
- `sys`
- `warnings`
- `decimal`
- `pytest`
- `hypothesis`
- `hypothesis.extra`
- `numpy`
- `numpy`
- `numpy._core`
- `numpy._core._rational_tests`
- `numpy._core.numerictypes`
- `numpy.exceptions`
- `numpy.random`
- `numpy.testing`
- `fractions`
- `numbers`
- `itertools`


## Step-by-Step Guide

### Step 1: Assign arr = np.arange.reshape(...)

```python
arr = np.arange(24).reshape(2, 3, 4)
```

**Verification:**
```python
assert np.shares_memory(np.reshape(arr, shape), arr)
```

### Step 2: Assign arr_f_ord = np.array(...)

```python
arr_f_ord = np.array(arr, order='F')
```

**Verification:**
```python
assert np.shares_memory(np.reshape(arr, shape, order='C'), arr)
```

### Step 3: Assign shape = value

```python
shape = (12, 2)
```

**Verification:**
```python
assert np.shares_memory(np.reshape(arr_f_ord, shape, order='F'), arr_f_ord)
```

### Step 4: Assign err_msg = 'Unable to avoid creating a copy while reshaping.'

```python
err_msg = 'Unable to avoid creating a copy while reshaping.'
```

**Verification:**
```python
assert np.shares_memory(np.reshape(arr, shape, copy=None), arr)
```

### Step 5: Call np.reshape()

```python
np.reshape(arr, shape, order='F', copy=False)
```

**Verification:**
```python
assert np.shares_memory(np.reshape(arr, shape, copy=False), arr)
```

### Step 6: Call np.reshape()

```python
np.reshape(arr_f_ord, shape, order='C', copy=False)
```

**Verification:**
```python
assert np.shares_memory(arr.reshape(shape, copy=False), arr)
```


## Complete Example

```python
# Workflow
arr = np.arange(24).reshape(2, 3, 4)
arr_f_ord = np.array(arr, order='F')
shape = (12, 2)
assert np.shares_memory(np.reshape(arr, shape), arr)
assert np.shares_memory(np.reshape(arr, shape, order='C'), arr)
assert np.shares_memory(np.reshape(arr_f_ord, shape, order='F'), arr_f_ord)
assert np.shares_memory(np.reshape(arr, shape, copy=None), arr)
assert np.shares_memory(np.reshape(arr, shape, copy=False), arr)
assert np.shares_memory(arr.reshape(shape, copy=False), arr)
assert not np.shares_memory(np.reshape(arr, shape, copy=True), arr)
assert not np.shares_memory(np.reshape(arr, shape, order='C', copy=True), arr)
assert not np.shares_memory(np.reshape(arr, shape, order='F', copy=True), arr)
assert not np.shares_memory(np.reshape(arr, shape, order='F', copy=None), arr)
err_msg = 'Unable to avoid creating a copy while reshaping.'
with pytest.raises(ValueError, match=err_msg):
    np.reshape(arr, shape, order='F', copy=False)
with pytest.raises(ValueError, match=err_msg):
    np.reshape(arr_f_ord, shape, order='C', copy=False)
```

## Next Steps


---

*Source: test_numeric.py:201 | Complexity: Intermediate | Last updated: 2026-06-02*