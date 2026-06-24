# How To: Divmod Ufunc

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test divmod ufunc

## Prerequisites

**Required Modules:**
- `datetime`
- `pickle`
- `numpy`
- `pytest`
- `pandas._libs.missing`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign a = np.array(...)

```python
a = np.array([1, 2, 3])
```

**Verification:**
```python
assert isinstance(result, tuple)
```

### Step 2: Assign expected = np.array(...)

```python
expected = np.array([NA, NA, NA], dtype=object)
```

### Step 3: Assign result = np.divmod(...)

```python
result = np.divmod(a, NA)
```

**Verification:**
```python
assert isinstance(result, tuple)
```

### Step 4: Assign result = np.divmod(...)

```python
result = np.divmod(NA, a)
```

### Step 5: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(arr, expected)
```

### Step 6: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(arr, expected)
```

### Step 7: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(arr, expected)
```

### Step 8: Call tm.assert_numpy_array_equal()

```python
tm.assert_numpy_array_equal(arr, expected)
```


## Complete Example

```python
# Workflow
a = np.array([1, 2, 3])
expected = np.array([NA, NA, NA], dtype=object)
result = np.divmod(a, NA)
assert isinstance(result, tuple)
for arr in result:
    tm.assert_numpy_array_equal(arr, expected)
    tm.assert_numpy_array_equal(arr, expected)
result = np.divmod(NA, a)
for arr in result:
    tm.assert_numpy_array_equal(arr, expected)
    tm.assert_numpy_array_equal(arr, expected)
```

## Next Steps


---

*Source: test_na_scalar.py:262 | Complexity: Advanced | Last updated: 2026-06-02*