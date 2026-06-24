# How To: Ufuncs Unary

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test ufuncs unary

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
result = ufunc(a)
```

### Step 3: Assign expected = pd.array(...)

```python
expected = pd.array(ufunc(a._data), dtype='boolean')
```

### Step 4: Assign unknown = value

```python
expected[a._mask] = np.nan
```

### Step 5: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 6: Assign ser = pd.Series(...)

```python
ser = pd.Series(a)
```

### Step 7: Assign result = ufunc(...)

```python
result = ufunc(ser)
```

### Step 8: Assign expected = pd.Series(...)

```python
expected = pd.Series(ufunc(a._data), dtype='boolean')
```

### Step 9: Assign unknown = value

```python
expected[a._mask] = np.nan
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: ufunc

# Workflow
a = pd.array([True, False, None], dtype='boolean')
result = ufunc(a)
expected = pd.array(ufunc(a._data), dtype='boolean')
expected[a._mask] = np.nan
tm.assert_extension_array_equal(result, expected)
ser = pd.Series(a)
result = ufunc(ser)
expected = pd.Series(ufunc(a._data), dtype='boolean')
expected[a._mask] = np.nan
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_function.py:55 | Complexity: Advanced | Last updated: 2026-06-02*