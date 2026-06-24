# How To: Fix

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fix

## Prerequisites

**Required Modules:**
- `numpy`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign a = np.array(...)

```python
a = np.array([[1.0, 1.1, 1.5, 1.8], [-1.0, -1.1, -1.5, -1.8]])
```

**Verification:**
```python
assert_equal(res, tgt)
```

### Step 2: Assign out = np.zeros(...)

```python
out = np.zeros(a.shape, float)
```

**Verification:**
```python
assert_equal(res, tgt)
```

### Step 3: Assign tgt = np.array(...)

```python
tgt = np.array([[1.0, 1.0, 1.0, 1.0], [-1.0, -1.0, -1.0, -1.0]])
```

**Verification:**
```python
assert_equal(out, tgt)
```

### Step 4: Assign res = fix(...)

```python
res = fix(a)
```

**Verification:**
```python
assert_equal(fix(3.14), 3)
```

### Step 5: Call assert_equal()

```python
assert_equal(res, tgt)
```

### Step 6: Assign res = fix(...)

```python
res = fix(a, out)
```

### Step 7: Call assert_equal()

```python
assert_equal(res, tgt)
```

### Step 8: Call assert_equal()

```python
assert_equal(out, tgt)
```

### Step 9: Call assert_equal()

```python
assert_equal(fix(3.14), 3)
```


## Complete Example

```python
# Workflow
a = np.array([[1.0, 1.1, 1.5, 1.8], [-1.0, -1.1, -1.5, -1.8]])
out = np.zeros(a.shape, float)
tgt = np.array([[1.0, 1.0, 1.0, 1.0], [-1.0, -1.0, -1.0, -1.0]])
res = fix(a)
assert_equal(res, tgt)
res = fix(a, out)
assert_equal(res, tgt)
assert_equal(out, tgt)
assert_equal(fix(3.14), 3)
```

## Next Steps


---

*Source: test_ufunclike.py:38 | Complexity: Advanced | Last updated: 2026-06-02*