# How To: Astype Different Target Dtype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test astype different target dtype

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
# Fixtures: using_copy_on_write, dtype
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3]})
```

**Verification:**
```python
assert not np.shares_memory(get_array(df2, 'a'), get_array(df, 'a'))
```

### Step 2: Assign df_orig = df.copy(...)

```python
df_orig = df.copy()
```

**Verification:**
```python
assert df2._mgr._has_no_reference(0)
```

### Step 3: Assign df2 = df.astype(...)

```python
df2 = df.astype(dtype)
```

**Verification:**
```python
assert not np.shares_memory(get_array(df2, 'a'), get_array(df, 'a'))
```

### Step 4: Assign unknown = 5

```python
df2.iloc[0, 0] = 5
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_orig)
```

### Step 6: Assign df2 = df.astype(...)

```python
df2 = df.astype(dtype)
```

### Step 7: Assign unknown = 100

```python
df.iloc[0, 0] = 100
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df2, df_orig.astype(dtype))
```

### Step 9: Call pytest.importorskip()

```python
pytest.importorskip('pyarrow')
```

**Verification:**
```python
assert df2._mgr._has_no_reference(0)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, dtype

# Workflow
if dtype == 'int32[pyarrow]':
    pytest.importorskip('pyarrow')
df = DataFrame({'a': [1, 2, 3]})
df_orig = df.copy()
df2 = df.astype(dtype)
assert not np.shares_memory(get_array(df2, 'a'), get_array(df, 'a'))
if using_copy_on_write:
    assert df2._mgr._has_no_reference(0)
df2.iloc[0, 0] = 5
tm.assert_frame_equal(df, df_orig)
df2 = df.astype(dtype)
df.iloc[0, 0] = 100
tm.assert_frame_equal(df2, df_orig.astype(dtype))
```

## Next Steps


---

*Source: test_astype.py:72 | Complexity: Advanced | Last updated: 2026-06-02*