# How To: Merge Equal Cat Dtypes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test merge equal cat dtypes

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: cat_dtype, reverse
```

## Step-by-Step Guide

### Step 1: Assign cat_dtypes = value

```python
cat_dtypes = {'one': CategoricalDtype(categories=['a', 'b', 'c'], ordered=False), 'two': CategoricalDtype(categories=['a', 'b', 'c'], ordered=False)}
```

### Step 2: Assign df1 = DataFrame.set_index(...)

```python
df1 = DataFrame({'foo': Series(['a', 'b', 'c']).astype(cat_dtypes['one']), 'left': [1, 2, 3]}).set_index('foo')
```

### Step 3: Assign data_foo = value

```python
data_foo = ['a', 'b', 'c']
```

### Step 4: Assign data_right = value

```python
data_right = [1, 2, 3]
```

### Step 5: Assign df2 = DataFrame.set_index(...)

```python
df2 = DataFrame({'foo': Series(data_foo).astype(cat_dtypes[cat_dtype]), 'right': data_right}).set_index('foo')
```

### Step 6: Assign result = df1.merge(...)

```python
result = df1.merge(df2, left_index=True, right_index=True)
```

### Step 7: Assign expected = DataFrame.set_index(...)

```python
expected = DataFrame({'left': [1, 2, 3], 'right': [1, 2, 3], 'foo': Series(['a', 'b', 'c']).astype(cat_dtypes['one'])}).set_index('foo')
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Call data_foo.reverse()

```python
data_foo.reverse()
```

### Step 10: Call data_right.reverse()

```python
data_right.reverse()
```


## Complete Example

```python
# Setup
# Fixtures: cat_dtype, reverse

# Workflow
cat_dtypes = {'one': CategoricalDtype(categories=['a', 'b', 'c'], ordered=False), 'two': CategoricalDtype(categories=['a', 'b', 'c'], ordered=False)}
df1 = DataFrame({'foo': Series(['a', 'b', 'c']).astype(cat_dtypes['one']), 'left': [1, 2, 3]}).set_index('foo')
data_foo = ['a', 'b', 'c']
data_right = [1, 2, 3]
if reverse:
    data_foo.reverse()
    data_right.reverse()
df2 = DataFrame({'foo': Series(data_foo).astype(cat_dtypes[cat_dtype]), 'right': data_right}).set_index('foo')
result = df1.merge(df2, left_index=True, right_index=True)
expected = DataFrame({'left': [1, 2, 3], 'right': [1, 2, 3], 'foo': Series(['a', 'b', 'c']).astype(cat_dtypes['one'])}).set_index('foo')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_merge.py:2424 | Complexity: Advanced | Last updated: 2026-06-02*