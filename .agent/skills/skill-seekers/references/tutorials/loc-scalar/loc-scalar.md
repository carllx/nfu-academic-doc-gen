# How To: Loc Scalar

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc scalar

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: df
```

## Step-by-Step Guide

### Step 1: Assign dtype = CategoricalDtype(...)

```python
dtype = CategoricalDtype(list('cab'))
```

**Verification:**
```python
assert bidx.dtype == dtype
```

### Step 2: Assign result = value

```python
result = df.loc['a']
```

**Verification:**
```python
assert bidx2.dtype == dtype
```

### Step 3: Assign bidx = Series.astype(...)

```python
bidx = Series(list('aaa'), name='B').astype(dtype)
```

**Verification:**
```python
assert bidx.dtype == dtype
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [0, 1, 5]}, index=Index(bidx))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign df = df.copy(...)

```python
df = df.copy()
```

### Step 7: Assign unknown = 20

```python
df.loc['a'] = 20
```

### Step 8: Assign bidx2 = Series.astype(...)

```python
bidx2 = Series(list('aabbca'), name='B').astype(dtype)
```

**Verification:**
```python
assert bidx2.dtype == dtype
```

### Step 9: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [20, 20, 2, 3, 4, 20]}, index=Index(bidx2))
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

### Step 11: Assign df2 = df.copy(...)

```python
df2 = df.copy()
```

### Step 12: Assign expected = df2.copy(...)

```python
expected = df2.copy()
```

### Step 13: Assign expected.index = expected.index.astype(...)

```python
expected.index = expected.index.astype(object)
```

### Step 14: Assign unknown = 10

```python
expected.loc['d'] = 10
```

### Step 15: Assign unknown = 10

```python
df2.loc['d'] = 10
```

### Step 16: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df2, expected)
```

### Step 17: df.loc['d']

```python
df.loc['d']
```


## Complete Example

```python
# Setup
# Fixtures: df

# Workflow
dtype = CategoricalDtype(list('cab'))
result = df.loc['a']
bidx = Series(list('aaa'), name='B').astype(dtype)
assert bidx.dtype == dtype
expected = DataFrame({'A': [0, 1, 5]}, index=Index(bidx))
tm.assert_frame_equal(result, expected)
df = df.copy()
df.loc['a'] = 20
bidx2 = Series(list('aabbca'), name='B').astype(dtype)
assert bidx2.dtype == dtype
expected = DataFrame({'A': [20, 20, 2, 3, 4, 20]}, index=Index(bidx2))
tm.assert_frame_equal(df, expected)
with pytest.raises(KeyError, match="^'d'$"):
    df.loc['d']
df2 = df.copy()
expected = df2.copy()
expected.index = expected.index.astype(object)
expected.loc['d'] = 10
df2.loc['d'] = 10
tm.assert_frame_equal(df2, expected)
```

## Next Steps


---

*Source: test_categorical.py:49 | Complexity: Advanced | Last updated: 2026-06-02*