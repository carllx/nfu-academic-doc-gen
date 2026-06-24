# How To: Replace List Categorical

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test replace list categorical

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
# Fixtures: using_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': ['a', 'b', 'c']}, dtype='category')
```

**Verification:**
```python
assert np.shares_memory(arr.codes, get_array(df, 'a').codes)
```

### Step 2: Assign arr = get_array(...)

```python
arr = get_array(df, 'a')
```

**Verification:**
```python
assert df._mgr._has_no_reference(0)
```

### Step 3: Assign msg = 'The behavior of Series\\.replace \\(and DataFrame.replace\\) with CategoricalDtype'

```python
msg = 'The behavior of Series\\.replace \\(and DataFrame.replace\\) with CategoricalDtype'
```

**Verification:**
```python
assert not np.shares_memory(arr.codes, get_array(df2, 'a').codes)
```

### Step 4: Assign df_orig = df.copy(...)

```python
df_orig = df.copy()
```

**Verification:**
```python
assert not np.shares_memory(arr.codes, get_array(df2, 'a').codes)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_orig)
```

### Step 6: Call df.replace()

```python
df.replace(['c'], value='a', inplace=True)
```

**Verification:**
```python
assert df._mgr._has_no_reference(0)
```

### Step 7: Assign df2 = df.replace(...)

```python
df2 = df.replace(['b'], value='a')
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
df = DataFrame({'a': ['a', 'b', 'c']}, dtype='category')
arr = get_array(df, 'a')
msg = 'The behavior of Series\\.replace \\(and DataFrame.replace\\) with CategoricalDtype'
with tm.assert_produces_warning(FutureWarning, match=msg):
    df.replace(['c'], value='a', inplace=True)
assert np.shares_memory(arr.codes, get_array(df, 'a').codes)
if using_copy_on_write:
    assert df._mgr._has_no_reference(0)
df_orig = df.copy()
with tm.assert_produces_warning(FutureWarning, match=msg):
    df2 = df.replace(['b'], value='a')
assert not np.shares_memory(arr.codes, get_array(df2, 'a').codes)
tm.assert_frame_equal(df, df_orig)
```

## Next Steps


---

*Source: test_replace.py:164 | Complexity: Intermediate | Last updated: 2026-06-02*