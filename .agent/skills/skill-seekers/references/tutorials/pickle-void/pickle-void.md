# How To: Pickle Void

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pickle void

## Prerequisites

**Required Modules:**
- `collections.abc`
- `pickle`
- `textwrap`
- `io`
- `os`
- `pathlib`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign dt = np.dtype(...)

```python
dt = np.dtype([('obj', 'O'), ('int', 'i')])
```

**Verification:**
```python
assert ctor is np._core.multiarray.scalar
```

### Step 2: Assign a = np.empty(...)

```python
a = np.empty(1, dtype=dt)
```

**Verification:**
```python
assert not isinstance(obj, bytes)
```

### Step 3: Assign data = value

```python
data = (bytearray(b'eman'),)
```

**Verification:**
```python
assert_raises(RuntimeError, ctor, dtype, 13)
```

### Step 4: Assign unknown = data

```python
a['obj'] = data
```

**Verification:**
```python
assert a[0] == unpickled
```

### Step 5: Assign unknown = 42

```python
a['int'] = 42
```

### Step 6: Assign unknown = unknown.__reduce__(...)

```python
ctor, args = a[0].__reduce__()
```

**Verification:**
```python
assert ctor is np._core.multiarray.scalar
```

### Step 7: Assign unknown = args

```python
dtype, obj = args
```

**Verification:**
```python
assert not isinstance(obj, bytes)
```

### Step 8: Call assert_raises()

```python
assert_raises(RuntimeError, ctor, dtype, 13)
```

### Step 9: Assign dump = pickle.dumps(...)

```python
dump = pickle.dumps(a[0])
```

### Step 10: Assign unpickled = pickle.loads(...)

```python
unpickled = pickle.loads(dump)
```

**Verification:**
```python
assert a[0] == unpickled
```

### Step 11: Call ctor()

```python
ctor(np.dtype('O'), data)
```


## Complete Example

```python
# Workflow
dt = np.dtype([('obj', 'O'), ('int', 'i')])
a = np.empty(1, dtype=dt)
data = (bytearray(b'eman'),)
a['obj'] = data
a['int'] = 42
ctor, args = a[0].__reduce__()
assert ctor is np._core.multiarray.scalar
dtype, obj = args
assert not isinstance(obj, bytes)
assert_raises(RuntimeError, ctor, dtype, 13)
dump = pickle.dumps(a[0])
unpickled = pickle.loads(dump)
assert a[0] == unpickled
with assert_raises(TypeError):
    ctor(np.dtype('O'), data)
```

## Next Steps


---

*Source: test_records.py:435 | Complexity: Advanced | Last updated: 2026-06-02*