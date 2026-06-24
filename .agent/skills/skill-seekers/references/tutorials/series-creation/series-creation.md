# How To: Series Creation

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series creation

## Prerequisites

**Required Modules:**
- `os`
- `subprocess`
- `sys`
- `pytest`
- `pandas.core.dtypes.missing`
- `pandas`
- `pandas._testing`
- `pandas.core.internals`


## Step-by-Step Guide

### Step 1: Assign msg = 'data_manager option is deprecated'

```python
msg = 'data_manager option is deprecated'
```

**Verification:**
```python
assert isinstance(s_block._mgr, SingleBlockManager)
```

### Step 2: Call tm.assert_series_equal()

```python
tm.assert_series_equal(s_block, s_array)
```

**Verification:**
```python
assert isinstance(s_array._mgr, SingleArrayManager)
```

### Step 3: Assign result = s_block._as_manager(...)

```python
result = s_block._as_manager('block')
```

**Verification:**
```python
assert isinstance(result._mgr, SingleBlockManager)
```

### Step 4: Assign result = s_block._as_manager(...)

```python
result = s_block._as_manager('array')
```

**Verification:**
```python
assert isinstance(result._mgr, SingleArrayManager)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, s_block)
```

**Verification:**
```python
assert isinstance(result._mgr, SingleArrayManager)
```

### Step 6: Assign result = s_array._as_manager(...)

```python
result = s_array._as_manager('array')
```

**Verification:**
```python
assert isinstance(result._mgr, SingleBlockManager)
```

### Step 7: Assign result = s_array._as_manager(...)

```python
result = s_array._as_manager('block')
```

**Verification:**
```python
assert isinstance(result._mgr, SingleBlockManager)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, s_array)
```

### Step 9: Assign s_block = pd.Series(...)

```python
s_block = pd.Series([1, 2, 3], name='A', index=['a', 'b', 'c'])
```

### Step 10: Assign s_array = pd.Series(...)

```python
s_array = pd.Series([1, 2, 3], name='A', index=['a', 'b', 'c'])
```


## Complete Example

```python
# Workflow
msg = 'data_manager option is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    with pd.option_context('mode.data_manager', 'block'):
        s_block = pd.Series([1, 2, 3], name='A', index=['a', 'b', 'c'])
assert isinstance(s_block._mgr, SingleBlockManager)
with tm.assert_produces_warning(FutureWarning, match=msg):
    with pd.option_context('mode.data_manager', 'array'):
        s_array = pd.Series([1, 2, 3], name='A', index=['a', 'b', 'c'])
assert isinstance(s_array._mgr, SingleArrayManager)
tm.assert_series_equal(s_block, s_array)
result = s_block._as_manager('block')
assert isinstance(result._mgr, SingleBlockManager)
result = s_block._as_manager('array')
assert isinstance(result._mgr, SingleArrayManager)
tm.assert_series_equal(result, s_block)
result = s_array._as_manager('array')
assert isinstance(result._mgr, SingleArrayManager)
result = s_array._as_manager('block')
assert isinstance(result._mgr, SingleBlockManager)
tm.assert_series_equal(result, s_array)
```

## Next Steps


---

*Source: test_managers.py:60 | Complexity: Advanced | Last updated: 2026-06-02*