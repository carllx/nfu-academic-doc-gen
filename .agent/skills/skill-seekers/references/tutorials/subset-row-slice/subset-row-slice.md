# How To: Subset Row Slice

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test subset row slice

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
_, DataFrame, _ = backend
```

**Verification:**
```python
assert np.shares_memory(get_array(subset, 'a'), get_array(df, 'a'))
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [0.1, 0.2, 0.3]})
```

**Verification:**
```python
assert not np.shares_memory(get_array(subset, 'a'), get_array(df, 'a'))
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

**Verification:**
```python
assert np.shares_memory(get_array(subset, 'a'), get_array(df, 'a'))
```

### Step 6: Call subset._mgr._verify_integrity()

```python
subset._mgr._verify_integrity()
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [0, 3], 'b': [5, 6], 'c': [0.2, 0.3]}, index=range(1, 3))
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(subset, expected)
```

### Step 9: Assign unknown = 0

```python
subset.iloc[0, 0] = 0
```

**Verification:**
```python
assert not np.shares_memory(get_array(subset, 'a'), get_array(df, 'a'))
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_orig)
```

### Step 11: Assign unknown = 0

```python
df_orig.iloc[1, 0] = 0
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_orig)
```

### Step 13: Assign unknown = 0

```python
subset.iloc[0, 0] = 0
```


## Complete Example

```python
# Setup
# Fixtures: backend, using_copy_on_write, warn_copy_on_write

# Workflow
_, DataFrame, _ = backend
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [0.1, 0.2, 0.3]})
df_orig = df.copy()
subset = df[1:3]
subset._mgr._verify_integrity()
assert np.shares_memory(get_array(subset, 'a'), get_array(df, 'a'))
if using_copy_on_write:
    subset.iloc[0, 0] = 0
    assert not np.shares_memory(get_array(subset, 'a'), get_array(df, 'a'))
else:
    with tm.assert_cow_warning(warn_copy_on_write):
        subset.iloc[0, 0] = 0
subset._mgr._verify_integrity()
expected = DataFrame({'a': [0, 3], 'b': [5, 6], 'c': [0.2, 0.3]}, index=range(1, 3))
tm.assert_frame_equal(subset, expected)
if using_copy_on_write:
    tm.assert_frame_equal(df, df_orig)
else:
    df_orig.iloc[1, 0] = 0
    tm.assert_frame_equal(df, df_orig)
```

## Next Steps


---

*Source: test_indexing.py:104 | Complexity: Advanced | Last updated: 2026-06-02*