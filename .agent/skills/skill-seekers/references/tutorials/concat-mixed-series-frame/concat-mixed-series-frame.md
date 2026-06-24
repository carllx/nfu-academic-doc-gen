# How To: Concat Mixed Series Frame

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat mixed series frame

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
df = DataFrame({'a': [1, 2, 3], 'c': 1})
```

**Verification:**
```python
assert np.shares_memory(get_array(result, 'a'), get_array(df, 'a'))
```

### Step 2: Assign ser = Series(...)

```python
ser = Series([4, 5, 6], name='d')
```

**Verification:**
```python
assert np.shares_memory(get_array(result, 'c'), get_array(df, 'c'))
```

### Step 3: Assign result = concat(...)

```python
result = concat([df, ser], axis=1)
```

**Verification:**
```python
assert np.shares_memory(get_array(result, 'd'), get_array(ser, 'd'))
```

### Step 4: Assign expected = result.copy(...)

```python
expected = result.copy()
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'a'), get_array(df, 'a'))
```

### Step 5: Assign unknown = 100

```python
ser.iloc[0] = 100
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'c'), get_array(df, 'c'))
```

### Step 6: Assign unknown = 100

```python
df.iloc[0, 0] = 100
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'd'), get_array(ser, 'd'))
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'd'), get_array(ser, 'd'))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
df = DataFrame({'a': [1, 2, 3], 'c': 1})
ser = Series([4, 5, 6], name='d')
result = concat([df, ser], axis=1)
expected = result.copy()
if using_copy_on_write:
    assert np.shares_memory(get_array(result, 'a'), get_array(df, 'a'))
    assert np.shares_memory(get_array(result, 'c'), get_array(df, 'c'))
    assert np.shares_memory(get_array(result, 'd'), get_array(ser, 'd'))
else:
    assert not np.shares_memory(get_array(result, 'a'), get_array(df, 'a'))
    assert not np.shares_memory(get_array(result, 'c'), get_array(df, 'c'))
    assert not np.shares_memory(get_array(result, 'd'), get_array(ser, 'd'))
ser.iloc[0] = 100
if using_copy_on_write:
    assert not np.shares_memory(get_array(result, 'd'), get_array(ser, 'd'))
df.iloc[0, 0] = 100
if using_copy_on_write:
    assert not np.shares_memory(get_array(result, 'a'), get_array(df, 'a'))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_functions.py:160 | Complexity: Intermediate | Last updated: 2026-06-02*