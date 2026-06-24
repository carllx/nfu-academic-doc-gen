# How To: Compare Ea And Np Dtype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test compare ea and np dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: val1, val2
```

## Step-by-Step Guide

### Step 1: Assign arr = value

```python
arr = [4.0, val1]
```

### Step 2: Assign ser = pd.Series(...)

```python
ser = pd.Series([1, val2], dtype='Int64')
```

### Step 3: Assign df1 = pd.DataFrame(...)

```python
df1 = pd.DataFrame({'a': arr, 'b': [1.0, 2]})
```

### Step 4: Assign df2 = pd.DataFrame(...)

```python
df2 = pd.DataFrame({'a': ser, 'b': [1.0, 2]})
```

### Step 5: Assign expected = pd.DataFrame(...)

```python
expected = pd.DataFrame({('a', 'self'): arr, ('a', 'other'): ser, ('b', 'self'): np.nan, ('b', 'other'): np.nan})
```

### Step 6: Assign unknown = value

```python
expected.loc[1, ('a', 'self')] = np.nan
```

### Step 7: Assign result = df1.compare(...)

```python
result = df1.compare(df2, keep_shape=True)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign result = df1.compare(...)

```python
result = df1.compare(df2, keep_shape=True)
```


## Complete Example

```python
# Setup
# Fixtures: val1, val2

# Workflow
arr = [4.0, val1]
ser = pd.Series([1, val2], dtype='Int64')
df1 = pd.DataFrame({'a': arr, 'b': [1.0, 2]})
df2 = pd.DataFrame({'a': ser, 'b': [1.0, 2]})
expected = pd.DataFrame({('a', 'self'): arr, ('a', 'other'): ser, ('b', 'self'): np.nan, ('b', 'other'): np.nan})
if val1 is pd.NA and val2 is pd.NA:
    expected.loc[1, ('a', 'self')] = np.nan
if val1 is pd.NA and np_version_gte1p25:
    with pytest.raises(TypeError, match='boolean value of NA is ambiguous'):
        result = df1.compare(df2, keep_shape=True)
else:
    result = df1.compare(df2, keep_shape=True)
    tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_compare.py:253 | Complexity: Advanced | Last updated: 2026-06-02*