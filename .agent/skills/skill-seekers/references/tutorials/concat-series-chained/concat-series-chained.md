# How To: Concat Series Chained

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat series chained

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

### Step 1: Assign ser1 = Series(...)

```python
ser1 = Series([1, 2, 3], name='a')
```

**Verification:**
```python
assert np.shares_memory(get_array(result, 'a'), get_array(ser1, 'a'))
```

### Step 2: Assign ser2 = Series(...)

```python
ser2 = Series([4, 5, 6], name='c')
```

**Verification:**
```python
assert np.shares_memory(get_array(result, 'c'), get_array(ser2, 'c'))
```

### Step 3: Assign ser3 = Series(...)

```python
ser3 = Series([4, 5, 6], name='d')
```

**Verification:**
```python
assert np.shares_memory(get_array(result, 'd'), get_array(ser3, 'd'))
```

### Step 4: Assign result = concat(...)

```python
result = concat([concat([ser1, ser2], axis=1), ser3], axis=1)
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'a'), get_array(ser1, 'a'))
```

### Step 5: Assign expected = result.copy(...)

```python
expected = result.copy()
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'c'), get_array(ser2, 'c'))
```

### Step 6: Assign unknown = 100

```python
ser1.iloc[0] = 100
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'd'), get_array(ser3, 'd'))
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'a'), get_array(ser1, 'a'))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
ser1 = Series([1, 2, 3], name='a')
ser2 = Series([4, 5, 6], name='c')
ser3 = Series([4, 5, 6], name='d')
result = concat([concat([ser1, ser2], axis=1), ser3], axis=1)
expected = result.copy()
if using_copy_on_write:
    assert np.shares_memory(get_array(result, 'a'), get_array(ser1, 'a'))
    assert np.shares_memory(get_array(result, 'c'), get_array(ser2, 'c'))
    assert np.shares_memory(get_array(result, 'd'), get_array(ser3, 'd'))
else:
    assert not np.shares_memory(get_array(result, 'a'), get_array(ser1, 'a'))
    assert not np.shares_memory(get_array(result, 'c'), get_array(ser2, 'c'))
    assert not np.shares_memory(get_array(result, 'd'), get_array(ser3, 'd'))
ser1.iloc[0] = 100
if using_copy_on_write:
    assert not np.shares_memory(get_array(result, 'a'), get_array(ser1, 'a'))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_functions.py:112 | Complexity: Intermediate | Last updated: 2026-06-02*