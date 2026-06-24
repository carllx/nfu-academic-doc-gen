# How To: Recarray Repr

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test recarray repr

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

### Step 1: Assign a = np.array(...)

```python
a = np.array([(1, 0.1), (2, 0.2)], dtype=[('foo', '<i4'), ('bar', '<f8')])
```

**Verification:**
```python
assert_equal(repr(a), textwrap.dedent("            rec.array([(1, 0.1), (2, 0.2)],\n                      dtype=[('foo', '<i4'), ('bar', '<f8')])"))
```

### Step 2: Assign a = np.rec.array(...)

```python
a = np.rec.array(a)
```

**Verification:**
```python
assert_(repr(np.rec.array(a)).startswith('rec.array'))
```

### Step 3: Call assert_equal()

```python
assert_equal(repr(a), textwrap.dedent("            rec.array([(1, 0.1), (2, 0.2)],\n                      dtype=[('foo', '<i4'), ('bar', '<f8')])"))
```

**Verification:**
```python
assert_equal(repr(a).find('numpy.record'), -1)
```

### Step 4: Assign a = np.array(...)

```python
a = np.array(np.ones(4, dtype='f8'))
```

**Verification:**
```python
assert_(repr(a).find('dtype=int32') != -1)
```

### Step 5: Call assert_()

```python
assert_(repr(np.rec.array(a)).startswith('rec.array'))
```

### Step 6: Assign a = np.rec.array(...)

```python
a = np.rec.array(np.ones(3, dtype='i4,i4'))
```

### Step 7: Call assert_equal()

```python
assert_equal(repr(a).find('numpy.record'), -1)
```

### Step 8: Assign a = np.rec.array(...)

```python
a = np.rec.array(np.ones(3, dtype='i4'))
```

### Step 9: Call assert_()

```python
assert_(repr(a).find('dtype=int32') != -1)
```


## Complete Example

```python
# Workflow
a = np.array([(1, 0.1), (2, 0.2)], dtype=[('foo', '<i4'), ('bar', '<f8')])
a = np.rec.array(a)
assert_equal(repr(a), textwrap.dedent("            rec.array([(1, 0.1), (2, 0.2)],\n                      dtype=[('foo', '<i4'), ('bar', '<f8')])"))
a = np.array(np.ones(4, dtype='f8'))
assert_(repr(np.rec.array(a)).startswith('rec.array'))
a = np.rec.array(np.ones(3, dtype='i4,i4'))
assert_equal(repr(a).find('numpy.record'), -1)
a = np.rec.array(np.ones(3, dtype='i4'))
assert_(repr(a).find('dtype=int32') != -1)
```

## Next Steps


---

*Source: test_records.py:125 | Complexity: Advanced | Last updated: 2026-06-02*