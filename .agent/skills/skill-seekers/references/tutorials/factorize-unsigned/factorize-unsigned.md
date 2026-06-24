# How To: Factorize Unsigned

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test factorize unsigned

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.arrays`


## Step-by-Step Guide

### Step 1: Assign arr = np.array(...)

```python
arr = np.array([1, 2, 3], dtype=np.uint64)
```

### Step 2: Assign obj = NumpyExtensionArray(...)

```python
obj = NumpyExtensionArray(arr)
```

### Step 3: Assign unknown = obj.factorize(...)

```python
res_codes, res_unique = obj.factorize()
```

### Step 4: Assign unknown = pd.factorize(...)

```python
exp_codes, exp_unique = pd.factorize(arr)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(res_codes, exp_codes)
```

### Step 6: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(res_unique, NumpyExtensionArray(exp_unique))
```


## Complete Example

```python
# Workflow
arr = np.array([1, 2, 3], dtype=np.uint64)
obj = NumpyExtensionArray(arr)
res_codes, res_unique = obj.factorize()
exp_codes, exp_unique = pd.factorize(arr)
tm.assert_numpy_array_equal(res_codes, exp_codes)
tm.assert_extension_array_equal(res_unique, NumpyExtensionArray(exp_unique))
```

## Next Steps


---

*Source: test_numpy.py:314 | Complexity: Intermediate | Last updated: 2026-06-02*