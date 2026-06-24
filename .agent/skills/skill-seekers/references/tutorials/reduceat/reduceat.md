# How To: Reduceat

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test bug in reduceat when structured arrays are not copied.

## Prerequisites

**Required Modules:**
- `fnmatch`
- `inspect`
- `itertools`
- `operator`
- `platform`
- `sys`
- `warnings`
- `collections`
- `fractions`
- `functools`
- `pytest`
- `numpy`
- `numpy._core.umath`
- `numpy._core`
- `numpy.testing`
- `numpy.testing._private.utils`
- `operator`
- `platform`
- `decimal`
- `cmath`


## Step-by-Step Guide

### Step 1: 'Test bug in reduceat when structured arrays are not copied.'

```python
'Test bug in reduceat when structured arrays are not copied.'
```

**Verification:**
```python
assert_array_almost_equal(h1, h2)
```

### Step 2: Assign db = np.dtype(...)

```python
db = np.dtype([('name', 'S11'), ('time', np.int64), ('value', np.float32)])
```

**Verification:**
```python
assert_array_almost_equal(h1, h2)
```

### Step 3: Assign a = np.empty(...)

```python
a = np.empty([100], dtype=db)
```

### Step 4: Assign unknown = 'Simple'

```python
a['name'] = 'Simple'
```

### Step 5: Assign unknown = 10

```python
a['time'] = 10
```

### Step 6: Assign unknown = 100

```python
a['value'] = 100
```

### Step 7: Assign indx = value

```python
indx = [0, 7, 15, 25]
```

### Step 8: Assign h2 = value

```python
h2 = []
```

### Step 9: Assign val1 = value

```python
val1 = indx[0]
```

### Step 10: Call h2.append()

```python
h2.append(np.add.reduce(a['value'][val1:]))
```

### Step 11: Assign h2 = np.array(...)

```python
h2 = np.array(h2)
```

### Step 12: Assign h1 = np.add.reduceat(...)

```python
h1 = np.add.reduceat(a['value'], indx)
```

### Step 13: Call assert_array_almost_equal()

```python
assert_array_almost_equal(h1, h2)
```

### Step 14: Call np.setbufsize()

```python
np.setbufsize(32)
```

### Step 15: Assign h1 = np.add.reduceat(...)

```python
h1 = np.add.reduceat(a['value'], indx)
```

### Step 16: Call np.setbufsize()

```python
np.setbufsize(ncu.UFUNC_BUFSIZE_DEFAULT)
```

### Step 17: Call assert_array_almost_equal()

```python
assert_array_almost_equal(h1, h2)
```

### Step 18: Call h2.append()

```python
h2.append(np.add.reduce(a['value'][val1:val2]))
```

### Step 19: Assign val1 = val2

```python
val1 = val2
```


## Complete Example

```python
# Workflow
'Test bug in reduceat when structured arrays are not copied.'
db = np.dtype([('name', 'S11'), ('time', np.int64), ('value', np.float32)])
a = np.empty([100], dtype=db)
a['name'] = 'Simple'
a['time'] = 10
a['value'] = 100
indx = [0, 7, 15, 25]
h2 = []
val1 = indx[0]
for val2 in indx[1:]:
    h2.append(np.add.reduce(a['value'][val1:val2]))
    val1 = val2
h2.append(np.add.reduce(a['value'][val1:]))
h2 = np.array(h2)
h1 = np.add.reduceat(a['value'], indx)
assert_array_almost_equal(h1, h2)
np.setbufsize(32)
h1 = np.add.reduceat(a['value'], indx)
np.setbufsize(ncu.UFUNC_BUFSIZE_DEFAULT)
assert_array_almost_equal(h1, h2)
```

## Next Steps


---

*Source: test_umath.py:4695 | Complexity: Advanced | Last updated: 2026-06-02*