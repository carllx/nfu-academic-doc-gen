# How To: Float Scalar Comparison

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test float scalar comparison

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

### Step 2: Assign a = SparseArray(...)

```python
a = SparseArray(values, kind=kind)
```

### Step 3: Call self._check_comparison_ops()

```python
self._check_comparison_ops(a, 1, values, 1)
```

### Step 4: Call self._check_comparison_ops()

```python
self._check_comparison_ops(a, 0, values, 0)
```

### Step 5: Call self._check_comparison_ops()

```python
self._check_comparison_ops(a, 3, values, 3)
```

### Step 6: Assign a = SparseArray(...)

```python
a = SparseArray(values, kind=kind, fill_value=0)
```

### Step 7: Call self._check_comparison_ops()

```python
self._check_comparison_ops(a, 1, values, 1)
```

### Step 8: Call self._check_comparison_ops()

```python
self._check_comparison_ops(a, 0, values, 0)
```

### Step 9: Call self._check_comparison_ops()

```python
self._check_comparison_ops(a, 3, values, 3)
```

### Step 10: Assign a = SparseArray(...)

```python
a = SparseArray(values, kind=kind, fill_value=2)
```

### Step 11: Call self._check_comparison_ops()

```python
self._check_comparison_ops(a, 1, values, 1)
```

### Step 12: Call self._check_comparison_ops()

```python
self._check_comparison_ops(a, 0, values, 0)
```

### Step 13: Call self._check_comparison_ops()

```python
self._check_comparison_ops(a, 3, values, 3)
```


## Complete Example

```python
# Setup
# Fixtures: kind

# Workflow
values = np.array([np.nan, 1, 2, 0, np.nan, 0, 1, 2, 1, np.nan])
a = SparseArray(values, kind=kind)
self._check_comparison_ops(a, 1, values, 1)
self._check_comparison_ops(a, 0, values, 0)
self._check_comparison_ops(a, 3, values, 3)
a = SparseArray(values, kind=kind, fill_value=0)
self._check_comparison_ops(a, 1, values, 1)
self._check_comparison_ops(a, 0, values, 0)
self._check_comparison_ops(a, 3, values, 3)
a = SparseArray(values, kind=kind, fill_value=2)
self._check_comparison_ops(a, 1, values, 1)
self._check_comparison_ops(a, 0, values, 0)
self._check_comparison_ops(a, 3, values, 3)
```

## Next Steps


---

*Source: test_arithmetics.py:123 | Complexity: Advanced | Last updated: 2026-06-02*