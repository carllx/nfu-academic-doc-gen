# How To: Interpolate Downcast Reference Triggers Copy

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test interpolate downcast reference triggers copy

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
df = DataFrame({'a': [1, np.nan, 2.5], 'b': 1})
```

**Verification:**
```python
assert df._mgr._has_no_reference(0)
```

### Step 2: Assign df_orig = df.copy(...)

```python
df_orig = df.copy()
```

**Verification:**
```python
assert not np.shares_memory(arr_a, get_array(df, 'a'))
```

### Step 3: Assign arr_a = get_array(...)

```python
arr_a = get_array(df, 'a')
```

### Step 4: Assign view = value

```python
view = df[:]
```

### Step 5: Assign msg = 'DataFrame.interpolate with method=pad is deprecated'

```python
msg = 'DataFrame.interpolate with method=pad is deprecated'
```

### Step 6: Call df.interpolate()

```python
df.interpolate(method='pad', inplace=True, downcast='infer')
```

**Verification:**
```python
assert df._mgr._has_no_reference(0)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_orig, view)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, view)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
df = DataFrame({'a': [1, np.nan, 2.5], 'b': 1})
df_orig = df.copy()
arr_a = get_array(df, 'a')
view = df[:]
msg = 'DataFrame.interpolate with method=pad is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    df.interpolate(method='pad', inplace=True, downcast='infer')
if using_copy_on_write:
    assert df._mgr._has_no_reference(0)
    assert not np.shares_memory(arr_a, get_array(df, 'a'))
    tm.assert_frame_equal(df_orig, view)
else:
    tm.assert_frame_equal(df, view)
```

## Next Steps


---

*Source: test_interp_fillna.py:199 | Complexity: Advanced | Last updated: 2026-06-02*