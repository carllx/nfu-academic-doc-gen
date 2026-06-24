# How To: With Sign

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test with sign

## Prerequisites

**Required Modules:**
- `gc`
- `sys`
- `textwrap`
- `pytest`
- `hypothesis`
- `hypothesis.extra`
- `numpy`
- `numpy._core.arrayprint`
- `numpy.testing`
- `numpy.testing._private.utils`


## Step-by-Step Guide

### Step 1: Assign a = np.array(...)

```python
a = np.array([-2, 0, 3])
```

**Verification:**
```python
assert_equal(np.array2string(a, sign='+'), '[-2 +0 +3]')
```

### Step 2: Call assert_equal()

```python
assert_equal(np.array2string(a, sign='+'), '[-2 +0 +3]')
```

**Verification:**
```python
assert_equal(np.array2string(a, sign='-'), '[-2  0  3]')
```

### Step 3: Call assert_equal()

```python
assert_equal(np.array2string(a, sign='-'), '[-2  0  3]')
```

**Verification:**
```python
assert_equal(np.array2string(a, sign=' '), '[-2  0  3]')
```

### Step 4: Call assert_equal()

```python
assert_equal(np.array2string(a, sign=' '), '[-2  0  3]')
```

**Verification:**
```python
assert_equal(np.array2string(a, sign='+'), '[+2 +0 +3]')
```

### Step 5: Assign a = np.array(...)

```python
a = np.array([2, 0, 3])
```

**Verification:**
```python
assert_equal(np.array2string(a, sign='-'), '[2 0 3]')
```

### Step 6: Call assert_equal()

```python
assert_equal(np.array2string(a, sign='+'), '[+2 +0 +3]')
```

**Verification:**
```python
assert_equal(np.array2string(a, sign=' '), '[ 2  0  3]')
```

### Step 7: Call assert_equal()

```python
assert_equal(np.array2string(a, sign='-'), '[2 0 3]')
```

**Verification:**
```python
assert_equal(np.array2string(a, sign='+'), '[-2 -1 -3]')
```

### Step 8: Call assert_equal()

```python
assert_equal(np.array2string(a, sign=' '), '[ 2  0  3]')
```

**Verification:**
```python
assert_equal(np.array2string(a, sign='-'), '[-2 -1 -3]')
```

### Step 9: Assign a = np.array(...)

```python
a = np.array([-2, -1, -3])
```

**Verification:**
```python
assert_equal(np.array2string(a, sign=' '), '[-2 -1 -3]')
```

### Step 10: Call assert_equal()

```python
assert_equal(np.array2string(a, sign='+'), '[-2 -1 -3]')
```

**Verification:**
```python
assert_equal(np.array2string(a, sign='+'), '[[+10  -1  +1  +1]\n [+10 +10 +10 +10]]')
```

### Step 11: Call assert_equal()

```python
assert_equal(np.array2string(a, sign='-'), '[-2 -1 -3]')
```

**Verification:**
```python
assert_equal(np.array2string(a, sign='-'), '[[10 -1  1  1]\n [10 10 10 10]]')
```

### Step 12: Call assert_equal()

```python
assert_equal(np.array2string(a, sign=' '), '[-2 -1 -3]')
```

**Verification:**
```python
assert_equal(np.array2string(a, sign=' '), '[[10 -1  1  1]\n [10 10 10 10]]')
```

### Step 13: Assign a = np.array(...)

```python
a = np.array([[10, -1, 1, 1], [10, 10, 10, 10]])
```

**Verification:**
```python
assert_equal(np.array2string(a, sign='+'), '[[+10  +0  +1  +1]\n [+10 +10 +10 +10]]')
```

### Step 14: Call assert_equal()

```python
assert_equal(np.array2string(a, sign='+'), '[[+10  -1  +1  +1]\n [+10 +10 +10 +10]]')
```

**Verification:**
```python
assert_equal(np.array2string(a, sign='-'), '[[10  0  1  1]\n [10 10 10 10]]')
```

### Step 15: Call assert_equal()

```python
assert_equal(np.array2string(a, sign='-'), '[[10 -1  1  1]\n [10 10 10 10]]')
```

**Verification:**
```python
assert_equal(np.array2string(a, sign=' '), '[[ 10   0   1   1]\n [ 10  10  10  10]]')
```

### Step 16: Call assert_equal()

```python
assert_equal(np.array2string(a, sign=' '), '[[10 -1  1  1]\n [10 10 10 10]]')
```

**Verification:**
```python
assert_equal(np.array2string(a, sign='+'), '[[-10  -1  -1  -1]\n [-10 -10 -10 -10]]')
```

### Step 17: Assign a = np.array(...)

```python
a = np.array([[10, 0, 1, 1], [10, 10, 10, 10]])
```

**Verification:**
```python
assert_equal(np.array2string(a, sign='-'), '[[-10  -1  -1  -1]\n [-10 -10 -10 -10]]')
```

### Step 18: Call assert_equal()

```python
assert_equal(np.array2string(a, sign='+'), '[[+10  +0  +1  +1]\n [+10 +10 +10 +10]]')
```

**Verification:**
```python
assert_equal(np.array2string(a, sign=' '), '[[-10  -1  -1  -1]\n [-10 -10 -10 -10]]')
```

### Step 19: Call assert_equal()

```python
assert_equal(np.array2string(a, sign='-'), '[[10  0  1  1]\n [10 10 10 10]]')
```

### Step 20: Call assert_equal()

```python
assert_equal(np.array2string(a, sign=' '), '[[ 10   0   1   1]\n [ 10  10  10  10]]')
```

### Step 21: Assign a = np.array(...)

```python
a = np.array([[-10, -1, -1, -1], [-10, -10, -10, -10]])
```

### Step 22: Call assert_equal()

```python
assert_equal(np.array2string(a, sign='+'), '[[-10  -1  -1  -1]\n [-10 -10 -10 -10]]')
```

### Step 23: Call assert_equal()

```python
assert_equal(np.array2string(a, sign='-'), '[[-10  -1  -1  -1]\n [-10 -10 -10 -10]]')
```

### Step 24: Call assert_equal()

```python
assert_equal(np.array2string(a, sign=' '), '[[-10  -1  -1  -1]\n [-10 -10 -10 -10]]')
```


## Complete Example

```python
# Workflow
a = np.array([-2, 0, 3])
assert_equal(np.array2string(a, sign='+'), '[-2 +0 +3]')
assert_equal(np.array2string(a, sign='-'), '[-2  0  3]')
assert_equal(np.array2string(a, sign=' '), '[-2  0  3]')
a = np.array([2, 0, 3])
assert_equal(np.array2string(a, sign='+'), '[+2 +0 +3]')
assert_equal(np.array2string(a, sign='-'), '[2 0 3]')
assert_equal(np.array2string(a, sign=' '), '[ 2  0  3]')
a = np.array([-2, -1, -3])
assert_equal(np.array2string(a, sign='+'), '[-2 -1 -3]')
assert_equal(np.array2string(a, sign='-'), '[-2 -1 -3]')
assert_equal(np.array2string(a, sign=' '), '[-2 -1 -3]')
a = np.array([[10, -1, 1, 1], [10, 10, 10, 10]])
assert_equal(np.array2string(a, sign='+'), '[[+10  -1  +1  +1]\n [+10 +10 +10 +10]]')
assert_equal(np.array2string(a, sign='-'), '[[10 -1  1  1]\n [10 10 10 10]]')
assert_equal(np.array2string(a, sign=' '), '[[10 -1  1  1]\n [10 10 10 10]]')
a = np.array([[10, 0, 1, 1], [10, 10, 10, 10]])
assert_equal(np.array2string(a, sign='+'), '[[+10  +0  +1  +1]\n [+10 +10 +10 +10]]')
assert_equal(np.array2string(a, sign='-'), '[[10  0  1  1]\n [10 10 10 10]]')
assert_equal(np.array2string(a, sign=' '), '[[ 10   0   1   1]\n [ 10  10  10  10]]')
a = np.array([[-10, -1, -1, -1], [-10, -10, -10, -10]])
assert_equal(np.array2string(a, sign='+'), '[[-10  -1  -1  -1]\n [-10 -10 -10 -10]]')
assert_equal(np.array2string(a, sign='-'), '[[-10  -1  -1  -1]\n [-10 -10 -10 -10]]')
assert_equal(np.array2string(a, sign=' '), '[[-10  -1  -1  -1]\n [-10 -10 -10 -10]]')
```

## Next Steps


---

*Source: test_arrayprint.py:563 | Complexity: Advanced | Last updated: 2026-06-02*