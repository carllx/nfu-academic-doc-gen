# How To: Rename Columns

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test rename columns

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`
- `pandas.util.version`

**Setup Required:**
```python
# Fixtures: using_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [0.1, 0.2, 0.3]})
```

**Verification:**
```python
assert np.shares_memory(get_array(df2, 'A'), get_array(df, 'a'))
```

### Step 2: Assign df_orig = df.copy(...)

```python
df_orig = df.copy()
```

**Verification:**
```python
assert not np.shares_memory(get_array(df2, 'A'), get_array(df, 'a'))
```

### Step 3: Assign df2 = df.rename(...)

```python
df2 = df.rename(columns=str.upper)
```

**Verification:**
```python
assert np.shares_memory(get_array(df2, 'C'), get_array(df, 'c'))
```

### Step 4: Assign unknown = 0

```python
df2.iloc[0, 0] = 0
```

**Verification:**
```python
assert not np.shares_memory(get_array(df2, 'A'), get_array(df, 'a'))
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [0, 2, 3], 'B': [4, 5, 6], 'C': [0.1, 0.2, 0.3]})
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df2, expected)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_orig)
```

**Verification:**
```python
assert np.shares_memory(get_array(df2, 'A'), get_array(df, 'a'))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [0.1, 0.2, 0.3]})
df_orig = df.copy()
df2 = df.rename(columns=str.upper)
if using_copy_on_write:
    assert np.shares_memory(get_array(df2, 'A'), get_array(df, 'a'))
df2.iloc[0, 0] = 0
assert not np.shares_memory(get_array(df2, 'A'), get_array(df, 'a'))
if using_copy_on_write:
    assert np.shares_memory(get_array(df2, 'C'), get_array(df, 'c'))
expected = DataFrame({'A': [0, 2, 3], 'B': [4, 5, 6], 'C': [0.1, 0.2, 0.3]})
tm.assert_frame_equal(df2, expected)
tm.assert_frame_equal(df, df_orig)
```

## Next Steps


---

*Source: test_methods.py:299 | Complexity: Intermediate | Last updated: 2026-06-02*