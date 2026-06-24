# How To: Series From Series

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test series from series

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.copy_view.util`

**Setup Required:**
```python
# Fixtures: dtype, using_copy_on_write, warn_copy_on_write
```

## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([1, 2, 3], name='name')
```

**Verification:**
```python
assert np.shares_memory(get_array(ser), get_array(result))
```

### Step 2: Assign result = Series(...)

```python
result = Series(ser, dtype=dtype)
```

**Verification:**
```python
assert result._mgr.blocks[0].refs.has_reference()
```

### Step 3: Assign result = Series(...)

```python
result = Series(ser, dtype=dtype)
```

**Verification:**
```python
assert ser.iloc[0] == 1
```

### Step 4: Assign unknown = 0

```python
result.iloc[0] = 0
```

**Verification:**
```python
assert not np.shares_memory(get_array(ser), get_array(result))
```

### Step 5: Assign unknown = 0

```python
ser.iloc[0] = 0
```

**Verification:**
```python
assert ser.iloc[0] == 0
```

### Step 6: Assign unknown = 0

```python
result.iloc[0] = 0
```

**Verification:**
```python
assert np.shares_memory(get_array(ser), get_array(result))
```

### Step 7: Assign unknown = 0

```python
ser.iloc[0] = 0
```

**Verification:**
```python
assert result.iloc[0] == 1
```


## Complete Example

```python
# Setup
# Fixtures: dtype, using_copy_on_write, warn_copy_on_write

# Workflow
ser = Series([1, 2, 3], name='name')
result = Series(ser, dtype=dtype)
assert np.shares_memory(get_array(ser), get_array(result))
if using_copy_on_write:
    assert result._mgr.blocks[0].refs.has_reference()
if using_copy_on_write:
    result.iloc[0] = 0
    assert ser.iloc[0] == 1
    assert not np.shares_memory(get_array(ser), get_array(result))
else:
    with tm.assert_cow_warning(warn_copy_on_write):
        result.iloc[0] = 0
    assert ser.iloc[0] == 0
    assert np.shares_memory(get_array(ser), get_array(result))
result = Series(ser, dtype=dtype)
if using_copy_on_write:
    ser.iloc[0] = 0
    assert result.iloc[0] == 1
else:
    with tm.assert_cow_warning(warn_copy_on_write):
        ser.iloc[0] = 0
    assert result.iloc[0] == 0
```

## Next Steps


---

*Source: test_constructors.py:24 | Complexity: Intermediate | Last updated: 2026-06-02*