# How To: Unary Op

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test unary op

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: op, fill_value
```

## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array([0, 1, np.nan, 2])
```

### Step 2: Assign sparray = SparseArray(...)

```python
sparray = SparseArray(arr, fill_value=fill_value)
```

### Step 3: Assign result = op(...)

```python
result = op(sparray)
```

### Step 4: Assign expected = SparseArray(...)

```python
expected = SparseArray(op(arr), fill_value=op(fill_value))
```

### Step 5: Call tm.assert_sp_array_equal()

```python
tm.assert_sp_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: op, fill_value

# Workflow
arr = np.array([0, 1, np.nan, 2])
sparray = SparseArray(arr, fill_value=fill_value)
result = op(sparray)
expected = SparseArray(op(arr), fill_value=op(fill_value))
tm.assert_sp_array_equal(result, expected)
```

## Next Steps


---

*Source: test_unary.py:14 | Complexity: Intermediate | Last updated: 2026-06-02*