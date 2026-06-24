# How To: Loadtxt Fields Subarrays

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test loadtxt fields subarrays

## Prerequisites

**Required Modules:**
- `os`
- `numpy`
- `numpy.testing`
- `numpy.lib.recfunctions`
- `io`


## Step-by-Step Guide

### Step 1: Assign dt = value

```python
dt = [('a', 'u1', 2), ('b', 'u1', 2)]
```

**Verification:**
```python
assert_equal(x, np.array([((0, 1), (2, 3))], dtype=dt))
```

### Step 2: Assign x = np.loadtxt(...)

```python
x = np.loadtxt(StringIO('0 1 2 3'), dtype=dt)
```

**Verification:**
```python
assert_equal(x, np.array([(((0, 1, 2), 3),)], dtype=dt))
```

### Step 3: Call assert_equal()

```python
assert_equal(x, np.array([((0, 1), (2, 3))], dtype=dt))
```

**Verification:**
```python
assert_equal(x, np.array([(((0, 1), (2, 3)),)], dtype=dt))
```

### Step 4: Assign dt = value

```python
dt = [('a', [('a', 'u1', (1, 3)), ('b', 'u1')])]
```

**Verification:**
```python
assert_equal(x, np.array(data, dtype=dt))
```

### Step 5: Assign x = np.loadtxt(...)

```python
x = np.loadtxt(StringIO('0 1 2 3'), dtype=dt)
```

### Step 6: Call assert_equal()

```python
assert_equal(x, np.array([(((0, 1, 2), 3),)], dtype=dt))
```

### Step 7: Assign dt = value

```python
dt = [('a', 'u1', (2, 2))]
```

### Step 8: Assign x = np.loadtxt(...)

```python
x = np.loadtxt(StringIO('0 1 2 3'), dtype=dt)
```

### Step 9: Call assert_equal()

```python
assert_equal(x, np.array([(((0, 1), (2, 3)),)], dtype=dt))
```

### Step 10: Assign dt = value

```python
dt = [('a', 'u1', (2, 3, 2))]
```

### Step 11: Assign x = np.loadtxt(...)

```python
x = np.loadtxt(StringIO('0 1 2 3 4 5 6 7 8 9 10 11'), dtype=dt)
```

### Step 12: Assign data = value

```python
data = [((((0, 1), (2, 3), (4, 5)), ((6, 7), (8, 9), (10, 11))),)]
```

### Step 13: Call assert_equal()

```python
assert_equal(x, np.array(data, dtype=dt))
```


## Complete Example

```python
# Workflow
from io import StringIO
dt = [('a', 'u1', 2), ('b', 'u1', 2)]
x = np.loadtxt(StringIO('0 1 2 3'), dtype=dt)
assert_equal(x, np.array([((0, 1), (2, 3))], dtype=dt))
dt = [('a', [('a', 'u1', (1, 3)), ('b', 'u1')])]
x = np.loadtxt(StringIO('0 1 2 3'), dtype=dt)
assert_equal(x, np.array([(((0, 1, 2), 3),)], dtype=dt))
dt = [('a', 'u1', (2, 2))]
x = np.loadtxt(StringIO('0 1 2 3'), dtype=dt)
assert_equal(x, np.array([(((0, 1), (2, 3)),)], dtype=dt))
dt = [('a', 'u1', (2, 3, 2))]
x = np.loadtxt(StringIO('0 1 2 3 4 5 6 7 8 9 10 11'), dtype=dt)
data = [((((0, 1), (2, 3), (4, 5)), ((6, 7), (8, 9), (10, 11))),)]
assert_equal(x, np.array(data, dtype=dt))
```

## Next Steps


---

*Source: test_regression.py:189 | Complexity: Advanced | Last updated: 2026-06-02*