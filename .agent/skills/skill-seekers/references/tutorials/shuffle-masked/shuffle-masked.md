# How To: Shuffle Masked

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test shuffle masked

## Prerequisites

**Required Modules:**
- `sys`
- `warnings`
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`
- `hashlib`
- `threading`


## Step-by-Step Guide

### Step 1: Assign a = np.ma.masked_values(...)

```python
a = np.ma.masked_values(np.reshape(range(20), (5, 4)) % 3 - 1, -1)
```

**Verification:**
```python
assert_equal(sorted(a.data[~a.mask]), sorted(a_orig.data[~a_orig.mask]))
```

### Step 2: Assign b = np.ma.masked_values(...)

```python
b = np.ma.masked_values(np.arange(20) % 3 - 1, -1)
```

**Verification:**
```python
assert_equal(sorted(b.data[~b.mask]), sorted(b_orig.data[~b_orig.mask]))
```

### Step 3: Assign a_orig = a.copy(...)

```python
a_orig = a.copy()
```

### Step 4: Assign b_orig = b.copy(...)

```python
b_orig = b.copy()
```

### Step 5: Call np.random.shuffle()

```python
np.random.shuffle(a)
```

### Step 6: Call assert_equal()

```python
assert_equal(sorted(a.data[~a.mask]), sorted(a_orig.data[~a_orig.mask]))
```

### Step 7: Call np.random.shuffle()

```python
np.random.shuffle(b)
```

### Step 8: Call assert_equal()

```python
assert_equal(sorted(b.data[~b.mask]), sorted(b_orig.data[~b_orig.mask]))
```


## Complete Example

```python
# Workflow
a = np.ma.masked_values(np.reshape(range(20), (5, 4)) % 3 - 1, -1)
b = np.ma.masked_values(np.arange(20) % 3 - 1, -1)
a_orig = a.copy()
b_orig = b.copy()
for i in range(50):
    np.random.shuffle(a)
    assert_equal(sorted(a.data[~a.mask]), sorted(a_orig.data[~a_orig.mask]))
    np.random.shuffle(b)
    assert_equal(sorted(b.data[~b.mask]), sorted(b_orig.data[~b_orig.mask]))
```

## Next Steps


---

*Source: test_random.py:514 | Complexity: Advanced | Last updated: 2026-06-02*