# How To: Astype Single Dtype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype single dtype

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pickle`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.pyarrow`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`

**Setup Required:**
```python
# Fixtures: using_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': 1.5})
```

**Verification:**
```python
assert np.shares_memory(get_array(df2, 'c'), get_array(df, 'c'))
```

### Step 2: Assign df_orig = df.copy(...)

```python
df_orig = df.copy()
```

**Verification:**
```python
assert not np.shares_memory(get_array(df2, 'a'), get_array(df, 'a'))
```

### Step 3: Assign df2 = df.astype(...)

```python
df2 = df.astype('float64')
```

**Verification:**
```python
assert not np.shares_memory(get_array(df2, 'c'), get_array(df, 'c'))
```

### Step 4: Assign unknown = 5.5

```python
df2.iloc[0, 2] = 5.5
```

**Verification:**
```python
assert not np.shares_memory(get_array(df2, 'a'), get_array(df, 'a'))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_orig)
```

**Verification:**
```python
assert not np.shares_memory(get_array(df2, 'c'), get_array(df, 'c'))
```

### Step 6: Assign df2 = df.astype(...)

```python
df2 = df.astype('float64')
```

### Step 7: Assign unknown = 5.5

```python
df.iloc[0, 2] = 5.5
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df2, df_orig.astype('float64'))
```

**Verification:**
```python
assert np.shares_memory(get_array(df2, 'c'), get_array(df, 'c'))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': 1.5})
df_orig = df.copy()
df2 = df.astype('float64')
if using_copy_on_write:
    assert np.shares_memory(get_array(df2, 'c'), get_array(df, 'c'))
    assert not np.shares_memory(get_array(df2, 'a'), get_array(df, 'a'))
else:
    assert not np.shares_memory(get_array(df2, 'c'), get_array(df, 'c'))
    assert not np.shares_memory(get_array(df2, 'a'), get_array(df, 'a'))
df2.iloc[0, 2] = 5.5
if using_copy_on_write:
    assert not np.shares_memory(get_array(df2, 'c'), get_array(df, 'c'))
tm.assert_frame_equal(df, df_orig)
df2 = df.astype('float64')
df.iloc[0, 2] = 5.5
tm.assert_frame_equal(df2, df_orig.astype('float64'))
```

## Next Steps


---

*Source: test_astype.py:21 | Complexity: Advanced | Last updated: 2026-06-02*