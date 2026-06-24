# How To: Ufuncs Single Float

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test ufuncs single float

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: ufunc
```

## Step-by-Step Guide

### Step 1: Assign a = pd.array(...)

```python
a = pd.array([1.0, 0.2, 3.0, np.nan], dtype='Float64')
```

### Step 2: Call tm.assert_extension_array_equal()

```python
tm.assert_extension_array_equal(result, expected)
```

### Step 3: Assign s = pd.Series(...)

```python
s = pd.Series(a)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign result = ufunc(...)

```python
result = ufunc(a)
```

### Step 6: Assign expected = pd.array(...)

```python
expected = pd.array(ufunc(a.astype(float)), dtype='Float64')
```

### Step 7: Assign result = ufunc(...)

```python
result = ufunc(s)
```

### Step 8: Assign expected = pd.Series(...)

```python
expected = pd.Series(ufunc(s.astype(float)), dtype='Float64')
```


## Complete Example

```python
# Setup
# Fixtures: ufunc

# Workflow
a = pd.array([1.0, 0.2, 3.0, np.nan], dtype='Float64')
with np.errstate(invalid='ignore'):
    result = ufunc(a)
    expected = pd.array(ufunc(a.astype(float)), dtype='Float64')
tm.assert_extension_array_equal(result, expected)
s = pd.Series(a)
with np.errstate(invalid='ignore'):
    result = ufunc(s)
    expected = pd.Series(ufunc(s.astype(float)), dtype='Float64')
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_function.py:26 | Complexity: Advanced | Last updated: 2026-06-02*