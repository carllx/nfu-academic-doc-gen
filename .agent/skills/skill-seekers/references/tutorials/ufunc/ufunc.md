# How To: Ufunc

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ufunc

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.arrays`


## Step-by-Step Guide

### Step 1: Assign arr = NumpyExtensionArray(...)

```python
arr = NumpyExtensionArray(np.array([-1.0, 0.0, 1.0]))
```

### Step 2: Assign unknown = np.divmod(...)

```python
r1, r2 = np.divmod(arr, np.add(arr, 2))
```

### Step 3: Assign unknown = np.divmod(...)

```python
e1, e2 = np.divmod(arr._ndarray, np.add(arr._ndarray, 2))
```

### Step 4: Assign e1 = NumpyExtensionArray(...)

```python
e1 = NumpyExtensionArray(e1)
```

### Step 5: Assign e2 = NumpyExtensionArray(...)

```python
e2 = NumpyExtensionArray(e2)
```

### Step 6: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(r1, e1)
```

### Step 7: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(r2, e2)
```


## Complete Example

```python
# Workflow
arr = NumpyExtensionArray(np.array([-1.0, 0.0, 1.0]))
r1, r2 = np.divmod(arr, np.add(arr, 2))
e1, e2 = np.divmod(arr._ndarray, np.add(arr._ndarray, 2))
e1 = NumpyExtensionArray(e1)
e2 = NumpyExtensionArray(e2)
tm.assert_extension_array_equal(r1, e1)
tm.assert_extension_array_equal(r2, e2)
```

## Next Steps


---

*Source: test_numpy.py:246 | Complexity: Intermediate | Last updated: 2026-06-02*