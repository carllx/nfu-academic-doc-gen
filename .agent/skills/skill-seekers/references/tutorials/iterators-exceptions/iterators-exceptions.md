# How To: Iterators Exceptions

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: cases in iterators.c

## Prerequisites

**Required Modules:**
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: 'cases in iterators.c'

```python
'cases in iterators.c'
```

**Verification:**
```python
assert_raises(IndexError, lambda: a[0, 5, None, 2])
```

### Step 2: Assign a = np.zeros(...)

```python
a = np.zeros([1, 2, 3])
```

**Verification:**
```python
assert_raises(IndexError, lambda: a[0, 5, 0, 2])
```

### Step 3: Call assert_raises()

```python
assert_raises(IndexError, lambda: a[0, 5, None, 2])
```

**Verification:**
```python
assert_raises(IndexError, lambda: assign(a, (0, 5, None, 2), 1))
```

### Step 4: Call assert_raises()

```python
assert_raises(IndexError, lambda: a[0, 5, 0, 2])
```

**Verification:**
```python
assert_raises(IndexError, lambda: assign(a, (0, 5, 0, 2), 1))
```

### Step 5: Call assert_raises()

```python
assert_raises(IndexError, lambda: assign(a, (0, 5, None, 2), 1))
```

**Verification:**
```python
assert_raises(IndexError, lambda: a[0, 0, None, 2])
```

### Step 6: Call assert_raises()

```python
assert_raises(IndexError, lambda: assign(a, (0, 5, 0, 2), 1))
```

**Verification:**
```python
assert_raises(IndexError, lambda: assign(a, (0, 0, None, 2), 1))
```

### Step 7: Assign a = np.zeros(...)

```python
a = np.zeros([1, 0, 3])
```

**Verification:**
```python
assert_raises(IndexError, lambda: a.flat[10])
```

### Step 8: Call assert_raises()

```python
assert_raises(IndexError, lambda: a[0, 0, None, 2])
```

**Verification:**
```python
assert_raises(IndexError, lambda: assign(a.flat, 10, 5))
```

### Step 9: Call assert_raises()

```python
assert_raises(IndexError, lambda: assign(a, (0, 0, None, 2), 1))
```

**Verification:**
```python
assert_raises(IndexError, lambda: a.flat[10])
```

### Step 10: Assign a = np.zeros(...)

```python
a = np.zeros([1, 2, 3])
```

**Verification:**
```python
assert_raises(IndexError, lambda: assign(a.flat, 10, 5))
```

### Step 11: Call assert_raises()

```python
assert_raises(IndexError, lambda: a.flat[10])
```

**Verification:**
```python
assert_raises(IndexError, lambda: a.flat[np.array(10)])
```

### Step 12: Call assert_raises()

```python
assert_raises(IndexError, lambda: assign(a.flat, 10, 5))
```

**Verification:**
```python
assert_raises(IndexError, lambda: assign(a.flat, np.array(10), 5))
```

### Step 13: Assign a = np.zeros(...)

```python
a = np.zeros([1, 0, 3])
```

**Verification:**
```python
assert_raises(IndexError, lambda: a.flat[np.array(10)])
```

### Step 14: Call assert_raises()

```python
assert_raises(IndexError, lambda: a.flat[10])
```

**Verification:**
```python
assert_raises(IndexError, lambda: assign(a.flat, np.array(10), 5))
```

### Step 15: Call assert_raises()

```python
assert_raises(IndexError, lambda: assign(a.flat, 10, 5))
```

**Verification:**
```python
assert_raises(IndexError, lambda: a.flat[np.array([10])])
```

### Step 16: Assign a = np.zeros(...)

```python
a = np.zeros([1, 2, 3])
```

**Verification:**
```python
assert_raises(IndexError, lambda: assign(a.flat, np.array([10]), 5))
```

### Step 17: Call assert_raises()

```python
assert_raises(IndexError, lambda: a.flat[np.array(10)])
```

**Verification:**
```python
assert_raises(IndexError, lambda: a.flat[np.array([10])])
```

### Step 18: Call assert_raises()

```python
assert_raises(IndexError, lambda: assign(a.flat, np.array(10), 5))
```

**Verification:**
```python
assert_raises(IndexError, lambda: assign(a.flat, np.array([10]), 5))
```

### Step 19: Assign a = np.zeros(...)

```python
a = np.zeros([1, 0, 3])
```

### Step 20: Call assert_raises()

```python
assert_raises(IndexError, lambda: a.flat[np.array(10)])
```

### Step 21: Call assert_raises()

```python
assert_raises(IndexError, lambda: assign(a.flat, np.array(10), 5))
```

### Step 22: Assign a = np.zeros(...)

```python
a = np.zeros([1, 2, 3])
```

### Step 23: Call assert_raises()

```python
assert_raises(IndexError, lambda: a.flat[np.array([10])])
```

### Step 24: Call assert_raises()

```python
assert_raises(IndexError, lambda: assign(a.flat, np.array([10]), 5))
```

### Step 25: Assign a = np.zeros(...)

```python
a = np.zeros([1, 0, 3])
```

### Step 26: Call assert_raises()

```python
assert_raises(IndexError, lambda: a.flat[np.array([10])])
```

### Step 27: Call assert_raises()

```python
assert_raises(IndexError, lambda: assign(a.flat, np.array([10]), 5))
```

### Step 28: Assign unknown = val

```python
obj[ind] = val
```


## Complete Example

```python
# Workflow
'cases in iterators.c'

def assign(obj, ind, val):
    obj[ind] = val
a = np.zeros([1, 2, 3])
assert_raises(IndexError, lambda: a[0, 5, None, 2])
assert_raises(IndexError, lambda: a[0, 5, 0, 2])
assert_raises(IndexError, lambda: assign(a, (0, 5, None, 2), 1))
assert_raises(IndexError, lambda: assign(a, (0, 5, 0, 2), 1))
a = np.zeros([1, 0, 3])
assert_raises(IndexError, lambda: a[0, 0, None, 2])
assert_raises(IndexError, lambda: assign(a, (0, 0, None, 2), 1))
a = np.zeros([1, 2, 3])
assert_raises(IndexError, lambda: a.flat[10])
assert_raises(IndexError, lambda: assign(a.flat, 10, 5))
a = np.zeros([1, 0, 3])
assert_raises(IndexError, lambda: a.flat[10])
assert_raises(IndexError, lambda: assign(a.flat, 10, 5))
a = np.zeros([1, 2, 3])
assert_raises(IndexError, lambda: a.flat[np.array(10)])
assert_raises(IndexError, lambda: assign(a.flat, np.array(10), 5))
a = np.zeros([1, 0, 3])
assert_raises(IndexError, lambda: a.flat[np.array(10)])
assert_raises(IndexError, lambda: assign(a.flat, np.array(10), 5))
a = np.zeros([1, 2, 3])
assert_raises(IndexError, lambda: a.flat[np.array([10])])
assert_raises(IndexError, lambda: assign(a.flat, np.array([10]), 5))
a = np.zeros([1, 0, 3])
assert_raises(IndexError, lambda: a.flat[np.array([10])])
assert_raises(IndexError, lambda: assign(a.flat, np.array([10]), 5))
```

## Next Steps


---

*Source: test_indexerrors.py:45 | Complexity: Advanced | Last updated: 2026-06-02*