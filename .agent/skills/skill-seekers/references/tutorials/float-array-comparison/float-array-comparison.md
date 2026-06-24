# How To: Float Array Comparison

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test float array comparison

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
# Fixtures: kind
```

## Step-by-Step Guide

### Step 1: Assign values = np.array(...)

```python
values = np.array([np.nan, 1, 2, 0, np.nan, 0, 1, 2, 1, np.nan])
```

### Step 2: Assign rvalues = np.array(...)

```python
rvalues = np.array([2, np.nan, 2, 3, np.nan, 0, 1, 5, 2, np.nan])
```

### Step 3: Assign a = SparseArray(...)

```python
a = SparseArray(values, kind=kind)
```

### Step 4: Assign b = SparseArray(...)

```python
b = SparseArray(rvalues, kind=kind)
```

### Step 5: Call self._check_comparison_ops()

```python
self._check_comparison_ops(a, b, values, rvalues)
```

### Step 6: Call self._check_comparison_ops()

```python
self._check_comparison_ops(a, b * 0, values, rvalues * 0)
```

### Step 7: Assign a = SparseArray(...)

```python
a = SparseArray(values, kind=kind, fill_value=0)
```

### Step 8: Assign b = SparseArray(...)

```python
b = SparseArray(rvalues, kind=kind)
```

### Step 9: Call self._check_comparison_ops()

```python
self._check_comparison_ops(a, b, values, rvalues)
```

### Step 10: Assign a = SparseArray(...)

```python
a = SparseArray(values, kind=kind, fill_value=0)
```

### Step 11: Assign b = SparseArray(...)

```python
b = SparseArray(rvalues, kind=kind, fill_value=0)
```

### Step 12: Call self._check_comparison_ops()

```python
self._check_comparison_ops(a, b, values, rvalues)
```

### Step 13: Assign a = SparseArray(...)

```python
a = SparseArray(values, kind=kind, fill_value=1)
```

### Step 14: Assign b = SparseArray(...)

```python
b = SparseArray(rvalues, kind=kind, fill_value=2)
```

### Step 15: Call self._check_comparison_ops()

```python
self._check_comparison_ops(a, b, values, rvalues)
```


## Complete Example

```python
# Setup
# Fixtures: kind

# Workflow
values = np.array([np.nan, 1, 2, 0, np.nan, 0, 1, 2, 1, np.nan])
rvalues = np.array([2, np.nan, 2, 3, np.nan, 0, 1, 5, 2, np.nan])
a = SparseArray(values, kind=kind)
b = SparseArray(rvalues, kind=kind)
self._check_comparison_ops(a, b, values, rvalues)
self._check_comparison_ops(a, b * 0, values, rvalues * 0)
a = SparseArray(values, kind=kind, fill_value=0)
b = SparseArray(rvalues, kind=kind)
self._check_comparison_ops(a, b, values, rvalues)
a = SparseArray(values, kind=kind, fill_value=0)
b = SparseArray(rvalues, kind=kind, fill_value=0)
self._check_comparison_ops(a, b, values, rvalues)
a = SparseArray(values, kind=kind, fill_value=1)
b = SparseArray(rvalues, kind=kind, fill_value=2)
self._check_comparison_ops(a, b, values, rvalues)
```

## Next Steps


---

*Source: test_arithmetics.py:226 | Complexity: Advanced | Last updated: 2026-06-02*