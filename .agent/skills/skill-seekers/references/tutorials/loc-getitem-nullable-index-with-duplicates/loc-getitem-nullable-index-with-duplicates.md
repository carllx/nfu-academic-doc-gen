# How To: Loc Getitem Nullable Index With Duplicates

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loc getitem nullable index with duplicates

## Prerequisites

**Required Modules:**
- `collections`
- `contextlib`
- `datetime`
- `re`
- `dateutil.tz`
- `numpy`
- `pytest`
- `pandas._config`
- `pandas._libs`
- `pandas.compat.numpy`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.core.indexing`
- `pandas.tests.indexing.common`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame(data=np.array([[1, 2, 3, 4], [5, 6, 7, 8], [1, 2, np.nan, np.nan]]).T, columns=['a', 'b', 'c'], dtype='Int64')
```

**Verification:**
```python
assert df2.index.dtype == 'Int64'
```

### Step 2: Assign df2 = df.set_index(...)

```python
df2 = df.set_index('c')
```

**Verification:**
```python
assert df2.index.dtype == 'Int64'
```

### Step 3: Assign res = value

```python
res = df2.loc[1]
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([1, 5], index=df2.columns, dtype='Int64', name=1)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```

### Step 6: Assign df2.index = df2.index.astype(...)

```python
df2.index = df2.index.astype(object)
```

### Step 7: Assign res = value

```python
res = df2.loc[1]
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame(data=np.array([[1, 2, 3, 4], [5, 6, 7, 8], [1, 2, np.nan, np.nan]]).T, columns=['a', 'b', 'c'], dtype='Int64')
df2 = df.set_index('c')
assert df2.index.dtype == 'Int64'
res = df2.loc[1]
expected = Series([1, 5], index=df2.columns, dtype='Int64', name=1)
tm.assert_series_equal(res, expected)
df2.index = df2.index.astype(object)
res = df2.loc[1]
tm.assert_series_equal(res, expected)
```

## Next Steps


---

*Source: test_loc.py:3038 | Complexity: Advanced | Last updated: 2026-06-02*