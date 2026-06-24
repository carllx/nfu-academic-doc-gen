# How To: Concat Series Updating Input

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat series updating input

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

### Step 1: Assign ser = Series(...)

```python
ser = Series([1, 2], name='a')
```

**Verification:**
```python
assert np.shares_memory(get_array(result, 'a'), get_array(ser, 'a'))
```

### Step 2: Assign ser2 = Series(...)

```python
ser2 = Series([3, 4], name='b')
```

**Verification:**
```python
assert np.shares_memory(get_array(result, 'b'), get_array(ser2, 'b'))
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'a': [1, 2], 'b': [3, 4]})
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'a'), get_array(ser, 'a'))
```

### Step 4: Assign result = concat(...)

```python
result = concat([ser, ser2], axis=1)
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'b'), get_array(ser2, 'b'))
```

### Step 5: Assign unknown = 100

```python
ser.iloc[0] = 100
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'a'), get_array(ser, 'a'))
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

**Verification:**
```python
assert np.shares_memory(get_array(result, 'b'), get_array(ser2, 'b'))
```

### Step 7: Assign unknown = 1000

```python
ser2.iloc[0] = 1000
```

**Verification:**
```python
assert not np.shares_memory(get_array(result, 'b'), get_array(ser2, 'b'))
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

**Verification:**
```python
assert np.shares_memory(get_array(result, 'a'), get_array(ser, 'a'))
```


## Complete Example

```python
# Setup
# Fixtures: using_copy_on_write

# Workflow
ser = Series([1, 2], name='a')
ser2 = Series([3, 4], name='b')
expected = DataFrame({'a': [1, 2], 'b': [3, 4]})
result = concat([ser, ser2], axis=1)
if using_copy_on_write:
    assert np.shares_memory(get_array(result, 'a'), get_array(ser, 'a'))
    assert np.shares_memory(get_array(result, 'b'), get_array(ser2, 'b'))
else:
    assert not np.shares_memory(get_array(result, 'a'), get_array(ser, 'a'))
    assert not np.shares_memory(get_array(result, 'b'), get_array(ser2, 'b'))
ser.iloc[0] = 100
if using_copy_on_write:
    assert not np.shares_memory(get_array(result, 'a'), get_array(ser, 'a'))
    assert np.shares_memory(get_array(result, 'b'), get_array(ser2, 'b'))
tm.assert_frame_equal(result, expected)
ser2.iloc[0] = 1000
if using_copy_on_write:
    assert not np.shares_memory(get_array(result, 'b'), get_array(ser2, 'b'))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_functions.py:135 | Complexity: Advanced | Last updated: 2026-06-02*