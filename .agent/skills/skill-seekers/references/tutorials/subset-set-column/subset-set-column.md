# How To: Subset Set Column

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test subset set column

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
# Fixtures: backend, using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign unknown = backend

```python
dtype_backend, DataFrame, _ = backend
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [0.1, 0.2, 0.3]})
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
expected = DataFrame({'a': [10, 11], 'b': [5, 6], 'c': [0.2, 0.3]}, index=range(1, 3))
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(subset, expected)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_orig)
```

### Step 9: Assign arr = np.array(...)

```python
arr = np.array([10, 11], dtype='int64')
```

### Step 10: Assign arr = pd.array(...)

```python
arr = pd.array([10, 11], dtype='Int64')
```

### Step 11: Assign unknown = arr

```python
subset['a'] = arr
```

### Step 12: Assign unknown = arr

```python
subset['a'] = arr
```


## Complete Example

```python
# Setup
# Fixtures: backend, using_copy_on_write, warn_copy_on_write

# Workflow
dtype_backend, DataFrame, _ = backend
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [0.1, 0.2, 0.3]})
df_orig = df.copy()
subset = df[1:3]
if dtype_backend == 'numpy':
    arr = np.array([10, 11], dtype='int64')
else:
    arr = pd.array([10, 11], dtype='Int64')
if using_copy_on_write or warn_copy_on_write:
    subset['a'] = arr
else:
    with pd.option_context('chained_assignment', 'warn'):
        with tm.assert_produces_warning(SettingWithCopyWarning):
            subset['a'] = arr
subset._mgr._verify_integrity()
expected = DataFrame({'a': [10, 11], 'b': [5, 6], 'c': [0.2, 0.3]}, index=range(1, 3))
tm.assert_frame_equal(subset, expected)
tm.assert_frame_equal(df, df_orig)
```

## Next Steps


---

*Source: test_indexing.py:394 | Complexity: Advanced | Last updated: 2026-06-02*