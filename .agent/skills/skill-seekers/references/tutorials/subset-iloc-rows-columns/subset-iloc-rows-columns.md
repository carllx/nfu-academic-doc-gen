# How To: Subset Iloc Rows Columns

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test subset iloc rows columns

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`

**Setup Required:**
```python
# Fixtures: backend, dtype, row_indexer, column_indexer, using_array_manager, using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign unknown = backend

```python
dtype_backend, DataFrame, _ = backend
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': np.array([7, 8, 9], dtype=dtype)})
```

### Step 3: Assign df_orig = df.copy(...)

```python
df_orig = df.copy()
```

### Step 4: Assign subset = value

```python
subset = df.iloc[row_indexer, column_indexer]
```

### Step 5: Assign mutate_parent = value

```python
mutate_parent = isinstance(row_indexer, slice) and isinstance(column_indexer, slice) and (using_array_manager or (dtype == 'int64' and dtype_backend == 'numpy' and (not using_copy_on_write)))
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame({'b': [0, 6], 'c': np.array([8, 9], dtype=dtype)}, index=range(1, 3))
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(subset, expected)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_orig)
```

### Step 9: Assign unknown = 0

```python
subset.iloc[0, 0] = 0
```

### Step 10: Assign unknown = 0

```python
df_orig.iloc[1, 1] = 0
```


## Complete Example

```python
# Setup
# Fixtures: backend, dtype, row_indexer, column_indexer, using_array_manager, using_copy_on_write, warn_copy_on_write

# Workflow
dtype_backend, DataFrame, _ = backend
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': np.array([7, 8, 9], dtype=dtype)})
df_orig = df.copy()
subset = df.iloc[row_indexer, column_indexer]
mutate_parent = isinstance(row_indexer, slice) and isinstance(column_indexer, slice) and (using_array_manager or (dtype == 'int64' and dtype_backend == 'numpy' and (not using_copy_on_write)))
with tm.assert_cow_warning(warn_copy_on_write and mutate_parent):
    subset.iloc[0, 0] = 0
expected = DataFrame({'b': [0, 6], 'c': np.array([8, 9], dtype=dtype)}, index=range(1, 3))
tm.assert_frame_equal(subset, expected)
if mutate_parent:
    df_orig.iloc[1, 1] = 0
tm.assert_frame_equal(df, df_orig)
```

## Next Steps


---

*Source: test_indexing.py:263 | Complexity: Advanced | Last updated: 2026-06-02*