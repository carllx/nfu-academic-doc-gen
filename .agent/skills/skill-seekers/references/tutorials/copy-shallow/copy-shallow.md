# How To: Copy Shallow

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test copy shallow

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
# Fixtures: using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [0.1, 0.2, 0.3]})
```

**Verification:**
```python
assert df_copy.index is not df.index
```

### Step 2: Assign df_copy = df.copy(...)

```python
df_copy = df.copy(deep=False)
```

**Verification:**
```python
assert df_copy.columns is not df.columns
```

### Step 3: Assign unknown = 0

```python
df_copy.iloc[0, 0] = 0
```

**Verification:**
```python
assert df_copy.index.is_(df.index)
```

### Step 4: Assign unknown = 0

```python
df_copy.iloc[0, 0] = 0
```

**Verification:**
```python
assert df_copy.columns.is_(df.columns)
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write, warn_copy_on_write

# Workflow
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [0.1, 0.2, 0.3]})
df_copy = df.copy(deep=False)
if using_copy_on_write:
    assert df_copy.index is not df.index
    assert df_copy.columns is not df.columns
    assert df_copy.index.is_(df.index)
    assert df_copy.columns.is_(df.columns)
else:
    assert df_copy.index is df.index
    assert df_copy.columns is df.columns
assert np.shares_memory(get_array(df_copy, 'a'), get_array(df, 'a'))
if using_copy_on_write:
    assert df_copy._mgr.blocks[0].refs.has_reference()
    assert df_copy._mgr.blocks[1].refs.has_reference()
if using_copy_on_write:
    df_copy.iloc[0, 0] = 0
    assert df.iloc[0, 0] == 1
    assert not np.shares_memory(get_array(df_copy, 'a'), get_array(df, 'a'))
    assert np.shares_memory(get_array(df_copy, 'c'), get_array(df, 'c'))
else:
    with tm.assert_cow_warning(warn_copy_on_write):
        df_copy.iloc[0, 0] = 0
    assert df.iloc[0, 0] == 0
    assert np.shares_memory(get_array(df_copy, 'a'), get_array(df, 'a'))
```

## Next Steps


---

*Source: test_methods.py:48 | Complexity: Intermediate | Last updated: 2026-06-02*