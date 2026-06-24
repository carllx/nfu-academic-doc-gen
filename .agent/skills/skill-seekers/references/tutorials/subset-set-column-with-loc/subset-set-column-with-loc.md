# How To: Subset Set Column With Loc

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test subset set column with loc

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
# Fixtures: backend, using_copy_on_write, warn_copy_on_write, using_array_manager, dtype
```

## Step-by-Step Guide

### Step 1: Assign unknown = backend

```python
_, DataFrame, _ = backend
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
subset = df[1:3]
```

### Step 5: Call subset._mgr._verify_integrity()

```python
subset._mgr._verify_integrity()
```

### Step 6: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [10, 11], 'b': [5, 6], 'c': np.array([8, 9], dtype=dtype)}, index=range(1, 3))
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(subset, expected)
```

### Step 8: Assign unknown = np.array(...)

```python
subset.loc[:, 'a'] = np.array([10, 11], dtype='int64')
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_orig)
```

### Step 10: Assign unknown = np.array(...)

```python
df_orig.loc[1:3, 'a'] = np.array([10, 11], dtype='int64')
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_orig)
```

### Step 12: Assign unknown = np.array(...)

```python
subset.loc[:, 'a'] = np.array([10, 11], dtype='int64')
```

### Step 13: Assign unknown = np.array(...)

```python
subset.loc[:, 'a'] = np.array([10, 11], dtype='int64')
```


## Complete Example

```python
# Setup
# Fixtures: backend, using_copy_on_write, warn_copy_on_write, using_array_manager, dtype

# Workflow
_, DataFrame, _ = backend
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': np.array([7, 8, 9], dtype=dtype)})
df_orig = df.copy()
subset = df[1:3]
if using_copy_on_write:
    subset.loc[:, 'a'] = np.array([10, 11], dtype='int64')
elif warn_copy_on_write:
    with tm.assert_cow_warning():
        subset.loc[:, 'a'] = np.array([10, 11], dtype='int64')
else:
    with pd.option_context('chained_assignment', 'warn'):
        with tm.assert_produces_warning(None, raise_on_extra_warnings=not using_array_manager):
            subset.loc[:, 'a'] = np.array([10, 11], dtype='int64')
subset._mgr._verify_integrity()
expected = DataFrame({'a': [10, 11], 'b': [5, 6], 'c': np.array([8, 9], dtype=dtype)}, index=range(1, 3))
tm.assert_frame_equal(subset, expected)
if using_copy_on_write:
    tm.assert_frame_equal(df, df_orig)
else:
    df_orig.loc[1:3, 'a'] = np.array([10, 11], dtype='int64')
    tm.assert_frame_equal(df, df_orig)
```

## Next Steps


---

*Source: test_indexing.py:424 | Complexity: Advanced | Last updated: 2026-06-02*