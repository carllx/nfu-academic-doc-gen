# How To: Astype Avoids Copy

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test astype avoids copy

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
# Fixtures: using_copy_on_write, dtype, new_dtype
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3]}, dtype=dtype)
```

**Verification:**
```python
assert np.shares_memory(get_array(df2, 'a'), get_array(df, 'a'))
```

### Step 2: Assign df_orig = df.copy(...)

```python
df_orig = df.copy()
```

**Verification:**
```python
assert not np.shares_memory(get_array(df2, 'a'), get_array(df, 'a'))
```

### Step 3: Assign df2 = df.astype(...)

```python
df2 = df.astype(new_dtype)
```

**Verification:**
```python
assert not np.shares_memory(get_array(df2, 'a'), get_array(df, 'a'))
```

### Step 4: Assign unknown = 10

```python
df2.iloc[0, 0] = 10
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_orig)
```

### Step 6: Assign df2 = df.astype(...)

```python
df2 = df.astype(new_dtype)
```

### Step 7: Assign unknown = 100

```python
df.iloc[0, 0] = 100
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df2, df_orig.astype(new_dtype))
```

### Step 9: Call pytest.importorskip()

```python
pytest.importorskip('pyarrow')
```

**Verification:**
```python
assert np.shares_memory(get_array(df2, 'a'), get_array(df, 'a'))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, dtype, new_dtype

# Workflow
if new_dtype == 'int64[pyarrow]':
    pytest.importorskip('pyarrow')
df = DataFrame({'a': [1, 2, 3]}, dtype=dtype)
df_orig = df.copy()
df2 = df.astype(new_dtype)
if using_copy_on_write:
    assert np.shares_memory(get_array(df2, 'a'), get_array(df, 'a'))
else:
    assert not np.shares_memory(get_array(df2, 'a'), get_array(df, 'a'))
df2.iloc[0, 0] = 10
if using_copy_on_write:
    assert not np.shares_memory(get_array(df2, 'a'), get_array(df, 'a'))
tm.assert_frame_equal(df, df_orig)
df2 = df.astype(new_dtype)
df.iloc[0, 0] = 100
tm.assert_frame_equal(df2, df_orig.astype(new_dtype))
```

## Next Steps


---

*Source: test_astype.py:47 | Complexity: Advanced | Last updated: 2026-06-02*