# How To: Unary Nullable

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test unary nullable

## Prerequisites

**Required Modules:**
- `decimal`
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign df = pd.DataFrame(...)

```python
df = pd.DataFrame({'a': pd.array([1, -2, 3, pd.NA], dtype='Int64'), 'b': pd.array([4.0, -5.0, 6.0, pd.NA], dtype='Float32'), 'c': pd.array([True, False, False, pd.NA], dtype='boolean'), 'd': np.array([True, False, False, True])})
```

### Step 2: Assign result = value

```python
result = +df
```

### Step 3: Assign res_ufunc = np.positive(...)

```python
res_ufunc = np.positive(df)
```

### Step 4: Assign expected = df

```python
expected = df
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res_ufunc, expected)
```

### Step 7: Assign result = value

```python
result = -df
```

### Step 8: Assign res_ufunc = np.negative(...)

```python
res_ufunc = np.negative(df)
```

### Step 9: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'a': pd.array([-1, 2, -3, pd.NA], dtype='Int64'), 'b': pd.array([-4.0, 5.0, -6.0, pd.NA], dtype='Float32'), 'c': pd.array([False, True, True, pd.NA], dtype='boolean'), 'd': np.array([False, True, True, False])})
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res_ufunc, expected)
```

### Step 12: Assign result = abs(...)

```python
result = abs(df)
```

### Step 13: Assign res_ufunc = np.abs(...)

```python
res_ufunc = np.abs(df)
```

### Step 14: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'a': pd.array([1, 2, 3, pd.NA], dtype='Int64'), 'b': pd.array([4.0, 5.0, 6.0, pd.NA], dtype='Float32'), 'c': pd.array([True, False, False, pd.NA], dtype='boolean'), 'd': np.array([True, False, False, True])})
```

### Step 15: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res_ufunc, expected)
```


## Complete Example

```python
# Workflow
df = pd.DataFrame({'a': pd.array([1, -2, 3, pd.NA], dtype='Int64'), 'b': pd.array([4.0, -5.0, 6.0, pd.NA], dtype='Float32'), 'c': pd.array([True, False, False, pd.NA], dtype='boolean'), 'd': np.array([True, False, False, True])})
result = +df
res_ufunc = np.positive(df)
expected = df
tm.assert_frame_equal(result, expected)
tm.assert_frame_equal(res_ufunc, expected)
result = -df
res_ufunc = np.negative(df)
expected = pd.DataFrame({'a': pd.array([-1, 2, -3, pd.NA], dtype='Int64'), 'b': pd.array([-4.0, 5.0, -6.0, pd.NA], dtype='Float32'), 'c': pd.array([False, True, True, pd.NA], dtype='boolean'), 'd': np.array([False, True, True, False])})
tm.assert_frame_equal(result, expected)
tm.assert_frame_equal(res_ufunc, expected)
result = abs(df)
res_ufunc = np.abs(df)
expected = pd.DataFrame({'a': pd.array([1, 2, 3, pd.NA], dtype='Int64'), 'b': pd.array([4.0, 5.0, 6.0, pd.NA], dtype='Float32'), 'c': pd.array([True, False, False, pd.NA], dtype='boolean'), 'd': np.array([True, False, False, True])})
tm.assert_frame_equal(result, expected)
tm.assert_frame_equal(res_ufunc, expected)
```

## Next Steps


---

*Source: test_unary.py:152 | Complexity: Advanced | Last updated: 2026-06-02*