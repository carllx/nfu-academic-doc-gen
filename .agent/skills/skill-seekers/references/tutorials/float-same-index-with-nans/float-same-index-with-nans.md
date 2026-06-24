# How To: Float Same Index With Nans

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test float same index with nans

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`

**Setup Required:**
```python
# Fixtures: kind, mix, all_arithmetic_functions, request
```

## Step-by-Step Guide

### Step 1: Assign op = all_arithmetic_functions

```python
op = all_arithmetic_functions
```

### Step 2: Assign values = np.array(...)

```python
values = np.array([np.nan, 1, 2, 0, np.nan, 0, 1, 2, 1, np.nan])
```

### Step 3: Assign rvalues = np.array(...)

```python
rvalues = np.array([np.nan, 2, 3, 4, np.nan, 0, 1, 3, 2, np.nan])
```

### Step 4: Assign a = SparseArray(...)

```python
a = SparseArray(values, kind=kind)
```

### Step 5: Assign b = SparseArray(...)

```python
b = SparseArray(rvalues, kind=kind)
```

### Step 6: Call self._check_numeric_ops()

```python
self._check_numeric_ops(a, b, values, rvalues, mix, op)
```


## Complete Example

```python
# Setup
# Fixtures: kind, mix, all_arithmetic_functions, request

# Workflow
op = all_arithmetic_functions
values = np.array([np.nan, 1, 2, 0, np.nan, 0, 1, 2, 1, np.nan])
rvalues = np.array([np.nan, 2, 3, 4, np.nan, 0, 1, 3, 2, np.nan])
a = SparseArray(values, kind=kind)
b = SparseArray(rvalues, kind=kind)
self._check_numeric_ops(a, b, values, rvalues, mix, op)
```

## Next Steps


---

*Source: test_arithmetics.py:152 | Complexity: Intermediate | Last updated: 2026-06-02*