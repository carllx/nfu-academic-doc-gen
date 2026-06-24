# How To: Replace Regex Inplace Refs

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test replace regex inplace refs

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
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
df = DataFrame({'a': ['aaa', 'bbb']})
```

**Verification:**
```python
assert not tm.shares_memory(arr, get_array(df, 'a'))
```

### Step 2: Assign df_orig = df.copy(...)

```python
df_orig = df.copy()
```

**Verification:**
```python
assert df._mgr._has_no_reference(0)
```

### Step 3: Assign view = value

```python
view = df[:]
```

**Verification:**
```python
assert np.shares_memory(arr, get_array(df, 'a'))
```

### Step 4: Assign arr = get_array(...)

```python
arr = get_array(df, 'a')
```

### Step 5: Call df.replace()

```python
df.replace(to_replace='^a.*$', value='new', inplace=True, regex=True)
```

**Verification:**
```python
assert not tm.shares_memory(arr, get_array(df, 'a'))
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(view, df_orig)
```

**Verification:**
```python
assert np.shares_memory(arr, get_array(df, 'a'))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, warn_copy_on_write

# Workflow
df = DataFrame({'a': ['aaa', 'bbb']})
df_orig = df.copy()
view = df[:]
arr = get_array(df, 'a')
with tm.assert_cow_warning(warn_copy_on_write):
    df.replace(to_replace='^a.*$', value='new', inplace=True, regex=True)
if using_copy_on_write:
    assert not tm.shares_memory(arr, get_array(df, 'a'))
    assert df._mgr._has_no_reference(0)
    tm.assert_frame_equal(view, df_orig)
else:
    assert np.shares_memory(arr, get_array(df, 'a'))
```

## Next Steps


---

*Source: test_replace.py:53 | Complexity: Intermediate | Last updated: 2026-06-02*