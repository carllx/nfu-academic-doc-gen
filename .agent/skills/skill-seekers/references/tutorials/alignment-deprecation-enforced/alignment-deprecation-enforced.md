# How To: Alignment Deprecation Enforced

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test alignment deprecation enforced

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

### Step 1: Assign df1 = pd.DataFrame(...)

```python
df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
```

### Step 2: Assign df2 = pd.DataFrame(...)

```python
df2 = pd.DataFrame({'b': [1, 2, 3], 'c': [4, 5, 6]})
```

### Step 3: Assign s1 = pd.Series(...)

```python
s1 = pd.Series([1, 2], index=['a', 'b'])
```

### Step 4: Assign s2 = pd.Series(...)

```python
s2 = pd.Series([1, 2], index=['b', 'c'])
```

### Step 5: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'a': [2, 4, 6], 'b': [8, 10, 12]})
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign result = np.add(...)

```python
result = np.add(df1, df2.values)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign result = np.add(...)

```python
result = np.add(df1, df2)
```

### Step 10: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'a': [np.nan] * 3, 'b': [5, 7, 9], 'c': [np.nan] * 3})
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 12: Assign result = np.add(...)

```python
result = np.add(df1.values, df2)
```

### Step 13: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'b': [2, 4, 6], 'c': [8, 10, 12]})
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 15: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'a': [2, 3, 4], 'b': [6, 7, 8]})
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 17: Assign result = np.add(...)

```python
result = np.add(df1, s2.values)
```

### Step 18: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 19: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({'a': [np.nan] * 3, 'b': [5.0, 6.0, 7.0], 'c': [np.nan] * 3})
```

### Step 20: Assign result = np.add(...)

```python
result = np.add(df1, s2)
```

### Step 21: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 22: Assign msg = "Cannot apply ufunc <ufunc 'add'> to mixed DataFrame and Series inputs."

```python
msg = "Cannot apply ufunc <ufunc 'add'> to mixed DataFrame and Series inputs."
```

### Step 23: Assign result = np.add(...)

```python
result = np.add(df1, df1)
```

### Step 24: Assign result = np.add(...)

```python
result = np.add(df1, s1)
```

### Step 25: Call np.add()

```python
np.add(s2, df1)
```


## Complete Example

```python
# Workflow
df1 = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
df2 = pd.DataFrame({'b': [1, 2, 3], 'c': [4, 5, 6]})
s1 = pd.Series([1, 2], index=['a', 'b'])
s2 = pd.Series([1, 2], index=['b', 'c'])
expected = pd.DataFrame({'a': [2, 4, 6], 'b': [8, 10, 12]})
with tm.assert_produces_warning(None):
    result = np.add(df1, df1)
tm.assert_frame_equal(result, expected)
result = np.add(df1, df2.values)
tm.assert_frame_equal(result, expected)
result = np.add(df1, df2)
expected = pd.DataFrame({'a': [np.nan] * 3, 'b': [5, 7, 9], 'c': [np.nan] * 3})
tm.assert_frame_equal(result, expected)
result = np.add(df1.values, df2)
expected = pd.DataFrame({'b': [2, 4, 6], 'c': [8, 10, 12]})
tm.assert_frame_equal(result, expected)
expected = pd.DataFrame({'a': [2, 3, 4], 'b': [6, 7, 8]})
with tm.assert_produces_warning(None):
    result = np.add(df1, s1)
tm.assert_frame_equal(result, expected)
result = np.add(df1, s2.values)
tm.assert_frame_equal(result, expected)
expected = pd.DataFrame({'a': [np.nan] * 3, 'b': [5.0, 6.0, 7.0], 'c': [np.nan] * 3})
result = np.add(df1, s2)
tm.assert_frame_equal(result, expected)
msg = "Cannot apply ufunc <ufunc 'add'> to mixed DataFrame and Series inputs."
with pytest.raises(NotImplementedError, match=msg):
    np.add(s2, df1)
```

## Next Steps


---

*Source: test_ufunc.py:199 | Complexity: Advanced | Last updated: 2026-06-02*