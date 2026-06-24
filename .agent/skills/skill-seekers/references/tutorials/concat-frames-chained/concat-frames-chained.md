# How To: Concat Frames Chained

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat frames chained

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

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame({'a': [1, 2, 3], 'b': [0.1, 0.2, 0.3]})
```

**Verification:**
```python
assert np.shares_memory(get_array(result, 'a'), get_array(df1, 'a'))
```

### Step 2: Assign df2 = DataFrame(...)

```python
df2 = DataFrame({'c': [4, 5, 6]})
```

**Verification:**
```python
assert np.shares_memory(get_array(result, 'c'), get_array(df2, 'c'))
```

### Step 3: Assign df3 = DataFrame(...)

```python
df3 = DataFrame({'d': [4, 5, 6]})
```

**Verification:**
```python
assert np.shares_memory(get_array(result, 'd'), get_array(df3, 'd'))
```

### Step 4: Assign result = concat(...)

```python
result = concat([concat([df1, df2], axis=1), df3], axis=1)
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'a'), get_array(df1, 'a'))
```

### Step 5: Assign expected = result.copy(...)

```python
expected = result.copy()
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'c'), get_array(df2, 'c'))
```

### Step 6: Assign unknown = 100

```python
df1.iloc[0, 0] = 100
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'd'), get_array(df3, 'd'))
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'a'), get_array(df1, 'a'))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
df1 = DataFrame({'a': [1, 2, 3], 'b': [0.1, 0.2, 0.3]})
df2 = DataFrame({'c': [4, 5, 6]})
df3 = DataFrame({'d': [4, 5, 6]})
result = concat([concat([df1, df2], axis=1), df3], axis=1)
expected = result.copy()
if using_copy_on_write:
    assert np.shares_memory(get_array(result, 'a'), get_array(df1, 'a'))
    assert np.shares_memory(get_array(result, 'c'), get_array(df2, 'c'))
    assert np.shares_memory(get_array(result, 'd'), get_array(df3, 'd'))
else:
    assert not np.shares_memory(get_array(result, 'a'), get_array(df1, 'a'))
    assert not np.shares_memory(get_array(result, 'c'), get_array(df2, 'c'))
    assert not np.shares_memory(get_array(result, 'd'), get_array(df3, 'd'))
df1.iloc[0, 0] = 100
if using_copy_on_write:
    assert not np.shares_memory(get_array(result, 'a'), get_array(df1, 'a'))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_functions.py:89 | Complexity: Intermediate | Last updated: 2026-06-02*