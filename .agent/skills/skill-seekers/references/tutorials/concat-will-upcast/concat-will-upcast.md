# How To: Concat Will Upcast

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test concat will upcast

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `collections`
- `collections.abc`
- `datetime`
- `decimal`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.tests.extension.decimal`

**Setup Required:**
```python
# Fixtures: pdt, any_signed_int_numpy_dtype
```

## Step-by-Step Guide

### Step 1: Assign dt = any_signed_int_numpy_dtype

```python
dt = any_signed_int_numpy_dtype
```

**Verification:**
```python
assert x.values.dtype == 'float64'
```

### Step 2: Assign dims = value

```python
dims = pdt().ndim
```

### Step 3: Assign dfs = value

```python
dfs = [pdt(np.array([1], dtype=dt, ndmin=dims)), pdt(np.array([np.nan], ndmin=dims)), pdt(np.array([5], dtype=dt, ndmin=dims))]
```

### Step 4: Assign x = concat(...)

```python
x = concat(dfs)
```

**Verification:**
```python
assert x.values.dtype == 'float64'
```


## Complete Example

```python
# Setup
# Fixtures: pdt, any_signed_int_numpy_dtype

# Workflow
dt = any_signed_int_numpy_dtype
dims = pdt().ndim
dfs = [pdt(np.array([1], dtype=dt, ndmin=dims)), pdt(np.array([np.nan], ndmin=dims)), pdt(np.array([5], dtype=dt, ndmin=dims))]
x = concat(dfs)
assert x.values.dtype == 'float64'
```

## Next Steps


---

*Source: test_concat.py:559 | Complexity: Intermediate | Last updated: 2026-06-02*