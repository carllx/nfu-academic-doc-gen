# How To: Datetime Memoryview

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test datetime memoryview

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy._core._multiarray_tests`
- `numpy._core._rational_tests`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign dt1 = np.datetime64(...)

```python
dt1 = np.datetime64('2016-01-01')
```

**Verification:**
```python
assert self._as_dict(v) == expected
```

### Step 2: Assign dt2 = np.datetime64(...)

```python
dt2 = np.datetime64('2017-01-01')
```

**Verification:**
```python
assert self._as_dict(v) == expected
```

### Step 3: Assign expected = value

```python
expected = {'strides': (1,), 'itemsize': 1, 'ndim': 1, 'shape': (8,), 'format': 'B', 'readonly': True}
```

**Verification:**
```python
assert_raises((ValueError, BufferError), memoryview, a[0])
```

### Step 4: Assign v = memoryview(...)

```python
v = memoryview(dt1)
```

**Verification:**
```python
assert self._as_dict(v) == expected
```

### Step 5: Assign v = memoryview(...)

```python
v = memoryview(dt2 - dt1)
```

**Verification:**
```python
assert self._as_dict(v) == expected
```

### Step 6: Assign dt = np.dtype(...)

```python
dt = np.dtype([('a', 'uint16'), ('b', 'M8[s]')])
```

### Step 7: Assign a = np.empty(...)

```python
a = np.empty(1, dt)
```

### Step 8: Call assert_raises()

```python
assert_raises((ValueError, BufferError), memoryview, a[0])
```

### Step 9: Call get_buffer_info()

```python
get_buffer_info(dt1, ['WRITABLE'])
```


## Complete Example

```python
# Workflow
dt1 = np.datetime64('2016-01-01')
dt2 = np.datetime64('2017-01-01')
expected = {'strides': (1,), 'itemsize': 1, 'ndim': 1, 'shape': (8,), 'format': 'B', 'readonly': True}
v = memoryview(dt1)
assert self._as_dict(v) == expected
v = memoryview(dt2 - dt1)
assert self._as_dict(v) == expected
dt = np.dtype([('a', 'uint16'), ('b', 'M8[s]')])
a = np.empty(1, dt)
assert_raises((ValueError, BufferError), memoryview, a[0])
with pytest.raises(BufferError, match='scalar buffer is readonly'):
    get_buffer_info(dt1, ['WRITABLE'])
```

## Next Steps


---

*Source: test_scalarbuffer.py:99 | Complexity: Advanced | Last updated: 2026-06-02*