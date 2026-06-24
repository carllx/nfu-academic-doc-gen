# How To: Concat No Unnecessary Upcast

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat no unnecessary upcast

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
# Fixtures: float_numpy_dtype, frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign dims = value

```python
dims = frame_or_series(dtype=object).ndim
```

**Verification:**
```python
assert x.values.dtype == dt
```

### Step 2: Assign dt = float_numpy_dtype

```python
dt = float_numpy_dtype
```

### Step 3: Assign dfs = value

```python
dfs = [frame_or_series(np.array([1], dtype=dt, ndmin=dims)), frame_or_series(np.array([np.nan], dtype=dt, ndmin=dims)), frame_or_series(np.array([5], dtype=dt, ndmin=dims))]
```

### Step 4: Assign x = concat(...)

```python
x = concat(dfs)
```

**Verification:**
```python
assert x.values.dtype == dt
```


## Complete Example

```python
# Setup
# Fixtures: float_numpy_dtype, frame_or_series

# Workflow
dims = frame_or_series(dtype=object).ndim
dt = float_numpy_dtype
dfs = [frame_or_series(np.array([1], dtype=dt, ndmin=dims)), frame_or_series(np.array([np.nan], dtype=dt, ndmin=dims)), frame_or_series(np.array([5], dtype=dt, ndmin=dims))]
x = concat(dfs)
assert x.values.dtype == dt
```

## Next Steps


---

*Source: test_concat.py:544 | Complexity: Intermediate | Last updated: 2026-06-02*