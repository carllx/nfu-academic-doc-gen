# How To: Nep35 Functions As Array Functions

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: unittest, workflow, integration

## Overview

Workflow: test nep35 functions as array functions

## Prerequisites

**Required Modules:**
- `inspect`
- `os`
- `pickle`
- `sys`
- `tempfile`
- `io`
- `unittest`
- `pytest`
- `numpy`
- `numpy._core.overrides`
- `numpy.testing`
- `numpy.testing.overrides`


## Step-by-Step Guide

### Step 1: Assign all_array_functions = get_overridable_numpy_array_functions(...)

```python
all_array_functions = get_overridable_numpy_array_functions()
```

**Verification:**
```python
assert like_array_functions_subset.issubset(all_array_functions)
```

### Step 2: Assign like_array_functions_subset = value

```python
like_array_functions_subset = {getattr(np, func_name) for func_name, *_ in self.__class__._array_tests}
```

**Verification:**
```python
assert nep35_python_functions.issubset(all_array_functions)
```

### Step 3: Assign nep35_python_functions = value

```python
nep35_python_functions = {np.eye, np.fromfunction, np.full, np.genfromtxt, np.identity, np.loadtxt, np.ones, np.require, np.tri}
```

**Verification:**
```python
assert nep35_C_functions.issubset(all_array_functions)
```

### Step 4: Assign nep35_C_functions = value

```python
nep35_C_functions = {np.arange, np.array, np.asanyarray, np.asarray, np.ascontiguousarray, np.asfortranarray, np.empty, np.frombuffer, np.fromfile, np.fromiter, np.fromstring, np.zeros}
```

**Verification:**
```python
assert nep35_C_functions.issubset(all_array_functions)
```


## Complete Example

```python
# Workflow
all_array_functions = get_overridable_numpy_array_functions()
like_array_functions_subset = {getattr(np, func_name) for func_name, *_ in self.__class__._array_tests}
assert like_array_functions_subset.issubset(all_array_functions)
nep35_python_functions = {np.eye, np.fromfunction, np.full, np.genfromtxt, np.identity, np.loadtxt, np.ones, np.require, np.tri}
assert nep35_python_functions.issubset(all_array_functions)
nep35_C_functions = {np.arange, np.array, np.asanyarray, np.asarray, np.ascontiguousarray, np.asfortranarray, np.empty, np.frombuffer, np.fromfile, np.fromiter, np.fromstring, np.zeros}
assert nep35_C_functions.issubset(all_array_functions)
```

## Next Steps


---

*Source: test_overrides.py:628 | Complexity: Intermediate | Last updated: 2026-06-02*