# How To: Concat Frames Updating Input

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat frames updating input

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
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
df = DataFrame({'b': ['a'] * 3}, dtype=object)
```

**Verification:**
```python
assert np.shares_memory(get_array(result, 'b'), get_array(df, 'b'))
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'a': ['a'] * 3}, dtype=object)
```

**Verification:**
```python
assert np.shares_memory(get_array(result, 'a'), get_array(df2, 'a'))
```

### Step 3: Assign result = concat(...)

```python
result = concat([df, df2], axis=1)
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'b'), get_array(df, 'b'))
```

### Step 4: Assign expected = result.copy(...)

```python
expected = result.copy()
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'a'), get_array(df2, 'a'))
```

### Step 5: Assign unknown = 'd'

```python
df.iloc[0, 0] = 'd'
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'b'), get_array(df, 'b'))
```

### Step 6: Assign unknown = 'd'

```python
df2.iloc[0, 0] = 'd'
```

**Verification:**
```python
assert np.shares_memory(get_array(result, 'a'), get_array(df2, 'a'))
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'a'), get_array(df2, 'a'))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
df = DataFrame({'b': ['a'] * 3}, dtype=object)
df2 = DataFrame({'a': ['a'] * 3}, dtype=object)
result = concat([df, df2], axis=1)
if using_copy_on_write:
    assert np.shares_memory(get_array(result, 'b'), get_array(df, 'b'))
    assert np.shares_memory(get_array(result, 'a'), get_array(df2, 'a'))
else:
    assert not np.shares_memory(get_array(result, 'b'), get_array(df, 'b'))
    assert not np.shares_memory(get_array(result, 'a'), get_array(df2, 'a'))
expected = result.copy()
df.iloc[0, 0] = 'd'
if using_copy_on_write:
    assert not np.shares_memory(get_array(result, 'b'), get_array(df, 'b'))
    assert np.shares_memory(get_array(result, 'a'), get_array(df2, 'a'))
df2.iloc[0, 0] = 'd'
if using_copy_on_write:
    assert not np.shares_memory(get_array(result, 'a'), get_array(df2, 'a'))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_functions.py:39 | Complexity: Intermediate | Last updated: 2026-06-02*