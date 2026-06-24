# How To: Replace Coerce Single Column

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test replace coerce single column

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
# Fixtures: using_copy_on_write, using_array_manager
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1.5, 2, 3], 'b': 100.5})
```

**Verification:**
```python
assert np.shares_memory(get_array(df, 'b'), get_array(df2, 'b'))
```

### Step 2: Assign df_orig = df.copy(...)

```python
df_orig = df.copy()
```

**Verification:**
```python
assert not np.shares_memory(get_array(df, 'a'), get_array(df2, 'a'))
```

### Step 3: Assign df2 = df.replace(...)

```python
df2 = df.replace(to_replace=1.5, value='a')
```

**Verification:**
```python
assert np.shares_memory(get_array(df, 'b'), get_array(df2, 'b'))
```

### Step 4: Assign unknown = 0.5

```python
df2.loc[0, 'b'] = 0.5
```

**Verification:**
```python
assert not np.shares_memory(get_array(df, 'a'), get_array(df2, 'a'))
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_orig)
```

**Verification:**
```python
assert not np.shares_memory(get_array(df, 'b'), get_array(df2, 'b'))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, using_array_manager

# Workflow
df = DataFrame({'a': [1.5, 2, 3], 'b': 100.5})
df_orig = df.copy()
df2 = df.replace(to_replace=1.5, value='a')
if using_copy_on_write:
    assert np.shares_memory(get_array(df, 'b'), get_array(df2, 'b'))
    assert not np.shares_memory(get_array(df, 'a'), get_array(df2, 'a'))
elif not using_array_manager:
    assert np.shares_memory(get_array(df, 'b'), get_array(df2, 'b'))
    assert not np.shares_memory(get_array(df, 'a'), get_array(df2, 'a'))
if using_copy_on_write:
    df2.loc[0, 'b'] = 0.5
    tm.assert_frame_equal(df, df_orig)
    assert not np.shares_memory(get_array(df, 'b'), get_array(df2, 'b'))
```

## Next Steps


---

*Source: test_replace.py:123 | Complexity: Intermediate | Last updated: 2026-06-02*