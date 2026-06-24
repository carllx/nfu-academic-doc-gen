# How To: Read Magic

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test read magic

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

### Step 1: Assign s1 = BytesIO(...)

```python
s1 = BytesIO()
```

**Verification:**
```python
assert_(version1 == (1, 0))
```

### Step 2: Assign s2 = BytesIO(...)

```python
s2 = BytesIO()
```

**Verification:**
```python
assert_(version2 == (2, 0))
```

### Step 3: Assign arr = np.ones(...)

```python
arr = np.ones((3, 6), dtype=float)
```

**Verification:**
```python
assert_(s1.tell() == format.MAGIC_LEN)
```

### Step 4: Call format.write_array()

```python
format.write_array(s1, arr, version=(1, 0))
```

**Verification:**
```python
assert_(s2.tell() == format.MAGIC_LEN)
```

### Step 5: Call format.write_array()

```python
format.write_array(s2, arr, version=(2, 0))
```

### Step 6: Call s1.seek()

```python
s1.seek(0)
```

### Step 7: Call s2.seek()

```python
s2.seek(0)
```

### Step 8: Assign version1 = format.read_magic(...)

```python
version1 = format.read_magic(s1)
```

### Step 9: Assign version2 = format.read_magic(...)

```python
version2 = format.read_magic(s2)
```

### Step 10: Call assert_()

```python
assert_(version1 == (1, 0))
```

### Step 11: Call assert_()

```python
assert_(version2 == (2, 0))
```

### Step 12: Call assert_()

```python
assert_(s1.tell() == format.MAGIC_LEN)
```

### Step 13: Call assert_()

```python
assert_(s2.tell() == format.MAGIC_LEN)
```


## Complete Example

```python
# Workflow
s1 = BytesIO()
s2 = BytesIO()
arr = np.ones((3, 6), dtype=float)
format.write_array(s1, arr, version=(1, 0))
format.write_array(s2, arr, version=(2, 0))
s1.seek(0)
s2.seek(0)
version1 = format.read_magic(s1)
version2 = format.read_magic(s2)
assert_(version1 == (1, 0))
assert_(version2 == (2, 0))
assert_(s1.tell() == format.MAGIC_LEN)
assert_(s2.tell() == format.MAGIC_LEN)
```

## Next Steps


---

*Source: test_format.py:826 | Complexity: Advanced | Last updated: 2026-06-02*