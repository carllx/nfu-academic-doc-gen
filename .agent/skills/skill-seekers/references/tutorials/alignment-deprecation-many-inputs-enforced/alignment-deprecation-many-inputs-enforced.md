# How To: Alignment Deprecation Many Inputs Enforced

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test alignment deprecation many inputs enforced

## Prerequisites

**Required Modules:**
- `functools`
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.api.types`


## Step-by-Step Guide

### Step 1: Assign numba = pytest.importorskip(...)

```python
numba = pytest.importorskip('numba')
```

### Step 2: Assign df1 = pd.DataFrame(...)

```python
df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
```

### Step 3: Assign df2 = pd.DataFrame(...)

```python
df2 = pd.DataFrame({'b': [1, 2, 3], 'c': [4, 5, 6]})
```

### Step 4: Assign df3 = pd.DataFrame(...)

```python
df3 = pd.DataFrame({'a': [1, 2, 3], 'c': [4, 5, 6]})
```

### Step 5: Assign result = my_ufunc(...)

```python
result = my_ufunc(df1, df2, df3)
```

### Step 6: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame(np.full((3, 3), np.nan), columns=['a', 'b', 'c'])
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame([[3.0, 12.0], [6.0, 15.0], [9.0, 18.0]], columns=['a', 'b'])
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Assign msg = 'operands could not be broadcast together with shapes \\(3,3\\) \\(3,3\\) \\(3,2\\)'

```python
msg = 'operands could not be broadcast together with shapes \\(3,3\\) \\(3,3\\) \\(3,2\\)'
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 12: Assign msg = 'operands could not be broadcast together with shapes \\(3,2\\) \\(3,3\\) \\(3,3\\)'

```python
msg = 'operands could not be broadcast together with shapes \\(3,2\\) \\(3,3\\) \\(3,3\\)'
```

### Step 13: Assign result = my_ufunc(...)

```python
result = my_ufunc(df1, df1, df1)
```

### Step 14: Call my_ufunc()

```python
my_ufunc(df1, df2, df3.values)
```

### Step 15: Assign result = my_ufunc(...)

```python
result = my_ufunc(df1, df2.values, df3.values)
```

### Step 16: Call my_ufunc()

```python
my_ufunc(df1.values, df2, df3)
```


## Complete Example

```python
# Workflow
numba = pytest.importorskip('numba')

@numba.vectorize([numba.float64(numba.float64, numba.float64, numba.float64)])
def my_ufunc(x, y, z):
    return x + y + z
df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
df2 = pd.DataFrame({'b': [1, 2, 3], 'c': [4, 5, 6]})
df3 = pd.DataFrame({'a': [1, 2, 3], 'c': [4, 5, 6]})
result = my_ufunc(df1, df2, df3)
expected = pd.DataFrame(np.full((3, 3), np.nan), columns=['a', 'b', 'c'])
tm.assert_frame_equal(result, expected)
with tm.assert_produces_warning(None):
    result = my_ufunc(df1, df1, df1)
expected = pd.DataFrame([[3.0, 12.0], [6.0, 15.0], [9.0, 18.0]], columns=['a', 'b'])
tm.assert_frame_equal(result, expected)
msg = 'operands could not be broadcast together with shapes \\(3,3\\) \\(3,3\\) \\(3,2\\)'
with pytest.raises(ValueError, match=msg):
    my_ufunc(df1, df2, df3.values)
with tm.assert_produces_warning(None):
    result = my_ufunc(df1, df2.values, df3.values)
tm.assert_frame_equal(result, expected)
msg = 'operands could not be broadcast together with shapes \\(3,2\\) \\(3,3\\) \\(3,3\\)'
with pytest.raises(ValueError, match=msg):
    my_ufunc(df1.values, df2, df3)
```

## Next Steps


---

*Source: test_ufunc.py:248 | Complexity: Advanced | Last updated: 2026-06-02*