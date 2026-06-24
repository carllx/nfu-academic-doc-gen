# How To: Mapping

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: cases from mapping.c

## Prerequisites

**Required Modules:**
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: 'cases from mapping.c'

```python
'cases from mapping.c'
```

**Verification:**
```python
assert_raises(IndexError, lambda: a[12])
```

### Step 2: Assign a = np.zeros(...)

```python
a = np.zeros((0, 10))
```

**Verification:**
```python
assert_raises(IndexError, lambda: a[10, 20])
```

### Step 3: Call assert_raises()

```python
assert_raises(IndexError, lambda: a[12])
```

**Verification:**
```python
assert_raises(IndexError, lambda: assign(a, (10, 20), 1))
```

### Step 4: Assign a = np.zeros(...)

```python
a = np.zeros((3, 5))
```

**Verification:**
```python
assert_raises(IndexError, lambda: a[1, 0])
```

### Step 5: Call assert_raises()

```python
assert_raises(IndexError, lambda: a[10, 20])
```

**Verification:**
```python
assert_raises(IndexError, lambda: assign(a, (1, 0), 1))
```

### Step 6: Call assert_raises()

```python
assert_raises(IndexError, lambda: assign(a, (10, 20), 1))
```

**Verification:**
```python
assert_raises(IndexError, lambda: assign(a, 10, 1))
```

### Step 7: Assign a = np.zeros(...)

```python
a = np.zeros((3, 0))
```

**Verification:**
```python
assert_raises(IndexError, lambda: assign(a, 10, 1))
```

### Step 8: Call assert_raises()

```python
assert_raises(IndexError, lambda: a[1, 0])
```

**Verification:**
```python
assert_raises(IndexError, lambda: a[1, [1, 20]])
```

### Step 9: Call assert_raises()

```python
assert_raises(IndexError, lambda: assign(a, (1, 0), 1))
```

**Verification:**
```python
assert_raises(IndexError, lambda: assign(a, (1, [1, 20]), 1))
```

### Step 10: Assign a = np.zeros(...)

```python
a = np.zeros((10,))
```

**Verification:**
```python
assert_raises(IndexError, lambda: a[1, [0, 1]])
```

### Step 11: Call assert_raises()

```python
assert_raises(IndexError, lambda: assign(a, 10, 1))
```

**Verification:**
```python
assert_raises(IndexError, lambda: assign(a, (1, [0, 1]), 1))
```

### Step 12: Assign a = np.zeros(...)

```python
a = np.zeros((0,))
```

### Step 13: Call assert_raises()

```python
assert_raises(IndexError, lambda: assign(a, 10, 1))
```

### Step 14: Assign a = np.zeros(...)

```python
a = np.zeros((3, 5))
```

### Step 15: Call assert_raises()

```python
assert_raises(IndexError, lambda: a[1, [1, 20]])
```

### Step 16: Call assert_raises()

```python
assert_raises(IndexError, lambda: assign(a, (1, [1, 20]), 1))
```

### Step 17: Assign a = np.zeros(...)

```python
a = np.zeros((3, 0))
```

### Step 18: Call assert_raises()

```python
assert_raises(IndexError, lambda: a[1, [0, 1]])
```

### Step 19: Call assert_raises()

```python
assert_raises(IndexError, lambda: assign(a, (1, [0, 1]), 1))
```

### Step 20: Assign unknown = val

```python
obj[ind] = val
```


## Complete Example

```python
# Workflow
'cases from mapping.c'

def assign(obj, ind, val):
    obj[ind] = val
a = np.zeros((0, 10))
assert_raises(IndexError, lambda: a[12])
a = np.zeros((3, 5))
assert_raises(IndexError, lambda: a[10, 20])
assert_raises(IndexError, lambda: assign(a, (10, 20), 1))
a = np.zeros((3, 0))
assert_raises(IndexError, lambda: a[1, 0])
assert_raises(IndexError, lambda: assign(a, (1, 0), 1))
a = np.zeros((10,))
assert_raises(IndexError, lambda: assign(a, 10, 1))
a = np.zeros((0,))
assert_raises(IndexError, lambda: assign(a, 10, 1))
a = np.zeros((3, 5))
assert_raises(IndexError, lambda: a[1, [1, 20]])
assert_raises(IndexError, lambda: assign(a, (1, [1, 20]), 1))
a = np.zeros((3, 0))
assert_raises(IndexError, lambda: a[1, [0, 1]])
assert_raises(IndexError, lambda: assign(a, (1, [0, 1]), 1))
```

## Next Steps


---

*Source: test_indexerrors.py:81 | Complexity: Advanced | Last updated: 2026-06-02*