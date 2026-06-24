# How To: Astype Copyflag

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype copyflag

## Prerequisites

**Required Modules:**
- `sys`
- `pytest`
- `numpy`
- `numpy._core.umath`
- `numpy._core._rational_tests`
- `numpy.lib`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign arr = np.arange(...)

```python
arr = np.arange(10, dtype=np.intp)
```

**Verification:**
```python
assert not np.shares_memory(arr, res_true)
```

### Step 2: Assign res_true = arr.astype(...)

```python
res_true = arr.astype(np.intp, copy=True)
```

**Verification:**
```python
assert np.shares_memory(arr, res_false)
```

### Step 3: Assign res_false = arr.astype(...)

```python
res_false = arr.astype(np.intp, copy=False)
```

**Verification:**
```python
assert not np.shares_memory(arr, res_false_float)
```

### Step 4: Assign res_false_float = arr.astype(...)

```python
res_false_float = arr.astype(np.float64, copy=False)
```

**Verification:**
```python
assert_raises(ValueError, arr.astype, np.float64, copy=np._CopyMode.NEVER)
```

### Step 5: Call assert_raises()

```python
assert_raises(ValueError, arr.astype, np.float64, copy=np._CopyMode.NEVER)
```


## Complete Example

```python
# Workflow
arr = np.arange(10, dtype=np.intp)
res_true = arr.astype(np.intp, copy=True)
assert not np.shares_memory(arr, res_true)
res_false = arr.astype(np.intp, copy=False)
assert np.shares_memory(arr, res_false)
res_false_float = arr.astype(np.float64, copy=False)
assert not np.shares_memory(arr, res_false_float)
assert_raises(ValueError, arr.astype, np.float64, copy=np._CopyMode.NEVER)
```

## Next Steps


---

*Source: test_api.py:640 | Complexity: Intermediate | Last updated: 2026-06-02*