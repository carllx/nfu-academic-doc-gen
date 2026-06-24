# How To: Dataframe Values

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dataframe values

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat.numpy`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`

**Setup Required:**
```python
# Fixtures: using_copy_on_write, using_array_manager, method
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
```

**Verification:**
```python
assert np.shares_memory(arr, get_array(df, 'a'))
```

### Step 2: Assign df_orig = df.copy(...)

```python
df_orig = df.copy()
```

**Verification:**
```python
assert arr.flags.writeable is False
```

### Step 3: Assign arr = method(...)

```python
arr = method(df)
```

**Verification:**
```python
assert df.values[0, 0] == 0
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_orig)
```

**Verification:**
```python
assert arr.flags.writeable is True
```

### Step 5: Assign unknown = 0

```python
df.iloc[0, 0] = 0
```

**Verification:**
```python
assert df.iloc[0, 0] == 0
```

### Step 6: Assign unknown = 0

```python
arr[0, 0] = 0
```

### Step 7: Assign unknown = 0

```python
arr[0, 0] = 0
```

**Verification:**
```python
assert df.iloc[0, 0] == 0
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_orig)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, using_array_manager, method

# Workflow
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
df_orig = df.copy()
arr = method(df)
if using_copy_on_write:
    assert np.shares_memory(arr, get_array(df, 'a'))
    assert arr.flags.writeable is False
    with pytest.raises(ValueError, match='read-only'):
        arr[0, 0] = 0
    tm.assert_frame_equal(df, df_orig)
    df.iloc[0, 0] = 0
    assert df.values[0, 0] == 0
else:
    assert arr.flags.writeable is True
    arr[0, 0] = 0
    if not using_array_manager:
        assert df.iloc[0, 0] == 0
    else:
        tm.assert_frame_equal(df, df_orig)
```

## Next Steps


---

*Source: test_array.py:61 | Complexity: Advanced | Last updated: 2026-06-02*