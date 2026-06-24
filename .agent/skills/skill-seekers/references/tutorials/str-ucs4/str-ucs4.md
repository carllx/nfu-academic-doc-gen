# How To: Str Ucs4

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test str ucs4

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `numpy`
- `numpy._core._multiarray_tests`
- `numpy._core._rational_tests`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: s
```

## Step-by-Step Guide

### Step 1: Assign s = np.str_(...)

```python
s = np.str_(s)
```

**Verification:**
```python
assert self._as_dict(v) == expected
```

### Step 2: Assign expected = value

```python
expected = {'strides': (), 'itemsize': 8, 'ndim': 0, 'shape': (), 'format': '2w', 'readonly': True}
```

**Verification:**
```python
assert_equal(code_points, [ord(c) for c in s])
```

### Step 3: Assign v = memoryview(...)

```python
v = memoryview(s)
```

**Verification:**
```python
assert self._as_dict(v) == expected
```

### Step 4: Assign code_points = np.frombuffer(...)

```python
code_points = np.frombuffer(v, dtype='i4')
```

### Step 5: Call assert_equal()

```python
assert_equal(code_points, [ord(c) for c in s])
```

### Step 6: Call get_buffer_info()

```python
get_buffer_info(s, ['WRITABLE'])
```


## Complete Example

```python
# Setup
# Fixtures: s

# Workflow
s = np.str_(s)
expected = {'strides': (), 'itemsize': 8, 'ndim': 0, 'shape': (), 'format': '2w', 'readonly': True}
v = memoryview(s)
assert self._as_dict(v) == expected
code_points = np.frombuffer(v, dtype='i4')
assert_equal(code_points, [ord(c) for c in s])
with pytest.raises(BufferError, match='scalar buffer is readonly'):
    get_buffer_info(s, ['WRITABLE'])
```

## Next Steps


---

*Source: test_scalarbuffer.py:127 | Complexity: Intermediate | Last updated: 2026-06-02*