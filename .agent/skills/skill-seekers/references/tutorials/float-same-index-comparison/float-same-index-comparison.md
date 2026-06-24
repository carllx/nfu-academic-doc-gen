# How To: Float Same Index Comparison

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test float same index comparison

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
rvalues = np.array([np.nan, 2, 3, 4, np.nan, 0, 1, 3, 2, np.nan])
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

### Step 6: Assign values = np.array(...)

```python
values = np.array([0.0, 1.0, 2.0, 6.0, 0.0, 0.0, 1.0, 2.0, 1.0, 0.0])
```

### Step 7: Assign rvalues = np.array(...)

```python
rvalues = np.array([0.0, 2.0, 3.0, 4.0, 0.0, 0.0, 1.0, 3.0, 2.0, 0.0])
```

### Step 8: Assign a = SparseArray(...)

```python
a = SparseArray(values, kind=kind, fill_value=0)
```

### Step 9: Assign b = SparseArray(...)

```python
b = SparseArray(rvalues, kind=kind, fill_value=0)
```

### Step 10: Call self._check_comparison_ops()

```python
self._check_comparison_ops(a, b, values, rvalues)
```


## Complete Example

```python
# Setup
# Fixtures: kind

# Workflow
values = np.array([np.nan, 1, 2, 0, np.nan, 0, 1, 2, 1, np.nan])
rvalues = np.array([np.nan, 2, 3, 4, np.nan, 0, 1, 3, 2, np.nan])
a = SparseArray(values, kind=kind)
b = SparseArray(rvalues, kind=kind)
self._check_comparison_ops(a, b, values, rvalues)
values = np.array([0.0, 1.0, 2.0, 6.0, 0.0, 0.0, 1.0, 2.0, 1.0, 0.0])
rvalues = np.array([0.0, 2.0, 3.0, 4.0, 0.0, 0.0, 1.0, 3.0, 2.0, 0.0])
a = SparseArray(values, kind=kind, fill_value=0)
b = SparseArray(rvalues, kind=kind, fill_value=0)
self._check_comparison_ops(a, b, values, rvalues)
```

## Next Steps


---

*Source: test_arithmetics.py:164 | Complexity: Advanced | Last updated: 2026-06-02*