# How To: Replace

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test replace

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
# Fixtures: using_copy_on_write, replace_kwargs
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [0.1, 0.2, 0.3]})
```

**Verification:**
```python
assert np.shares_memory(get_array(df_replaced, 'b'), get_array(df, 'b'))
```

### Step 2: Assign df_orig = df.copy(...)

```python
df_orig = df.copy()
```

**Verification:**
```python
assert tm.shares_memory(get_array(df_replaced, 'c'), get_array(df, 'c'))
```

### Step 3: Assign df_replaced = df.replace(...)

```python
df_replaced = df.replace(**replace_kwargs)
```

**Verification:**
```python
assert not np.shares_memory(get_array(df_replaced, 'c'), get_array(df, 'c'))
```

### Step 4: Assign unknown = value

```python
df_replaced.loc[0, 'c'] = -1
```

**Verification:**
```python
assert np.shares_memory(get_array(df_replaced, 'a'), arr)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_orig)
```

**Verification:**
```python
assert tm.shares_memory(get_array(df_replaced, 'c'), get_array(df, 'c'))
```

### Step 6: Assign arr = get_array(...)

```python
arr = get_array(df_replaced, 'a')
```

### Step 7: Assign unknown = 100

```python
df_replaced.loc[0, 'a'] = 100
```

**Verification:**
```python
assert np.shares_memory(get_array(df_replaced, 'a'), arr)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, replace_kwargs

# Workflow
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [0.1, 0.2, 0.3]})
df_orig = df.copy()
df_replaced = df.replace(**replace_kwargs)
if using_copy_on_write:
    if (df_replaced['b'] == df['b']).all():
        assert np.shares_memory(get_array(df_replaced, 'b'), get_array(df, 'b'))
    assert tm.shares_memory(get_array(df_replaced, 'c'), get_array(df, 'c'))
df_replaced.loc[0, 'c'] = -1
if using_copy_on_write:
    assert not np.shares_memory(get_array(df_replaced, 'c'), get_array(df, 'c'))
if 'a' in replace_kwargs['to_replace']:
    arr = get_array(df_replaced, 'a')
    df_replaced.loc[0, 'a'] = 100
    assert np.shares_memory(get_array(df_replaced, 'a'), arr)
tm.assert_frame_equal(df, df_orig)
```

## Next Steps


---

*Source: test_replace.py:30 | Complexity: Intermediate | Last updated: 2026-06-02*