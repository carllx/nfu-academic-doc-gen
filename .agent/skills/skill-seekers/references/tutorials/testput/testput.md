# How To: Testput

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test testPut

## Prerequisites

**Required Modules:**
- `pickle`
- `functools`
- `pytest`
- `numpy`
- `numpy._core.fromnumeric`
- `numpy._core.umath`
- `numpy.ma`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign d = arange(...)

```python
d = arange(5)
```

**Verification:**
```python
assert_(x[3] is masked)
```

### Step 2: Assign n = value

```python
n = [0, 0, 0, 1, 1]
```

**Verification:**
```python
assert_(x[4] is masked)
```

### Step 3: Assign m = make_mask(...)

```python
m = make_mask(n)
```

**Verification:**
```python
assert_(x._mask is m)
```

### Step 4: Assign m2 = m.copy(...)

```python
m2 = m.copy()
```

**Verification:**
```python
assert_(x[3] is masked)
```

### Step 5: Assign x = array(...)

```python
x = array(d, mask=m)
```

**Verification:**
```python
assert_(x[4] is not masked)
```

### Step 6: Call assert_()

```python
assert_(x[3] is masked)
```

**Verification:**
```python
assert_(eq(x, [0, 10, 2, -1, 40]))
```

### Step 7: Call assert_()

```python
assert_(x[4] is masked)
```

**Verification:**
```python
assert_(x._mask is not m2)
```

### Step 8: Assign unknown = value

```python
x[[1, 4]] = [10, 40]
```

**Verification:**
```python
assert_(x[3] is masked)
```

### Step 9: Call assert_()

```python
assert_(x._mask is m)
```

**Verification:**
```python
assert_(x[4] is masked)
```

### Step 10: Call assert_()

```python
assert_(x[3] is masked)
```

**Verification:**
```python
assert_(eq(x, [-1, 100, 200, 0, 0]))
```

### Step 11: Call assert_()

```python
assert_(x[4] is not masked)
```

### Step 12: Call assert_()

```python
assert_(eq(x, [0, 10, 2, -1, 40]))
```

### Step 13: Assign x = array(...)

```python
x = array(d, mask=m2, copy=True)
```

### Step 14: Call x.put()

```python
x.put([0, 1, 2], [-1, 100, 200])
```

### Step 15: Call assert_()

```python
assert_(x._mask is not m2)
```

### Step 16: Call assert_()

```python
assert_(x[3] is masked)
```

### Step 17: Call assert_()

```python
assert_(x[4] is masked)
```

### Step 18: Call assert_()

```python
assert_(eq(x, [-1, 100, 200, 0, 0]))
```


## Complete Example

```python
# Workflow
d = arange(5)
n = [0, 0, 0, 1, 1]
m = make_mask(n)
m2 = m.copy()
x = array(d, mask=m)
assert_(x[3] is masked)
assert_(x[4] is masked)
x[[1, 4]] = [10, 40]
assert_(x._mask is m)
assert_(x[3] is masked)
assert_(x[4] is not masked)
assert_(eq(x, [0, 10, 2, -1, 40]))
x = array(d, mask=m2, copy=True)
x.put([0, 1, 2], [-1, 100, 200])
assert_(x._mask is not m2)
assert_(x[3] is masked)
assert_(x[4] is masked)
assert_(eq(x, [-1, 100, 200, 0, 0]))
```

## Next Steps


---

*Source: test_old_ma.py:371 | Complexity: Advanced | Last updated: 2026-06-02*