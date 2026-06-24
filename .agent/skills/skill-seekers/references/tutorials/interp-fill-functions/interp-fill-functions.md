# How To: Interp Fill Functions

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test interp fill functions

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
# Fixtures: using_copy_on_write, func
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2]})
```

**Verification:**
```python
assert np.shares_memory(get_array(result, 'a'), get_array(df, 'a'))
```

### Step 2: Assign df_orig = df.copy(...)

```python
df_orig = df.copy()
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'a'), get_array(df, 'a'))
```

### Step 3: Assign result = getattr(...)

```python
result = getattr(df, func)()
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'a'), get_array(df, 'a'))
```

### Step 4: Assign unknown = 100

```python
result.iloc[0, 0] = 100
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_orig)
```

**Verification:**
```python
assert np.shares_memory(get_array(result, 'a'), get_array(df, 'a'))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, func

# Workflow
df = DataFrame({'a': [1, 2]})
df_orig = df.copy()
result = getattr(df, func)()
if using_copy_on_write:
    assert np.shares_memory(get_array(result, 'a'), get_array(df, 'a'))
else:
    assert not np.shares_memory(get_array(result, 'a'), get_array(df, 'a'))
result.iloc[0, 0] = 100
if using_copy_on_write:
    assert not np.shares_memory(get_array(result, 'a'), get_array(df, 'a'))
tm.assert_frame_equal(df, df_orig)
```

## Next Steps


---

*Source: test_interp_fillna.py:46 | Complexity: Intermediate | Last updated: 2026-06-02*