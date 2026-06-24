# How To: Ufunc Unary

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test ufunc unary

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas._testing`
- `pandas.arrays`

**Setup Required:**
```python
# Fixtures: ufunc
```

## Step-by-Step Guide

### Step 1: Assign arr = NumpyExtensionArray(...)

```python
arr = NumpyExtensionArray(np.array([-1.0, 0.0, 1.0]))
```

### Step 2: Assign result = ufunc(...)

```python
result = ufunc(arr)
```

### Step 3: Assign expected = NumpyExtensionArray(...)

```python
expected = NumpyExtensionArray(ufunc(arr._ndarray))
```

### Step 4: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 5: Assign out = NumpyExtensionArray(...)

```python
out = NumpyExtensionArray(np.array([-9.0, -9.0, -9.0]))
```

### Step 6: Call ufunc()

```python
ufunc(arr, out=out)
```

### Step 7: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(out, expected)
```


## Complete Example

```python
# Setup
# Fixtures: ufunc

# Workflow
arr = NumpyExtensionArray(np.array([-1.0, 0.0, 1.0]))
result = ufunc(arr)
expected = NumpyExtensionArray(ufunc(arr._ndarray))
tm.assert_extension_array_equal(result, expected)
out = NumpyExtensionArray(np.array([-9.0, -9.0, -9.0]))
ufunc(arr, out=out)
tm.assert_extension_array_equal(out, expected)
```

## Next Steps


---

*Source: test_numpy.py:234 | Complexity: Intermediate | Last updated: 2026-06-02*