# How To: Replace Count And Size

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test replace count and size

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy._core.multiarray`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign a = np.array.view(...)

```python
a = np.array(['0123456789' * i for i in range(4)]).view(np.char.chararray)
```

**Verification:**
```python
assert r1.dtype.itemsize == (3 * 10 + 3 * 4) * 4
```

### Step 2: Assign r1 = a.replace(...)

```python
r1 = a.replace('5', 'ABCDE')
```

**Verification:**
```python
assert_array_equal(r1, np.array(['01234ABCDE6789' * i for i in range(4)]))
```

### Step 3: Call assert_array_equal()

```python
assert_array_equal(r1, np.array(['01234ABCDE6789' * i for i in range(4)]))
```

**Verification:**
```python
assert r2.dtype.itemsize == (3 * 10 + 4) * 4
```

### Step 4: Assign r2 = a.replace(...)

```python
r2 = a.replace('5', 'ABCDE', count=1)
```

**Verification:**
```python
assert r3.dtype.itemsize == a.dtype.itemsize
```

### Step 5: Assign r3 = a.replace(...)

```python
r3 = a.replace('5', 'ABCDE', count=0)
```

**Verification:**
```python
assert_array_equal(r3, a)
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(r3, a)
```

**Verification:**
```python
assert r4.dtype.itemsize == (3 * 10 + 3 * 4) * 4
```

### Step 7: Assign r4 = a.replace(...)

```python
r4 = a.replace('5', 'ABCDE', count=-1)
```

**Verification:**
```python
assert_array_equal(r4, r1)
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(r4, r1)
```

**Verification:**
```python
assert r5.dtype.itemsize == (3 * 10 + 4) * 4
```

### Step 9: Assign r5 = a.replace(...)

```python
r5 = a.replace('5', 'ABCDE', count=[-1, -1, -1, 1])
```

**Verification:**
```python
assert_array_equal(r5, np.array(['01234ABCDE6789' * i for i in range(3)] + ['01234ABCDE6789' + '0123456789' * 2]))
```

### Step 10: Call assert_array_equal()

```python
assert_array_equal(r5, np.array(['01234ABCDE6789' * i for i in range(3)] + ['01234ABCDE6789' + '0123456789' * 2]))
```


## Complete Example

```python
# Workflow
a = np.array(['0123456789' * i for i in range(4)]).view(np.char.chararray)
r1 = a.replace('5', 'ABCDE')
assert r1.dtype.itemsize == (3 * 10 + 3 * 4) * 4
assert_array_equal(r1, np.array(['01234ABCDE6789' * i for i in range(4)]))
r2 = a.replace('5', 'ABCDE', count=1)
assert r2.dtype.itemsize == (3 * 10 + 4) * 4
r3 = a.replace('5', 'ABCDE', count=0)
assert r3.dtype.itemsize == a.dtype.itemsize
assert_array_equal(r3, a)
r4 = a.replace('5', 'ABCDE', count=-1)
assert r4.dtype.itemsize == (3 * 10 + 3 * 4) * 4
assert_array_equal(r4, r1)
r5 = a.replace('5', 'ABCDE', count=[-1, -1, -1, 1])
assert r5.dtype.itemsize == (3 * 10 + 4) * 4
assert_array_equal(r5, np.array(['01234ABCDE6789' * i for i in range(3)] + ['01234ABCDE6789' + '0123456789' * 2]))
```

## Next Steps


---

*Source: test_defchararray.py:500 | Complexity: Advanced | Last updated: 2026-06-02*