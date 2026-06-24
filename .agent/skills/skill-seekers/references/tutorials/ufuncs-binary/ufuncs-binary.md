# How To: Ufuncs Binary

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test ufuncs binary

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: ufunc
```

## Step-by-Step Guide

### Step 1: Assign a = pd.array(...)

```python
a = pd.array([True, False, None], dtype='boolean')
```

### Step 2: Assign result = ufunc(...)

```python
result = ufunc(a, a)
```

### Step 3: Assign expected = pd.array(...)

```python
expected = pd.array(ufunc(a._data, a._data), dtype='boolean')
```

### Step 4: Assign unknown = value

```python
expected[a._mask] = np.nan
```

### Step 5: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 6: Assign s = pd.Series(...)

```python
s = pd.Series(a)
```

### Step 7: Assign result = ufunc(...)

```python
result = ufunc(s, a)
```

### Step 8: Assign expected = pd.Series(...)

```python
expected = pd.Series(ufunc(a._data, a._data), dtype='boolean')
```

### Step 9: Assign unknown = value

```python
expected[a._mask] = np.nan
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 11: Assign arr = np.array(...)

```python
arr = np.array([True, True, False])
```

### Step 12: Assign result = ufunc(...)

```python
result = ufunc(a, arr)
```

### Step 13: Assign expected = pd.array(...)

```python
expected = pd.array(ufunc(a._data, arr), dtype='boolean')
```

### Step 14: Assign unknown = value

```python
expected[a._mask] = np.nan
```

### Step 15: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 16: Assign result = ufunc(...)

```python
result = ufunc(arr, a)
```

### Step 17: Assign expected = pd.array(...)

```python
expected = pd.array(ufunc(arr, a._data), dtype='boolean')
```

### Step 18: Assign unknown = value

```python
expected[a._mask] = np.nan
```

### Step 19: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 20: Assign result = ufunc(...)

```python
result = ufunc(a, True)
```

### Step 21: Assign expected = pd.array(...)

```python
expected = pd.array(ufunc(a._data, True), dtype='boolean')
```

### Step 22: Assign unknown = value

```python
expected[a._mask] = np.nan
```

### Step 23: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 24: Assign result = ufunc(...)

```python
result = ufunc(True, a)
```

### Step 25: Assign expected = pd.array(...)

```python
expected = pd.array(ufunc(True, a._data), dtype='boolean')
```

### Step 26: Assign unknown = value

```python
expected[a._mask] = np.nan
```

### Step 27: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 28: Assign msg = 'operand type\\(s\\) all returned NotImplemented from __array_ufunc__'

```python
msg = 'operand type\\(s\\) all returned NotImplemented from __array_ufunc__'
```

### Step 29: Call ufunc()

```python
ufunc(a, 'test')
```


## Complete Example

```python
# Setup
# Fixtures: ufunc

# Workflow
a = pd.array([True, False, None], dtype='boolean')
result = ufunc(a, a)
expected = pd.array(ufunc(a._data, a._data), dtype='boolean')
expected[a._mask] = np.nan
tm.assert_extension_array_equal(result, expected)
s = pd.Series(a)
result = ufunc(s, a)
expected = pd.Series(ufunc(a._data, a._data), dtype='boolean')
expected[a._mask] = np.nan
tm.assert_series_equal(result, expected)
arr = np.array([True, True, False])
result = ufunc(a, arr)
expected = pd.array(ufunc(a._data, arr), dtype='boolean')
expected[a._mask] = np.nan
tm.assert_extension_array_equal(result, expected)
result = ufunc(arr, a)
expected = pd.array(ufunc(arr, a._data), dtype='boolean')
expected[a._mask] = np.nan
tm.assert_extension_array_equal(result, expected)
result = ufunc(a, True)
expected = pd.array(ufunc(a._data, True), dtype='boolean')
expected[a._mask] = np.nan
tm.assert_extension_array_equal(result, expected)
result = ufunc(True, a)
expected = pd.array(ufunc(True, a._data), dtype='boolean')
expected[a._mask] = np.nan
tm.assert_extension_array_equal(result, expected)
msg = 'operand type\\(s\\) all returned NotImplemented from __array_ufunc__'
with pytest.raises(TypeError, match=msg):
    ufunc(a, 'test')
```

## Next Steps


---

*Source: test_function.py:11 | Complexity: Advanced | Last updated: 2026-06-02*