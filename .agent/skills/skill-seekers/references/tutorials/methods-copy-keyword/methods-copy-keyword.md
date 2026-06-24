# How To: Methods Copy Keyword

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test methods copy keyword

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
# Fixtures: request, method, copy, using_copy_on_write, using_array_manager
```

## Step-by-Step Guide

### Step 1: Assign index = None

```python
index = None
```

**Verification:**
```python
assert np.shares_memory(get_array(df2, 'a'), get_array(df, 'a'))
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [0.1, 0.2, 0.3]}, index=index)
```

**Verification:**
```python
assert not np.shares_memory(get_array(df2, 'a'), get_array(df, 'a'))
```

### Step 3: Assign share_memory = value

```python
share_memory = using_copy_on_write or copy is False
```

### Step 4: Assign index = period_range(...)

```python
index = period_range('2012-01-01', freq='D', periods=3)
```

### Step 5: Assign msg = "'DataFrame.swapaxes' is deprecated"

```python
msg = "'DataFrame.swapaxes' is deprecated"
```

### Step 6: Assign df2 = method(...)

```python
df2 = method(df, copy=copy)
```

**Verification:**
```python
assert np.shares_memory(get_array(df2, 'a'), get_array(df, 'a'))
```

### Step 7: Assign index = date_range(...)

```python
index = date_range('2012-01-01', freq='D', periods=3)
```

### Step 8: Assign df2 = method(...)

```python
df2 = method(df, copy=copy)
```

### Step 9: Assign share_memory = False

```python
share_memory = False
```

### Step 10: Assign index = date_range(...)

```python
index = date_range('2012-01-01', freq='D', periods=3)
```

### Step 11: Assign index = date_range(...)

```python
index = date_range('2012-01-01', freq='D', periods=3, tz='Europe/Brussels')
```


## Complete Example

```python
# Setup
# Fixtures: request, method, copy, using_copy_on_write, using_array_manager

# Workflow
index = None
if 'to_timestamp' in request.node.callspec.id:
    index = period_range('2012-01-01', freq='D', periods=3)
elif 'to_period' in request.node.callspec.id:
    index = date_range('2012-01-01', freq='D', periods=3)
elif 'tz_localize' in request.node.callspec.id:
    index = date_range('2012-01-01', freq='D', periods=3)
elif 'tz_convert' in request.node.callspec.id:
    index = date_range('2012-01-01', freq='D', periods=3, tz='Europe/Brussels')
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [0.1, 0.2, 0.3]}, index=index)
if 'swapaxes' in request.node.callspec.id:
    msg = "'DataFrame.swapaxes' is deprecated"
    with tm.assert_produces_warning(FutureWarning, match=msg):
        df2 = method(df, copy=copy)
else:
    df2 = method(df, copy=copy)
share_memory = using_copy_on_write or copy is False
if request.node.callspec.id.startswith('reindex-'):
    if not using_copy_on_write and (not using_array_manager) and (copy is False):
        share_memory = False
if share_memory:
    assert np.shares_memory(get_array(df2, 'a'), get_array(df, 'a'))
else:
    assert not np.shares_memory(get_array(df2, 'a'), get_array(df, 'a'))
```

## Next Steps


---

*Source: test_methods.py:127 | Complexity: Advanced | Last updated: 2026-06-02*