# How To: Engine Type

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test engine type

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs`
- `pandas._libs.arrays`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.api`

**Setup Required:**
```python
# Fixtures: dtype, engine_type
```

## Step-by-Step Guide

### Step 1: Assign num_uniques = value

```python
num_uniques = {np.int8: 1, np.int16: 128, np.int32: 32768}[dtype]
```

**Verification:**
```python
assert np.issubdtype(ci.codes.dtype, dtype)
```

### Step 2: Assign ci = CategoricalIndex(...)

```python
ci = CategoricalIndex(range(num_uniques))
```

**Verification:**
```python
assert isinstance(ci._engine, engine_type)
```

### Step 3: Assign ci = CategoricalIndex(...)

```python
ci = CategoricalIndex(range(32768))
```

### Step 4: Assign arr = ci.values._ndarray.astype(...)

```python
arr = ci.values._ndarray.astype('int64')
```

### Step 5: Call NDArrayBacked.__init__()

```python
NDArrayBacked.__init__(ci._data, arr, ci.dtype)
```


## Complete Example

```python
# Setup
# Fixtures: dtype, engine_type

# Workflow
if dtype != np.int64:
    num_uniques = {np.int8: 1, np.int16: 128, np.int32: 32768}[dtype]
    ci = CategoricalIndex(range(num_uniques))
else:
    ci = CategoricalIndex(range(32768))
    arr = ci.values._ndarray.astype('int64')
    NDArrayBacked.__init__(ci._data, arr, ci.dtype)
assert np.issubdtype(ci.codes.dtype, dtype)
assert isinstance(ci._engine, engine_type)
```

## Next Steps


---

*Source: test_category.py:289 | Complexity: Intermediate | Last updated: 2026-06-02*