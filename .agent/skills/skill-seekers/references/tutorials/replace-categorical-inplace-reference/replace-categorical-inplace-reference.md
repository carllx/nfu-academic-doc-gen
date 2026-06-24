# How To: Replace Categorical Inplace Reference

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test replace categorical inplace reference

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
# Fixtures: using_copy_on_write, val, to_replace
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': Categorical([1, 2, 3])})
```

**Verification:**
```python
assert not np.shares_memory(get_array(df, 'a').codes, arr_a.codes)
```

### Step 2: Assign df_orig = df.copy(...)

```python
df_orig = df.copy()
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
assert np.shares_memory(get_array(df, 'a').codes, arr_a.codes)
```

### Step 5: Assign msg = 'The behavior of Series\\.replace \\(and DataFrame.replace\\) with CategoricalDtype'

```python
msg = 'The behavior of Series\\.replace \\(and DataFrame.replace\\) with CategoricalDtype'
```

### Step 6: Assign warn = value

```python
warn = FutureWarning if val == 1.5 else None
```

### Step 7: Call df.replace()

```python
df.replace(to_replace=to_replace, value=val, inplace=True)
```

**Verification:**
```python
assert not np.shares_memory(get_array(df, 'a').codes, arr_a.codes)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(view, df_orig)
```

**Verification:**
```python
assert np.shares_memory(get_array(df, 'a').codes, arr_a.codes)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, val, to_replace

# Workflow
df = DataFrame({'a': Categorical([1, 2, 3])})
df_orig = df.copy()
arr_a = get_array(df, 'a')
view = df[:]
msg = 'The behavior of Series\\.replace \\(and DataFrame.replace\\) with CategoricalDtype'
warn = FutureWarning if val == 1.5 else None
with tm.assert_produces_warning(warn, match=msg):
    df.replace(to_replace=to_replace, value=val, inplace=True)
if using_copy_on_write:
    assert not np.shares_memory(get_array(df, 'a').codes, arr_a.codes)
    assert df._mgr._has_no_reference(0)
    assert view._mgr._has_no_reference(0)
    tm.assert_frame_equal(view, df_orig)
else:
    assert np.shares_memory(get_array(df, 'a').codes, arr_a.codes)
```

## Next Steps


---

*Source: test_replace.py:249 | Complexity: Advanced | Last updated: 2026-06-02*