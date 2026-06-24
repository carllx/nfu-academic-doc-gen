# How To: Ufuncs Binary Int

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test ufuncs binary int

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: ufunc
```

## Step-by-Step Guide

### Step 1: Assign a = pd.array(...)

```python
a = pd.array([1, 2, -3, np.nan])
```

### Step 2: Assign result = ufunc(...)

```python
result = ufunc(a, a)
```

### Step 3: Assign expected = pd.array(...)

```python
expected = pd.array(ufunc(a.astype(float), a.astype(float)), dtype='Int64')
```

### Step 4: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 5: Assign arr = np.array(...)

```python
arr = np.array([1, 2, 3, 4])
```

### Step 6: Assign result = ufunc(...)

```python
result = ufunc(a, arr)
```

### Step 7: Assign expected = pd.array(...)

```python
expected = pd.array(ufunc(a.astype(float), arr), dtype='Int64')
```

### Step 8: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 9: Assign result = ufunc(...)

```python
result = ufunc(arr, a)
```

### Step 10: Assign expected = pd.array(...)

```python
expected = pd.array(ufunc(arr, a.astype(float)), dtype='Int64')
```

### Step 11: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 12: Assign result = ufunc(...)

```python
result = ufunc(a, 1)
```

### Step 13: Assign expected = pd.array(...)

```python
expected = pd.array(ufunc(a.astype(float), 1), dtype='Int64')
```

### Step 14: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 15: Assign result = ufunc(...)

```python
result = ufunc(1, a)
```

### Step 16: Assign expected = pd.array(...)

```python
expected = pd.array(ufunc(1, a.astype(float)), dtype='Int64')
```

### Step 17: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: ufunc

# Workflow
a = pd.array([1, 2, -3, np.nan])
result = ufunc(a, a)
expected = pd.array(ufunc(a.astype(float), a.astype(float)), dtype='Int64')
tm.assert_extension_array_equal(result, expected)
arr = np.array([1, 2, 3, 4])
result = ufunc(a, arr)
expected = pd.array(ufunc(a.astype(float), arr), dtype='Int64')
tm.assert_extension_array_equal(result, expected)
result = ufunc(arr, a)
expected = pd.array(ufunc(arr, a.astype(float)), dtype='Int64')
tm.assert_extension_array_equal(result, expected)
result = ufunc(a, 1)
expected = pd.array(ufunc(a.astype(float), 1), dtype='Int64')
tm.assert_extension_array_equal(result, expected)
result = ufunc(1, a)
expected = pd.array(ufunc(1, a.astype(float)), dtype='Int64')
tm.assert_extension_array_equal(result, expected)
```

## Next Steps


---

*Source: test_function.py:40 | Complexity: Advanced | Last updated: 2026-06-02*