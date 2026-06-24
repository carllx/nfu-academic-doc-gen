# How To: Bad Header

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test bad header

## Prerequisites

**Required Modules:**
- `os`
- `sys`
- `warnings`
- `io`
- `pytest`
- `numpy`
- `numpy.lib`
- `numpy.testing`
- `numpy.testing._private.utils`
- `numpy.lib._utils_impl`
- `random`
- `subprocess`


## Step-by-Step Guide

### Step 1: Assign s = BytesIO(...)

```python
s = BytesIO()
```

**Verification:**
```python
assert_raises(ValueError, format.read_array_header_1_0, s)
```

### Step 2: Call assert_raises()

```python
assert_raises(ValueError, format.read_array_header_1_0, s)
```

**Verification:**
```python
assert_raises(ValueError, format.read_array_header_1_0, s)
```

### Step 3: Assign s = BytesIO(...)

```python
s = BytesIO(b'1')
```

**Verification:**
```python
assert_raises(ValueError, format.read_array_header_1_0, s)
```

### Step 4: Call assert_raises()

```python
assert_raises(ValueError, format.read_array_header_1_0, s)
```

**Verification:**
```python
assert_raises(ValueError, format.read_array_header_1_0, s)
```

### Step 5: Assign s = BytesIO(...)

```python
s = BytesIO(b'\x01\x00')
```

**Verification:**
```python
assert_raises(ValueError, format.read_array_header_1_0, s)
```

### Step 6: Call assert_raises()

```python
assert_raises(ValueError, format.read_array_header_1_0, s)
```

### Step 7: Assign s = BytesIO(...)

```python
s = BytesIO(b"\x93NUMPY\x01\x006\x00{'descr': 'x', 'shape': (1, 2), }                    \n")
```

### Step 8: Call assert_raises()

```python
assert_raises(ValueError, format.read_array_header_1_0, s)
```

### Step 9: Assign d = value

```python
d = {'shape': (1, 2), 'fortran_order': False, 'descr': 'x', 'extrakey': -1}
```

### Step 10: Assign s = BytesIO(...)

```python
s = BytesIO()
```

### Step 11: Call format.write_array_header_1_0()

```python
format.write_array_header_1_0(s, d)
```

### Step 12: Call assert_raises()

```python
assert_raises(ValueError, format.read_array_header_1_0, s)
```


## Complete Example

```python
# Workflow
s = BytesIO()
assert_raises(ValueError, format.read_array_header_1_0, s)
s = BytesIO(b'1')
assert_raises(ValueError, format.read_array_header_1_0, s)
s = BytesIO(b'\x01\x00')
assert_raises(ValueError, format.read_array_header_1_0, s)
s = BytesIO(b"\x93NUMPY\x01\x006\x00{'descr': 'x', 'shape': (1, 2), }                    \n")
assert_raises(ValueError, format.read_array_header_1_0, s)
d = {'shape': (1, 2), 'fortran_order': False, 'descr': 'x', 'extrakey': -1}
s = BytesIO()
format.write_array_header_1_0(s, d)
assert_raises(ValueError, format.read_array_header_1_0, s)
```

## Next Steps


---

*Source: test_format.py:902 | Complexity: Advanced | Last updated: 2026-06-02*