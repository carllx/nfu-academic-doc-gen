# How To: Float Same Index Without Nans

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test float same index without nans

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
# Fixtures: kind, mix, all_arithmetic_functions
```

## Step-by-Step Guide

### Step 1: Assign op = all_arithmetic_functions

```python
op = all_arithmetic_functions
```

### Step 2: Assign values = np.array(...)

```python
values = np.array([0.0, 1.0, 2.0, 6.0, 0.0, 0.0, 1.0, 2.0, 1.0, 0.0])
```

### Step 3: Assign rvalues = np.array(...)

```python
rvalues = np.array([0.0, 2.0, 3.0, 4.0, 0.0, 0.0, 1.0, 3.0, 2.0, 0.0])
```

### Step 4: Assign a = SparseArray(...)

```python
a = SparseArray(values, kind=kind, fill_value=0)
```

### Step 5: Assign b = SparseArray(...)

```python
b = SparseArray(rvalues, kind=kind, fill_value=0)
```

### Step 6: Call self._check_numeric_ops()

```python
self._check_numeric_ops(a, b, values, rvalues, mix, op)
```


## Complete Example

```python
# Setup
# Fixtures: kind, mix, all_arithmetic_functions

# Workflow
op = all_arithmetic_functions
values = np.array([0.0, 1.0, 2.0, 6.0, 0.0, 0.0, 1.0, 2.0, 1.0, 0.0])
rvalues = np.array([0.0, 2.0, 3.0, 4.0, 0.0, 0.0, 1.0, 3.0, 2.0, 0.0])
a = SparseArray(values, kind=kind, fill_value=0)
b = SparseArray(rvalues, kind=kind, fill_value=0)
self._check_numeric_ops(a, b, values, rvalues, mix, op)
```

## Next Steps


---

*Source: test_arithmetics.py:141 | Complexity: Intermediate | Last updated: 2026-06-02*