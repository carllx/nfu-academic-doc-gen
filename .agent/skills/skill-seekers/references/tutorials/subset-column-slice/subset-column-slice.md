# How To: Subset Column Slice

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test subset column slice

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
dtype_backend, DataFrame, _ = backend
```

**Verification:**
```python
assert np.shares_memory(get_array(subset, 'b'), get_array(df, 'b'))
```

### Step 2: Assign single_block = value

```python
single_block = (dtype == 'int64' and dtype_backend == 'numpy') and (not using_array_manager)
```

**Verification:**
```python
assert not np.shares_memory(get_array(subset, 'b'), get_array(df, 'b'))
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': np.array([7, 8, 9], dtype=dtype)})
```

### Step 4: Assign df_orig = df.copy(...)

```python
df_orig = df.copy()
```

### Step 5: Assign subset = value

```python
subset = df.iloc[:, 1:]
```

### Step 6: Call subset._mgr._verify_integrity()

```python
subset._mgr._verify_integrity()
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame({'b': [0, 5, 6], 'c': np.array([7, 8, 9], dtype=dtype)})
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(subset, expected)
```

**Verification:**
```python
assert np.shares_memory(get_array(subset, 'b'), get_array(df, 'b'))
```

### Step 9: Assign unknown = 0

```python
subset.iloc[0, 0] = 0
```

**Verification:**
```python
assert not np.shares_memory(get_array(subset, 'b'), get_array(df, 'b'))
```

### Step 10: Assign unknown = 0

```python
df_orig.iloc[0, 1] = 0
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_orig)
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_orig)
```

### Step 13: Assign warn = value

```python
warn = SettingWithCopyWarning if single_block else None
```

### Step 14: Assign unknown = 0

```python
subset.iloc[0, 0] = 0
```

### Step 15: Assign unknown = 0

```python
subset.iloc[0, 0] = 0
```


## Complete Example

```python
# Setup
# Fixtures: backend, using_copy_on_write, warn_copy_on_write, using_array_manager, dtype

# Workflow
dtype_backend, DataFrame, _ = backend
single_block = (dtype == 'int64' and dtype_backend == 'numpy') and (not using_array_manager)
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': np.array([7, 8, 9], dtype=dtype)})
df_orig = df.copy()
subset = df.iloc[:, 1:]
subset._mgr._verify_integrity()
if using_copy_on_write:
    assert np.shares_memory(get_array(subset, 'b'), get_array(df, 'b'))
    subset.iloc[0, 0] = 0
    assert not np.shares_memory(get_array(subset, 'b'), get_array(df, 'b'))
elif warn_copy_on_write:
    with tm.assert_cow_warning(single_block):
        subset.iloc[0, 0] = 0
else:
    warn = SettingWithCopyWarning if single_block else None
    with pd.option_context('chained_assignment', 'warn'):
        with tm.assert_produces_warning(warn):
            subset.iloc[0, 0] = 0
expected = DataFrame({'b': [0, 5, 6], 'c': np.array([7, 8, 9], dtype=dtype)})
tm.assert_frame_equal(subset, expected)
if not using_copy_on_write and (using_array_manager or single_block):
    df_orig.iloc[0, 1] = 0
    tm.assert_frame_equal(df, df_orig)
else:
    tm.assert_frame_equal(df, df_orig)
```

## Next Steps


---

*Source: test_indexing.py:143 | Complexity: Advanced | Last updated: 2026-06-02*