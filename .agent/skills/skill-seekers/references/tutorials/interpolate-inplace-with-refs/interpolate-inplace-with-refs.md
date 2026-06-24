# How To: Interpolate Inplace With Refs

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test interpolate inplace with refs

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
# Fixtures: using_copy_on_write, vals, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, np.nan, 2]})
```

**Verification:**
```python
assert not np.shares_memory(arr, get_array(df, 'a'))
```

### Step 2: Assign df_orig = df.copy(...)

```python
df_orig = df.copy()
```

**Verification:**
```python
assert df._mgr._has_no_reference(0)
```

### Step 3: Assign arr = get_array(...)

```python
arr = get_array(df, 'a')
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
assert np.shares_memory(arr, get_array(df, 'a'))
```

### Step 5: Call df.interpolate()

```python
df.interpolate(method='linear', inplace=True)
```

**Verification:**
```python
assert not np.shares_memory(arr, get_array(df, 'a'))
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_orig, view)
```

**Verification:**
```python
assert df._mgr._has_no_reference(0)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, vals, warn_copy_on_write

# Workflow
df = DataFrame({'a': [1, np.nan, 2]})
df_orig = df.copy()
arr = get_array(df, 'a')
view = df[:]
with tm.assert_cow_warning(warn_copy_on_write):
    df.interpolate(method='linear', inplace=True)
if using_copy_on_write:
    assert not np.shares_memory(arr, get_array(df, 'a'))
    tm.assert_frame_equal(df_orig, view)
    assert df._mgr._has_no_reference(0)
    assert view._mgr._has_no_reference(0)
else:
    assert np.shares_memory(arr, get_array(df, 'a'))
```

## Next Steps


---

*Source: test_interp_fillna.py:96 | Complexity: Intermediate | Last updated: 2026-06-02*