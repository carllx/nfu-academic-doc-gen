# How To: Clip Inplace Reference

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test clip inplace reference

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`

**Setup Required:**
```python
# Fixtures: using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1.5, 2, 3]})
```

**Verification:**
```python
assert not np.shares_memory(get_array(df, 'a'), arr_a)
```

### Step 2: Assign df_copy = df.copy(...)

```python
df_copy = df.copy()
```

**Verification:**
```python
assert df._mgr._has_no_reference(0)
```

### Step 3: Assign arr_a = get_array(...)

```python
arr_a = get_array(df, 'a')
```

**Verification:**
```python
assert view._mgr._has_no_reference(0)
```

### Step 4: Assign view = value

```python
view = df[:]
```

**Verification:**
```python
assert np.shares_memory(get_array(df, 'a'), arr_a)
```

### Step 5: Call df.clip()

```python
df.clip(lower=2, inplace=True)
```

**Verification:**
```python
assert not np.shares_memory(get_array(df, 'a'), arr_a)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_copy, view)
```

**Verification:**
```python
assert np.shares_memory(get_array(df, 'a'), arr_a)
```

### Step 7: Call df.clip()

```python
df.clip(lower=2, inplace=True)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, warn_copy_on_write

# Workflow
df = DataFrame({'a': [1.5, 2, 3]})
df_copy = df.copy()
arr_a = get_array(df, 'a')
view = df[:]
if warn_copy_on_write:
    with tm.assert_cow_warning():
        df.clip(lower=2, inplace=True)
else:
    df.clip(lower=2, inplace=True)
if using_copy_on_write:
    assert not np.shares_memory(get_array(df, 'a'), arr_a)
    assert df._mgr._has_no_reference(0)
    assert view._mgr._has_no_reference(0)
    tm.assert_frame_equal(df_copy, view)
else:
    assert np.shares_memory(get_array(df, 'a'), arr_a)
```

## Next Steps


---

*Source: test_clip.py:13 | Complexity: Intermediate | Last updated: 2026-06-02*