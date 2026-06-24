# How To: Float Array Different Kind

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test float array different kind

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
# Fixtures: mix, all_arithmetic_functions
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
rvalues = np.array([2, np.nan, 2, 3, np.nan, 0, 1, 5, 2, np.nan])
```

### Step 4: Assign a = SparseArray(...)

```python
a = SparseArray(values, kind='integer')
```

### Step 5: Assign b = SparseArray(...)

```python
b = SparseArray(rvalues, kind='block')
```

### Step 6: Call self._check_numeric_ops()

```python
self._check_numeric_ops(a, b, values, rvalues, mix, op)
```

### Step 7: Call self._check_numeric_ops()

```python
self._check_numeric_ops(a, b * 0, values, rvalues * 0, mix, op)
```

### Step 8: Assign a = SparseArray(...)

```python
a = SparseArray(values, kind='integer', fill_value=0)
```

### Step 9: Assign b = SparseArray(...)

```python
b = SparseArray(rvalues, kind='block')
```

### Step 10: Call self._check_numeric_ops()

```python
self._check_numeric_ops(a, b, values, rvalues, mix, op)
```

### Step 11: Assign a = SparseArray(...)

```python
a = SparseArray(values, kind='integer', fill_value=0)
```

### Step 12: Assign b = SparseArray(...)

```python
b = SparseArray(rvalues, kind='block', fill_value=0)
```

### Step 13: Call self._check_numeric_ops()

```python
self._check_numeric_ops(a, b, values, rvalues, mix, op)
```

### Step 14: Assign a = SparseArray(...)

```python
a = SparseArray(values, kind='integer', fill_value=1)
```

### Step 15: Assign b = SparseArray(...)

```python
b = SparseArray(rvalues, kind='block', fill_value=2)
```

### Step 16: Call self._check_numeric_ops()

```python
self._check_numeric_ops(a, b, values, rvalues, mix, op)
```


## Complete Example

```python
# Setup
# Fixtures: mix, all_arithmetic_functions

# Workflow
op = all_arithmetic_functions
values = np.array([np.nan, 1, 2, 0, np.nan, 0, 1, 2, 1, np.nan])
rvalues = np.array([2, np.nan, 2, 3, np.nan, 0, 1, 5, 2, np.nan])
a = SparseArray(values, kind='integer')
b = SparseArray(rvalues, kind='block')
self._check_numeric_ops(a, b, values, rvalues, mix, op)
self._check_numeric_ops(a, b * 0, values, rvalues * 0, mix, op)
a = SparseArray(values, kind='integer', fill_value=0)
b = SparseArray(rvalues, kind='block')
self._check_numeric_ops(a, b, values, rvalues, mix, op)
a = SparseArray(values, kind='integer', fill_value=0)
b = SparseArray(rvalues, kind='block', fill_value=0)
self._check_numeric_ops(a, b, values, rvalues, mix, op)
a = SparseArray(values, kind='integer', fill_value=1)
b = SparseArray(rvalues, kind='block', fill_value=2)
self._check_numeric_ops(a, b, values, rvalues, mix, op)
```

## Next Steps


---

*Source: test_arithmetics.py:203 | Complexity: Advanced | Last updated: 2026-06-02*