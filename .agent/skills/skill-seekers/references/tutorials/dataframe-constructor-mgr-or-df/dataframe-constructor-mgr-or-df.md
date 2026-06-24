# How To: Dataframe Constructor Mgr Or Df

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dataframe constructor mgr or df

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`

**Setup Required:**
```python
# Fixtures: using_copy_on_write, warn_copy_on_write, columns, use_mgr
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3]})
```

**Verification:**
```python
assert np.shares_memory(get_array(df, 'a'), get_array(new_df, 'a'))
```

### Step 2: Assign df_orig = df.copy(...)

```python
df_orig = df.copy()
```

**Verification:**
```python
assert not np.shares_memory(get_array(df, 'a'), get_array(new_df, 'a'))
```

### Step 3: Assign msg = 'Passing a BlockManager to DataFrame'

```python
msg = 'Passing a BlockManager to DataFrame'
```

**Verification:**
```python
assert np.shares_memory(get_array(df, 'a'), get_array(new_df, 'a'))
```

### Step 4: Assign data = value

```python
data = df._mgr
```

### Step 5: Assign warn = DeprecationWarning

```python
warn = DeprecationWarning
```

### Step 6: Assign data = df

```python
data = df
```

### Step 7: Assign warn = None

```python
warn = None
```

### Step 8: Assign new_df = DataFrame(...)

```python
new_df = DataFrame(data)
```

### Step 9: Assign unknown = 100

```python
new_df.iloc[0] = 100
```

**Verification:**
```python
assert not np.shares_memory(get_array(df, 'a'), get_array(new_df, 'a'))
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_orig)
```

**Verification:**
```python
assert np.shares_memory(get_array(df, 'a'), get_array(new_df, 'a'))
```

### Step 11: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, new_df)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, warn_copy_on_write, columns, use_mgr

# Workflow
df = DataFrame({'a': [1, 2, 3]})
df_orig = df.copy()
if use_mgr:
    data = df._mgr
    warn = DeprecationWarning
else:
    data = df
    warn = None
msg = 'Passing a BlockManager to DataFrame'
with tm.assert_produces_warning(warn, match=msg, check_stacklevel=False):
    new_df = DataFrame(data)
assert np.shares_memory(get_array(df, 'a'), get_array(new_df, 'a'))
with tm.assert_cow_warning(warn_copy_on_write and (not use_mgr)):
    new_df.iloc[0] = 100
if using_copy_on_write:
    assert not np.shares_memory(get_array(df, 'a'), get_array(new_df, 'a'))
    tm.assert_frame_equal(df, df_orig)
else:
    assert np.shares_memory(get_array(df, 'a'), get_array(new_df, 'a'))
    tm.assert_frame_equal(df, new_df)
```

## Next Steps


---

*Source: test_constructors.py:193 | Complexity: Advanced | Last updated: 2026-06-02*