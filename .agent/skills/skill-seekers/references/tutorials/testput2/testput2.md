# How To: Testput2

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test testPut2

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
assert_(x[2] is not masked)
```

### Step 2: Assign x = array(...)

```python
x = array(d, mask=[0, 0, 0, 0, 0])
```

**Verification:**
```python
assert_(x[3] is not masked)
```

### Step 3: Assign z = array(...)

```python
z = array([10, 40], mask=[1, 0])
```

**Verification:**
```python
assert_(x[2] is masked)
```

### Step 4: Call assert_()

```python
assert_(x[2] is not masked)
```

**Verification:**
```python
assert_(x[3] is not masked)
```

### Step 5: Call assert_()

```python
assert_(x[3] is not masked)
```

**Verification:**
```python
assert_(eq(x, [0, 1, 10, 40, 4]))
```

### Step 6: Assign unknown = z

```python
x[2:4] = z
```

**Verification:**
```python
assert_(x[2] is not masked)
```

### Step 7: Call assert_()

```python
assert_(x[2] is masked)
```

**Verification:**
```python
assert_(x[3] is not masked)
```

### Step 8: Call assert_()

```python
assert_(x[3] is not masked)
```

**Verification:**
```python
assert_(y[0] is masked)
```

### Step 9: Call assert_()

```python
assert_(eq(x, [0, 1, 10, 40, 4]))
```

**Verification:**
```python
assert_(y[1] is not masked)
```

### Step 10: Assign d = arange(...)

```python
d = arange(5)
```

**Verification:**
```python
assert_(eq(y, [10, 40]))
```

### Step 11: Assign x = array(...)

```python
x = array(d, mask=[0, 0, 0, 0, 0])
```

**Verification:**
```python
assert_(x[2] is masked)
```

### Step 12: Assign y = value

```python
y = x[2:4]
```

**Verification:**
```python
assert_(x[3] is not masked)
```

### Step 13: Assign z = array(...)

```python
z = array([10, 40], mask=[1, 0])
```

**Verification:**
```python
assert_(eq(x, [0, 1, 10, 40, 4]))
```

### Step 14: Call assert_()

```python
assert_(x[2] is not masked)
```

### Step 15: Call assert_()

```python
assert_(x[3] is not masked)
```

### Step 16: Assign unknown = z

```python
y[:] = z
```

### Step 17: Call assert_()

```python
assert_(y[0] is masked)
```

### Step 18: Call assert_()

```python
assert_(y[1] is not masked)
```

### Step 19: Call assert_()

```python
assert_(eq(y, [10, 40]))
```

### Step 20: Call assert_()

```python
assert_(x[2] is masked)
```

### Step 21: Call assert_()

```python
assert_(x[3] is not masked)
```

### Step 22: Call assert_()

```python
assert_(eq(x, [0, 1, 10, 40, 4]))
```


## Complete Example

```python
# Workflow
d = arange(5)
x = array(d, mask=[0, 0, 0, 0, 0])
z = array([10, 40], mask=[1, 0])
assert_(x[2] is not masked)
assert_(x[3] is not masked)
x[2:4] = z
assert_(x[2] is masked)
assert_(x[3] is not masked)
assert_(eq(x, [0, 1, 10, 40, 4]))
d = arange(5)
x = array(d, mask=[0, 0, 0, 0, 0])
y = x[2:4]
z = array([10, 40], mask=[1, 0])
assert_(x[2] is not masked)
assert_(x[3] is not masked)
y[:] = z
assert_(y[0] is masked)
assert_(y[1] is not masked)
assert_(eq(y, [10, 40]))
assert_(x[2] is masked)
assert_(x[3] is not masked)
assert_(eq(x, [0, 1, 10, 40, 4]))
```

## Next Steps


---

*Source: test_old_ma.py:393 | Complexity: Advanced | Last updated: 2026-06-02*