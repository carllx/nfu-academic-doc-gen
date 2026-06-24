# How To: Astype Dict Dtypes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test astype dict dtypes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pickle`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.compat.pyarrow`
- `pandas.util._test_decorators`
- `pandas`
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
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': Series([1.5, 1.5, 1.5], dtype='float64')})
```

**Verification:**
```python
assert np.shares_memory(get_array(df2, 'c'), get_array(df, 'c'))
```

### Step 2: Assign df_orig = df.copy(...)

```python
df_orig = df.copy()
```

**Verification:**
```python
assert np.shares_memory(get_array(df2, 'b'), get_array(df, 'b'))
```

### Step 3: Assign df2 = df.astype(...)

```python
df2 = df.astype({'a': 'float64', 'c': 'float64'})
```

**Verification:**
```python
assert not np.shares_memory(get_array(df2, 'a'), get_array(df, 'a'))
```

### Step 4: Assign unknown = 5.5

```python
df2.iloc[0, 2] = 5.5
```

**Verification:**
```python
assert not np.shares_memory(get_array(df2, 'c'), get_array(df, 'c'))
```

### Step 5: Assign unknown = 10

```python
df2.iloc[0, 1] = 10
```

**Verification:**
```python
assert not np.shares_memory(get_array(df2, 'b'), get_array(df, 'b'))
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_orig)
```

**Verification:**
```python
assert not np.shares_memory(get_array(df2, 'a'), get_array(df, 'a'))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': Series([1.5, 1.5, 1.5], dtype='float64')})
df_orig = df.copy()
df2 = df.astype({'a': 'float64', 'c': 'float64'})
if using_copy_on_write:
    assert np.shares_memory(get_array(df2, 'c'), get_array(df, 'c'))
    assert np.shares_memory(get_array(df2, 'b'), get_array(df, 'b'))
    assert not np.shares_memory(get_array(df2, 'a'), get_array(df, 'a'))
else:
    assert not np.shares_memory(get_array(df2, 'c'), get_array(df, 'c'))
    assert not np.shares_memory(get_array(df2, 'b'), get_array(df, 'b'))
    assert not np.shares_memory(get_array(df2, 'a'), get_array(df, 'a'))
df2.iloc[0, 2] = 5.5
if using_copy_on_write:
    assert not np.shares_memory(get_array(df2, 'c'), get_array(df, 'c'))
df2.iloc[0, 1] = 10
if using_copy_on_write:
    assert not np.shares_memory(get_array(df2, 'b'), get_array(df, 'b'))
tm.assert_frame_equal(df, df_orig)
```

## Next Steps


---

*Source: test_astype.py:165 | Complexity: Intermediate | Last updated: 2026-06-02*