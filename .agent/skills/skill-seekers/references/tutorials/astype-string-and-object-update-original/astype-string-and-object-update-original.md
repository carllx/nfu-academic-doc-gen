# How To: Astype String And Object Update Original

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test astype string and object update original

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
# Fixtures: using_copy_on_write, dtype, new_dtype
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': ['a', 'b', 'c']}, dtype=dtype)
```

**Verification:**
```python
assert np.shares_memory(get_array(df2, 'a'), get_array(df, 'a'))
```

### Step 2: Assign df2 = df.astype(...)

```python
df2 = df.astype(new_dtype)
```

**Verification:**
```python
assert not np.shares_memory(get_array(df2, 'a'), get_array(df, 'a'))
```

### Step 3: Assign df_orig = df2.copy(...)

```python
df_orig = df2.copy()
```

### Step 4: Assign unknown = 'x'

```python
df.iloc[0, 0] = 'x'
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df2, df_orig)
```

**Verification:**
```python
assert np.shares_memory(get_array(df2, 'a'), get_array(df, 'a'))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, dtype, new_dtype

# Workflow
df = DataFrame({'a': ['a', 'b', 'c']}, dtype=dtype)
df2 = df.astype(new_dtype)
df_orig = df2.copy()
if using_copy_on_write:
    assert np.shares_memory(get_array(df2, 'a'), get_array(df, 'a'))
else:
    assert not np.shares_memory(get_array(df2, 'a'), get_array(df, 'a'))
df.iloc[0, 0] = 'x'
tm.assert_frame_equal(df2, df_orig)
```

## Next Steps


---

*Source: test_astype.py:120 | Complexity: Intermediate | Last updated: 2026-06-02*