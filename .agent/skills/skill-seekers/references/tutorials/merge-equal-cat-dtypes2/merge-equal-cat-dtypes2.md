# How To: Merge Equal Cat Dtypes2

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test merge equal cat dtypes2

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.dtypes`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.reshape.concat`
- `pandas.core.reshape.merge`


## Step-by-Step Guide

### Step 1: Assign cat_dtype = CategoricalDtype(...)

```python
cat_dtype = CategoricalDtype(categories=['a', 'b', 'c'], ordered=False)
```

### Step 2: Assign df1 = DataFrame.set_index(...)

```python
df1 = DataFrame({'foo': Series(['a', 'b']).astype(cat_dtype), 'left': [1, 2]}).set_index('foo')
```

### Step 3: Assign df2 = DataFrame.set_index(...)

```python
df2 = DataFrame({'foo': Series(['a', 'b', 'c']).astype(cat_dtype), 'right': [3, 2, 1]}).set_index('foo')
```

### Step 4: Assign result = df1.merge(...)

```python
result = df1.merge(df2, left_index=True, right_index=True)
```

### Step 5: Assign expected = DataFrame.set_index(...)

```python
expected = DataFrame({'left': [1, 2], 'right': [3, 2], 'foo': Series(['a', 'b']).astype(cat_dtype)}).set_index('foo')
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
cat_dtype = CategoricalDtype(categories=['a', 'b', 'c'], ordered=False)
df1 = DataFrame({'foo': Series(['a', 'b']).astype(cat_dtype), 'left': [1, 2]}).set_index('foo')
df2 = DataFrame({'foo': Series(['a', 'b', 'c']).astype(cat_dtype), 'right': [3, 2, 1]}).set_index('foo')
result = df1.merge(df2, left_index=True, right_index=True)
expected = DataFrame({'left': [1, 2], 'right': [3, 2], 'foo': Series(['a', 'b']).astype(cat_dtype)}).set_index('foo')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_merge.py:2459 | Complexity: Intermediate | Last updated: 2026-06-02*