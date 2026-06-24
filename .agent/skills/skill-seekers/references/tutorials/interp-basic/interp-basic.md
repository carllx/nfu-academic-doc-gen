# How To: Interp Basic

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test interp basic

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._config`
- `pandas.compat`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: using_copy_on_write, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'A': [1, 2, np.nan, 4], 'B': [1, 4, 9, np.nan], 'C': [1, 2, 3, 5], 'D': list('abcd')})
```

**Verification:**
```python
assert np.shares_memory(cvalues, result['C']._values)
```

### Step 2: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [1.0, 2.0, 3.0, 4.0], 'B': [1.0, 4.0, 9.0, 9.0], 'C': [1, 2, 3, 5], 'D': list('abcd')})
```

**Verification:**
```python
assert np.shares_memory(dvalues, result['D']._values)
```

### Step 3: Assign msg = 'DataFrame.interpolate with object dtype'

```python
msg = 'DataFrame.interpolate with object dtype'
```

**Verification:**
```python
assert not np.shares_memory(cvalues, result['C']._values)
```

### Step 4: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

**Verification:**
```python
assert not np.shares_memory(dvalues, result['D']._values)
```

### Step 5: Assign cvalues = value

```python
cvalues = df['C']._values
```

**Verification:**
```python
assert res is None
```

### Step 6: Assign dvalues = value

```python
dvalues = df['D'].values
```

**Verification:**
```python
assert tm.shares_memory(df['C']._values, cvalues)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, expected)
```

**Verification:**
```python
assert tm.shares_memory(df['D']._values, dvalues)
```

### Step 8: Assign dtype = value

```python
dtype = 'str' if using_infer_string else 'object'
```

### Step 9: Assign msg = value

```python
msg = f'[Cc]annot interpolate with {dtype} dtype'
```

### Step 10: Assign result = df.interpolate(...)

```python
result = df.interpolate()
```

**Verification:**
```python
assert np.shares_memory(cvalues, result['C']._values)
```

### Step 11: Assign res = df.interpolate(...)

```python
res = df.interpolate(inplace=True)
```

### Step 12: Call df.interpolate()

```python
df.interpolate()
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, using_infer_string

# Workflow
df = DataFrame({'A': [1, 2, np.nan, 4], 'B': [1, 4, 9, np.nan], 'C': [1, 2, 3, 5], 'D': list('abcd')})
expected = DataFrame({'A': [1.0, 2.0, 3.0, 4.0], 'B': [1.0, 4.0, 9.0, 9.0], 'C': [1, 2, 3, 5], 'D': list('abcd')})
if using_infer_string:
    dtype = 'str' if using_infer_string else 'object'
    msg = f'[Cc]annot interpolate with {dtype} dtype'
    with pytest.raises(TypeError, match=msg):
        df.interpolate()
    return
msg = 'DataFrame.interpolate with object dtype'
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = df.interpolate()
tm.assert_frame_equal(result, expected)
cvalues = df['C']._values
dvalues = df['D'].values
if using_copy_on_write:
    assert np.shares_memory(cvalues, result['C']._values)
    assert np.shares_memory(dvalues, result['D']._values)
else:
    assert not np.shares_memory(cvalues, result['C']._values)
    assert not np.shares_memory(dvalues, result['D']._values)
with tm.assert_produces_warning(FutureWarning, match=msg):
    res = df.interpolate(inplace=True)
assert res is None
tm.assert_frame_equal(df, expected)
assert tm.shares_memory(df['C']._values, cvalues)
assert tm.shares_memory(df['D']._values, dvalues)
```

## Next Steps


---

*Source: test_interpolate.py:73 | Complexity: Advanced | Last updated: 2026-06-02*