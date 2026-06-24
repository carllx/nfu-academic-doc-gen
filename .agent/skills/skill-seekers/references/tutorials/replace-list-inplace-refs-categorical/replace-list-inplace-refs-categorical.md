# How To: Replace List Inplace Refs Categorical

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test replace list inplace refs categorical

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
assert not np.shares_memory(get_array(view, 'a').codes, get_array(df, 'a').codes)
```

### Step 2: Assign view = value

```python
view = df[:]
```

**Verification:**
```python
assert not np.shares_memory(get_array(view, 'a').codes, get_array(df, 'a').codes)
```

### Step 3: Assign df_orig = df.copy(...)

```python
df_orig = df.copy()
```

### Step 4: Assign msg = 'The behavior of Series\\.replace \\(and DataFrame.replace\\) with CategoricalDtype'

```python
msg = 'The behavior of Series\\.replace \\(and DataFrame.replace\\) with CategoricalDtype'
```

### Step 5: Call df.replace()

```python
df.replace(['c'], value='a', inplace=True)
```

**Verification:**
```python
assert not np.shares_memory(get_array(view, 'a').codes, get_array(df, 'a').codes)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_orig, view)
```

**Verification:**
```python
assert not np.shares_memory(get_array(view, 'a').codes, get_array(df, 'a').codes)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
df = DataFrame({'a': ['a', 'b', 'c']}, dtype='category')
view = df[:]
df_orig = df.copy()
msg = 'The behavior of Series\\.replace \\(and DataFrame.replace\\) with CategoricalDtype'
with tm.assert_produces_warning(FutureWarning, match=msg):
    df.replace(['c'], value='a', inplace=True)
if using_copy_on_write:
    assert not np.shares_memory(get_array(view, 'a').codes, get_array(df, 'a').codes)
    tm.assert_frame_equal(df_orig, view)
else:
    assert not np.shares_memory(get_array(view, 'a').codes, get_array(df, 'a').codes)
```

## Next Steps


---

*Source: test_replace.py:185 | Complexity: Intermediate | Last updated: 2026-06-02*