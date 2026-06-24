# How To: Consolidate

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test consolidate

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
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
df = DataFrame({'a': [1, 2, 3], 'b': [0.1, 0.2, 0.3]})
```

**Verification:**
```python
assert all((blk.refs.has_reference() for blk in subset._mgr.blocks))
```

### Step 2: Assign unknown = value

```python
df['c'] = [4, 5, 6]
```

**Verification:**
```python
assert subset._mgr.blocks[0].refs.has_reference()
```

### Step 3: Assign subset = value

```python
subset = df[:]
```

**Verification:**
```python
assert np.shares_memory(get_array(df, 'b'), get_array(subset, 'b'))
```

### Step 4: Call subset._consolidate_inplace()

```python
subset._consolidate_inplace()
```

**Verification:**
```python
assert not subset._mgr.blocks[1].refs.has_reference()
```

### Step 5: Assign unknown = 0.0

```python
subset.iloc[0, 1] = 0.0
```

**Verification:**
```python
assert not df._mgr.blocks[0].refs.has_reference()
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
df = DataFrame({'a': [1, 2, 3], 'b': [0.1, 0.2, 0.3]})
df['c'] = [4, 5, 6]
subset = df[:]
assert all((blk.refs.has_reference() for blk in subset._mgr.blocks))
subset._consolidate_inplace()
assert subset._mgr.blocks[0].refs.has_reference()
assert np.shares_memory(get_array(df, 'b'), get_array(subset, 'b'))
assert not subset._mgr.blocks[1].refs.has_reference()
assert not df._mgr.blocks[0].refs.has_reference()
assert df._mgr.blocks[1].refs.has_reference()
assert not df._mgr.blocks[2].refs.has_reference()
if using_copy_on_write:
    subset.iloc[0, 1] = 0.0
    assert not df._mgr.blocks[1].refs.has_reference()
    assert df.loc[0, 'b'] == 0.1
```

## Next Steps


---

*Source: test_internals.py:16 | Complexity: Intermediate | Last updated: 2026-06-02*