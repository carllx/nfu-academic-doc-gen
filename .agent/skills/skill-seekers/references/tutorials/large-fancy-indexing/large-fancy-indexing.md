# How To: Large Fancy Indexing

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test large fancy indexing

## Prerequisites

**Required Modules:**
- `os`
- `numpy`
- `numpy.testing`
- `numpy.lib.recfunctions`
- `io`


## Step-by-Step Guide

### Step 1: Assign nbits = value

```python
nbits = np.dtype(np.intp).itemsize * 8
```

**Verification:**
```python
assert_raises(ValueError, dp)
```

### Step 2: Assign thesize = int(...)

```python
thesize = int((2 ** nbits) ** (1.0 / 5.0) + 1)
```

**Verification:**
```python
assert_raises(ValueError, dp2)
```

### Step 3: Call assert_raises()

```python
assert_raises(ValueError, dp)
```

### Step 4: Call assert_raises()

```python
assert_raises(ValueError, dp2)
```

### Step 5: Assign n = 3

```python
n = 3
```

### Step 6: Assign a = np.ones(...)

```python
a = np.ones((n,) * 5)
```

### Step 7: Assign i = np.random.randint(...)

```python
i = np.random.randint(0, n, size=thesize)
```

### Step 8: Assign unknown = 0

```python
a[np.ix_(i, i, i, i, i)] = 0
```

### Step 9: Assign n = 3

```python
n = 3
```

### Step 10: Assign a = np.ones(...)

```python
a = np.ones((n,) * 5)
```

### Step 11: Assign i = np.random.randint(...)

```python
i = np.random.randint(0, n, size=thesize)
```

### Step 12: a[np.ix_(i, i, i, i, i)]

```python
a[np.ix_(i, i, i, i, i)]
```


## Complete Example

```python
# Workflow
nbits = np.dtype(np.intp).itemsize * 8
thesize = int((2 ** nbits) ** (1.0 / 5.0) + 1)

def dp():
    n = 3
    a = np.ones((n,) * 5)
    i = np.random.randint(0, n, size=thesize)
    a[np.ix_(i, i, i, i, i)] = 0

def dp2():
    n = 3
    a = np.ones((n,) * 5)
    i = np.random.randint(0, n, size=thesize)
    a[np.ix_(i, i, i, i, i)]
assert_raises(ValueError, dp)
assert_raises(ValueError, dp2)
```

## Next Steps


---

*Source: test_regression.py:135 | Complexity: Advanced | Last updated: 2026-06-02*