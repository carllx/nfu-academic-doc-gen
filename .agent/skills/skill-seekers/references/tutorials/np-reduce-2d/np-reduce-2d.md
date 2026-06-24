# How To: Np Reduce 2D

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test np reduce 2d

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.arrays`


## Step-by-Step Guide

### Step 1: Assign raw = np.arange.reshape(...)

```python
raw = np.arange(12).reshape(4, 3)
```

### Step 2: Assign arr = NumpyExtensionArray(...)

```python
arr = NumpyExtensionArray(raw)
```

### Step 3: Assign res = np.maximum.reduce(...)

```python
res = np.maximum.reduce(arr, axis=0)
```

### Step 4: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(res, arr[-1])
```

### Step 5: Assign alt = arr.max(...)

```python
alt = arr.max(axis=0)
```

### Step 6: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(alt, arr[-1])
```


## Complete Example

```python
# Workflow
raw = np.arange(12).reshape(4, 3)
arr = NumpyExtensionArray(raw)
res = np.maximum.reduce(arr, axis=0)
tm.assert_extension_array_equal(res, arr[-1])
alt = arr.max(axis=0)
tm.assert_extension_array_equal(alt, arr[-1])
```

## Next Steps


---

*Source: test_numpy.py:218 | Complexity: Intermediate | Last updated: 2026-06-02*