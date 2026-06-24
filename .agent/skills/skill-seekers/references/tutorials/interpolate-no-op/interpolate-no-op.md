# How To: Interpolate No Op

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test interpolate no op

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
# Fixtures: using_copy_on_write, method
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

### Step 3: Assign warn = None

```python
warn = None
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'a'), get_array(df, 'a'))
```

### Step 4: Assign msg = 'DataFrame.interpolate with method=pad is deprecated'

```python
msg = 'DataFrame.interpolate with method=pad is deprecated'
```

### Step 5: Assign unknown = 100

```python
result.iloc[0, 0] = 100
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df, df_orig)
```

### Step 7: Assign warn = FutureWarning

```python
warn = FutureWarning
```

### Step 8: Assign result = df.interpolate(...)

```python
result = df.interpolate(method=method)
```

**Verification:**
```python
assert np.shares_memory(get_array(result, 'a'), get_array(df, 'a'))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, method

# Workflow
df = DataFrame({'a': [1, 2]})
df_orig = df.copy()
warn = None
if method == 'pad':
    warn = FutureWarning
msg = 'DataFrame.interpolate with method=pad is deprecated'
with tm.assert_produces_warning(warn, match=msg):
    result = df.interpolate(method=method)
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

*Source: test_interp_fillna.py:22 | Complexity: Advanced | Last updated: 2026-06-02*