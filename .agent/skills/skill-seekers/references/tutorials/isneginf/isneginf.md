# How To: Isneginf

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test isneginf

## Prerequisites

**Required Modules:**
- `numpy`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign a = np.array(...)

```python
a = np.array([np.inf, -np.inf, np.nan, 0.0, 3.0, -3.0])
```

**Verification:**
```python
assert_equal(res, tgt)
```

### Step 2: Assign out = np.zeros(...)

```python
out = np.zeros(a.shape, bool)
```

**Verification:**
```python
assert_equal(res, tgt)
```

### Step 3: Assign tgt = np.array(...)

```python
tgt = np.array([False, True, False, False, False, False])
```

**Verification:**
```python
assert_equal(out, tgt)
```

### Step 4: Assign res = isneginf(...)

```python
res = isneginf(a)
```

### Step 5: Call assert_equal()

```python
assert_equal(res, tgt)
```

### Step 6: Assign res = isneginf(...)

```python
res = isneginf(a, out)
```

### Step 7: Call assert_equal()

```python
assert_equal(res, tgt)
```

### Step 8: Call assert_equal()

```python
assert_equal(out, tgt)
```

### Step 9: Assign a = a.astype(...)

```python
a = a.astype(np.complex128)
```

### Step 10: Call isneginf()

```python
isneginf(a)
```


## Complete Example

```python
# Workflow
a = np.array([np.inf, -np.inf, np.nan, 0.0, 3.0, -3.0])
out = np.zeros(a.shape, bool)
tgt = np.array([False, True, False, False, False, False])
res = isneginf(a)
assert_equal(res, tgt)
res = isneginf(a, out)
assert_equal(res, tgt)
assert_equal(out, tgt)
a = a.astype(np.complex128)
with assert_raises(TypeError):
    isneginf(a)
```

## Next Steps


---

*Source: test_ufunclike.py:23 | Complexity: Advanced | Last updated: 2026-06-02*