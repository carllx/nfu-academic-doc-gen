# How To: Set Fill Value

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test set fill value

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas._libs.sparse`
- `pandas.compat.numpy`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.sparse`


## Step-by-Step Guide

### Step 1: Assign arr = SparseArray(...)

```python
arr = SparseArray([1.0, np.nan, 2.0], fill_value=np.nan)
```

**Verification:**
```python
assert arr.fill_value == 2
```

### Step 2: Assign arr.fill_value = 2

```python
arr.fill_value = 2
```

**Verification:**
```python
assert arr.fill_value == 2
```

### Step 3: Assign arr = SparseArray(...)

```python
arr = SparseArray([1, 0, 2], fill_value=0, dtype=np.int64)
```

**Verification:**
```python
assert arr.fill_value == 3.1
```

### Step 4: Assign arr.fill_value = 2

```python
arr.fill_value = 2
```

**Verification:**
```python
assert np.isnan(arr.fill_value)
```

### Step 5: Assign msg = 'Allowing arbitrary scalar fill_value in SparseDtype is deprecated'

```python
msg = 'Allowing arbitrary scalar fill_value in SparseDtype is deprecated'
```

**Verification:**
```python
assert arr.fill_value is True
```

### Step 6: Assign arr.fill_value = value

```python
arr.fill_value = np.nan
```

**Verification:**
```python
assert np.isnan(arr.fill_value)
```

### Step 7: Assign arr = SparseArray(...)

```python
arr = SparseArray([True, False, True], fill_value=False, dtype=np.bool_)
```

### Step 8: Assign arr.fill_value = True

```python
arr.fill_value = True
```

**Verification:**
```python
assert arr.fill_value is True
```

### Step 9: Assign arr.fill_value = value

```python
arr.fill_value = np.nan
```

**Verification:**
```python
assert np.isnan(arr.fill_value)
```

### Step 10: Assign arr.fill_value = 3.1

```python
arr.fill_value = 3.1
```

### Step 11: Assign arr.fill_value = 0

```python
arr.fill_value = 0
```


## Complete Example

```python
# Workflow
arr = SparseArray([1.0, np.nan, 2.0], fill_value=np.nan)
arr.fill_value = 2
assert arr.fill_value == 2
arr = SparseArray([1, 0, 2], fill_value=0, dtype=np.int64)
arr.fill_value = 2
assert arr.fill_value == 2
msg = 'Allowing arbitrary scalar fill_value in SparseDtype is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    arr.fill_value = 3.1
assert arr.fill_value == 3.1
arr.fill_value = np.nan
assert np.isnan(arr.fill_value)
arr = SparseArray([True, False, True], fill_value=False, dtype=np.bool_)
arr.fill_value = True
assert arr.fill_value is True
with tm.assert_produces_warning(FutureWarning, match=msg):
    arr.fill_value = 0
arr.fill_value = np.nan
assert np.isnan(arr.fill_value)
```

## Next Steps


---

*Source: test_array.py:47 | Complexity: Advanced | Last updated: 2026-06-02*