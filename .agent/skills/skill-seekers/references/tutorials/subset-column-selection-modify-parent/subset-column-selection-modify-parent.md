# How To: Subset Column Selection Modify Parent

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test subset column selection modify parent

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`

**Setup Required:**
```python
# Fixtures: backend, using_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign unknown = backend

```python
_, DataFrame, _ = backend
```

**Verification:**
```python
assert np.shares_memory(get_array(subset, 'a'), get_array(df, 'a'))
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [0.1, 0.2, 0.3]})
```

**Verification:**
```python
assert not np.shares_memory(get_array(subset, 'a'), get_array(df, 'a'))
```

### Step 3: Assign subset = value

```python
subset = df[['a', 'c']]
```

**Verification:**
```python
assert np.shares_memory(get_array(subset, 'c'), get_array(df, 'c'))
```

### Step 4: Assign unknown = 0

```python
df.iloc[0, 0] = 0
```

**Verification:**
```python
assert not np.shares_memory(get_array(subset, 'a'), get_array(df, 'a'))
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1, 2, 3], 'c': [0.1, 0.2, 0.3]})
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(subset, expected)
```

**Verification:**
```python
assert np.shares_memory(get_array(subset, 'a'), get_array(df, 'a'))
```


## Complete Example

```python
# Setup
# Fixtures: backend, using_copy_on_write

# Workflow
_, DataFrame, _ = backend
df = DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [0.1, 0.2, 0.3]})
subset = df[['a', 'c']]
if using_copy_on_write:
    assert np.shares_memory(get_array(subset, 'a'), get_array(df, 'a'))
df.iloc[0, 0] = 0
assert not np.shares_memory(get_array(subset, 'a'), get_array(df, 'a'))
if using_copy_on_write:
    assert np.shares_memory(get_array(subset, 'c'), get_array(df, 'c'))
expected = DataFrame({'a': [1, 2, 3], 'c': [0.1, 0.2, 0.3]})
tm.assert_frame_equal(subset, expected)
```

## Next Steps


---

*Source: test_indexing.py:81 | Complexity: Intermediate | Last updated: 2026-06-02*