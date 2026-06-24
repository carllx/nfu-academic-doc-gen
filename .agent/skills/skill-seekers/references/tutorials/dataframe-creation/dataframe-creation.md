# How To: Dataframe Creation

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dataframe creation

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
assert isinstance(df_block._mgr, BlockManager)
```

### Step 2: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(df_block, df_array)
```

**Verification:**
```python
assert isinstance(df_array._mgr, ArrayManager)
```

### Step 3: Assign result = df_block._as_manager(...)

```python
result = df_block._as_manager('block')
```

**Verification:**
```python
assert isinstance(result._mgr, BlockManager)
```

### Step 4: Assign result = df_block._as_manager(...)

```python
result = df_block._as_manager('array')
```

**Verification:**
```python
assert isinstance(result._mgr, ArrayManager)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df_block)
```

**Verification:**
```python
assert all((array_equivalent(left, right) for left, right in zip(result._mgr.arrays, df_array._mgr.arrays)))
```

### Step 6: Assign result = df_array._as_manager(...)

```python
result = df_array._as_manager('array')
```

**Verification:**
```python
assert isinstance(result._mgr, ArrayManager)
```

### Step 7: Assign result = df_array._as_manager(...)

```python
result = df_array._as_manager('block')
```

**Verification:**
```python
assert isinstance(result._mgr, BlockManager)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, df_array)
```

**Verification:**
```python
assert len(result._mgr.blocks) == 2
```

### Step 9: Assign df_block = pd.DataFrame(...)

```python
df_block = pd.DataFrame({'a': [1, 2, 3], 'b': [0.1, 0.2, 0.3], 'c': [4, 5, 6]})
```

### Step 10: Assign df_array = pd.DataFrame(...)

```python
df_array = pd.DataFrame({'a': [1, 2, 3], 'b': [0.1, 0.2, 0.3], 'c': [4, 5, 6]})
```


## Complete Example

```python
# Workflow
msg = 'data_manager option is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    with pd.option_context('mode.data_manager', 'block'):
        df_block = pd.DataFrame({'a': [1, 2, 3], 'b': [0.1, 0.2, 0.3], 'c': [4, 5, 6]})
assert isinstance(df_block._mgr, BlockManager)
with tm.assert_produces_warning(FutureWarning, match=msg):
    with pd.option_context('mode.data_manager', 'array'):
        df_array = pd.DataFrame({'a': [1, 2, 3], 'b': [0.1, 0.2, 0.3], 'c': [4, 5, 6]})
assert isinstance(df_array._mgr, ArrayManager)
tm.assert_frame_equal(df_block, df_array)
result = df_block._as_manager('block')
assert isinstance(result._mgr, BlockManager)
result = df_block._as_manager('array')
assert isinstance(result._mgr, ArrayManager)
tm.assert_frame_equal(result, df_block)
assert all((array_equivalent(left, right) for left, right in zip(result._mgr.arrays, df_array._mgr.arrays)))
result = df_array._as_manager('array')
assert isinstance(result._mgr, ArrayManager)
result = df_array._as_manager('block')
assert isinstance(result._mgr, BlockManager)
tm.assert_frame_equal(result, df_array)
assert len(result._mgr.blocks) == 2
```

## Next Steps


---

*Source: test_managers.py:22 | Complexity: Advanced | Last updated: 2026-06-02*