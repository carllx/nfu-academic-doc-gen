# How To: Pickle Python2 Python3

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test pickle python2 python3

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

### Step 1: Assign data_dir = os.path.join(...)

```python
data_dir = os.path.join(os.path.dirname(__file__), 'data')
```

**Verification:**
```python
assert_(isinstance(data[3], str))
```

### Step 2: Assign expected = np.array(...)

```python
expected = np.array([None, range, '優良', b'\xe4\xb8\x8d\xe8\x89\xaf'], dtype=object)
```

**Verification:**
```python
assert_array_equal(data[:-1], expected[:-1])
```

### Step 3: Assign path = os.path.join(...)

```python
path = os.path.join(data_dir, fname)
```

**Verification:**
```python
assert_array_equal(data[-1].encode(encoding), expected[-1])
```

### Step 4: Assign data_f = np.load(...)

```python
data_f = np.load(path, allow_pickle=True, encoding=encoding)
```

**Verification:**
```python
assert_(isinstance(data[3], bytes))
```

### Step 5: Assign data = value

```python
data = data_f['x']
```

**Verification:**
```python
assert_array_equal(data, expected)
```

### Step 6: Call data_f.close()

```python
data_f.close()
```

**Verification:**
```python
assert_raises(UnicodeError, data.__getitem__, 'x')
```

### Step 7: Assign data = data_f

```python
data = data_f
```

**Verification:**
```python
assert_raises(ImportError, data.__getitem__, 'x')
```

### Step 8: Call assert_()

```python
assert_(isinstance(data[3], str))
```

**Verification:**
```python
assert_raises(UnicodeError, np.load, path, allow_pickle=True)
```

### Step 9: Call assert_array_equal()

```python
assert_array_equal(data[:-1], expected[:-1])
```

**Verification:**
```python
assert_raises(ImportError, np.load, path, allow_pickle=True, fix_imports=False, encoding='latin1')
```

### Step 10: Call assert_array_equal()

```python
assert_array_equal(data[-1].encode(encoding), expected[-1])
```

### Step 11: Call assert_()

```python
assert_(isinstance(data[3], bytes))
```

### Step 12: Call assert_array_equal()

```python
assert_array_equal(data, expected)
```

### Step 13: Assign data = np.load(...)

```python
data = np.load(path, allow_pickle=True)
```

### Step 14: Call assert_raises()

```python
assert_raises(UnicodeError, data.__getitem__, 'x')
```

### Step 15: Call data.close()

```python
data.close()
```

### Step 16: Assign data = np.load(...)

```python
data = np.load(path, allow_pickle=True, fix_imports=False, encoding='latin1')
```

### Step 17: Call assert_raises()

```python
assert_raises(ImportError, data.__getitem__, 'x')
```

### Step 18: Call data.close()

```python
data.close()
```

### Step 19: Call assert_raises()

```python
assert_raises(UnicodeError, np.load, path, allow_pickle=True)
```

### Step 20: Call assert_raises()

```python
assert_raises(ImportError, np.load, path, allow_pickle=True, fix_imports=False, encoding='latin1')
```


## Complete Example

```python
# Workflow
data_dir = os.path.join(os.path.dirname(__file__), 'data')
expected = np.array([None, range, '優良', b'\xe4\xb8\x8d\xe8\x89\xaf'], dtype=object)
for fname in ['py2-np0-objarr.npy', 'py2-objarr.npy', 'py2-objarr.npz', 'py3-objarr.npy', 'py3-objarr.npz']:
    path = os.path.join(data_dir, fname)
    for encoding in ['bytes', 'latin1']:
        data_f = np.load(path, allow_pickle=True, encoding=encoding)
        if fname.endswith('.npz'):
            data = data_f['x']
            data_f.close()
        else:
            data = data_f
        if encoding == 'latin1' and fname.startswith('py2'):
            assert_(isinstance(data[3], str))
            assert_array_equal(data[:-1], expected[:-1])
            assert_array_equal(data[-1].encode(encoding), expected[-1])
        else:
            assert_(isinstance(data[3], bytes))
            assert_array_equal(data, expected)
    if fname.startswith('py2'):
        if fname.endswith('.npz'):
            data = np.load(path, allow_pickle=True)
            assert_raises(UnicodeError, data.__getitem__, 'x')
            data.close()
            data = np.load(path, allow_pickle=True, fix_imports=False, encoding='latin1')
            assert_raises(ImportError, data.__getitem__, 'x')
            data.close()
        else:
            assert_raises(UnicodeError, np.load, path, allow_pickle=True)
            assert_raises(ImportError, np.load, path, allow_pickle=True, fix_imports=False, encoding='latin1')
```

## Next Steps


---

*Source: test_format.py:567 | Complexity: Advanced | Last updated: 2026-06-02*