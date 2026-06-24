# How To: Reset Index

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reset index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`
- `pandas.util.version`

**Setup Required:**
```python
# Fixtures: using_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [0.1, 0.2, 0.3]}, index=[10, 11, 12])
```

**Verification:**
```python
assert np.shares_memory(get_array(df2, 'b'), get_array(df, 'b'))
```

### Step 2: Assign df_orig = df.copy(...)

```python
df_orig = df.copy()
```

**Verification:**
```python
assert np.shares_memory(get_array(df2, 'c'), get_array(df, 'c'))
```

### Step 3: Assign df2 = df.reset_index(...)

```python
df2 = df.reset_index()
```

**Verification:**
```python
assert not np.shares_memory(get_array(df2, 'b'), get_array(df, 'b'))
```

### Step 4: Call df2._mgr._verify_integrity()

```python
df2._mgr._verify_integrity()
```

**Verification:**
```python
assert np.shares_memory(get_array(df2, 'c'), get_array(df, 'c'))
```

### Step 5: Assign unknown = 0

```python
df2.iloc[0, 2] = 0
```

**Verification:**
```python
assert not np.shares_memory(get_array(df2, 'b'), get_array(df, 'b'))
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_orig)
```

**Verification:**
```python
assert np.shares_memory(get_array(df2, 'b'), get_array(df, 'b'))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [0.1, 0.2, 0.3]}, index=[10, 11, 12])
df_orig = df.copy()
df2 = df.reset_index()
df2._mgr._verify_integrity()
if using_copy_on_write:
    assert np.shares_memory(get_array(df2, 'b'), get_array(df, 'b'))
    assert np.shares_memory(get_array(df2, 'c'), get_array(df, 'c'))
df2.iloc[0, 2] = 0
assert not np.shares_memory(get_array(df2, 'b'), get_array(df, 'b'))
if using_copy_on_write:
    assert np.shares_memory(get_array(df2, 'c'), get_array(df, 'c'))
tm.assert_frame_equal(df, df_orig)
```

## Next Steps


---

*Source: test_methods.py:251 | Complexity: Intermediate | Last updated: 2026-06-02*