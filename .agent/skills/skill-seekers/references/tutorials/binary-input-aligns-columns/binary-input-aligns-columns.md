# How To: Binary Input Aligns Columns

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test binary input aligns columns

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `functools`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.api.types`

**Setup Required:**
```python
# Fixtures: request, dtype_a, dtype_b
```

## Step-by-Step Guide

### Step 1: Assign df1 = pd.DataFrame.astype(...)

```python
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}).astype(dtype_a)
```

### Step 2: Assign df2 = pd.DataFrame.astype(...)

```python
df2 = pd.DataFrame({'A': [1, 2], 'C': [3, 4]}).astype(dtype_b)
```

### Step 3: Assign result = np.heaviside(...)

```python
result = np.heaviside(df1, df2)
```

### Step 4: Assign expected = np.heaviside(...)

```python
expected = np.heaviside(np.array([[1, 3, np.nan], [2, 4, np.nan]]), np.array([[1, np.nan, 3], [2, np.nan, 4]]))
```

### Step 5: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame(expected, index=[0, 1], columns=['A', 'B', 'C'])
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign result = np.heaviside(...)

```python
result = np.heaviside(df1, df2.values)
```

### Step 8: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame([[1.0, 1.0], [1.0, 1.0]], columns=['A', 'B'])
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Call request.applymarker()

```python
request.applymarker(pytest.mark.xfail(reason='Extension / mixed with multiple inputs not implemented.'))
```

### Step 11: Assign dtype_b = dtype_b.copy(...)

```python
dtype_b = dtype_b.copy()
```

### Step 12: Assign unknown = dtype_b.pop(...)

```python
dtype_b['C'] = dtype_b.pop('B')
```


## Complete Example

```python
# Setup
# Fixtures: request, dtype_a, dtype_b

# Workflow
if is_extension_array_dtype(dtype_a) or isinstance(dtype_a, dict) or is_extension_array_dtype(dtype_b) or isinstance(dtype_b, dict):
    request.applymarker(pytest.mark.xfail(reason='Extension / mixed with multiple inputs not implemented.'))
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}).astype(dtype_a)
if isinstance(dtype_a, dict) and isinstance(dtype_b, dict):
    dtype_b = dtype_b.copy()
    dtype_b['C'] = dtype_b.pop('B')
df2 = pd.DataFrame({'A': [1, 2], 'C': [3, 4]}).astype(dtype_b)
result = np.heaviside(df1, df2)
expected = np.heaviside(np.array([[1, 3, np.nan], [2, 4, np.nan]]), np.array([[1, np.nan, 3], [2, np.nan, 4]]))
expected = pd.DataFrame(expected, index=[0, 1], columns=['A', 'B', 'C'])
tm.assert_frame_equal(result, expected)
result = np.heaviside(df1, df2.values)
expected = pd.DataFrame([[1.0, 1.0], [1.0, 1.0]], columns=['A', 'B'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_ufunc.py:102 | Complexity: Advanced | Last updated: 2026-06-02*