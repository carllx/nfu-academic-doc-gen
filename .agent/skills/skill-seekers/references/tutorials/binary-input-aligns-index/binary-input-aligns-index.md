# How To: Binary Input Aligns Index

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test binary input aligns index

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
# Fixtures: request, dtype
```

## Step-by-Step Guide

### Step 1: Assign df1 = pd.DataFrame.astype(...)

```python
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['a', 'b']).astype(dtype)
```

### Step 2: Assign df2 = pd.DataFrame.astype(...)

```python
df2 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['a', 'c']).astype(dtype)
```

### Step 3: Assign result = np.heaviside(...)

```python
result = np.heaviside(df1, df2)
```

### Step 4: Assign expected = np.heaviside(...)

```python
expected = np.heaviside(np.array([[1, 3], [3, 4], [np.nan, np.nan]]), np.array([[1, 3], [np.nan, np.nan], [3, 4]]))
```

### Step 5: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame(expected, index=['a', 'b', 'c'], columns=['A', 'B'])
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
expected = pd.DataFrame([[1.0, 1.0], [1.0, 1.0]], columns=['A', 'B'], index=['a', 'b'])
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Call request.applymarker()

```python
request.applymarker(pytest.mark.xfail(reason='Extension / mixed with multiple inputs not implemented.'))
```


## Complete Example

```python
# Setup
# Fixtures: request, dtype

# Workflow
if is_extension_array_dtype(dtype) or isinstance(dtype, dict):
    request.applymarker(pytest.mark.xfail(reason='Extension / mixed with multiple inputs not implemented.'))
df1 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['a', 'b']).astype(dtype)
df2 = pd.DataFrame({'A': [1, 2], 'B': [3, 4]}, index=['a', 'c']).astype(dtype)
result = np.heaviside(df1, df2)
expected = np.heaviside(np.array([[1, 3], [3, 4], [np.nan, np.nan]]), np.array([[1, 3], [np.nan, np.nan], [3, 4]]))
expected = pd.DataFrame(expected, index=['a', 'b', 'c'], columns=['A', 'B'])
tm.assert_frame_equal(result, expected)
result = np.heaviside(df1, df2.values)
expected = pd.DataFrame([[1.0, 1.0], [1.0, 1.0]], columns=['A', 'B'], index=['a', 'b'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_ufunc.py:136 | Complexity: Advanced | Last updated: 2026-06-02*