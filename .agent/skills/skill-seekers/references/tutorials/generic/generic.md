# How To: Generic

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test generic

## Prerequisites

**Required Modules:**
- `numpy`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: assert_all(vals[0] < -10000000000.0) and assert_all(np.isfinite(vals[0]))

```python
assert_all(vals[0] < -10000000000.0) and assert_all(np.isfinite(vals[0]))
```

**Verification:**
```python
assert_all(vals[0] < -10000000000.0) and assert_all(np.isfinite(vals[0]))
```

### Step 2: Call assert_()

```python
assert_(vals[1] == 0)
```

**Verification:**
```python
assert_(vals[1] == 0)
```

### Step 3: assert_all(vals[2] > 10000000000.0) and assert_all(np.isfinite(vals[2]))

```python
assert_all(vals[2] > 10000000000.0) and assert_all(np.isfinite(vals[2]))
```

**Verification:**
```python
assert_all(vals[2] > 10000000000.0) and assert_all(np.isfinite(vals[2]))
```

### Step 4: Call assert_equal()

```python
assert_equal(type(vals), np.ndarray)
```

**Verification:**
```python
assert_equal(type(vals), np.ndarray)
```

### Step 5: Call assert_equal()

```python
assert_equal(vals, [30, 10, 20])
```

**Verification:**
```python
assert_equal(vals, [30, 10, 20])
```

### Step 6: Call assert_all()

```python
assert_all(np.isfinite(vals[[0, 2]]))
```

**Verification:**
```python
assert_all(np.isfinite(vals[[0, 2]]))
```

### Step 7: Call assert_equal()

```python
assert_equal(type(vals), np.ndarray)
```

**Verification:**
```python
assert_equal(type(vals), np.ndarray)
```

### Step 8: Assign result = nan_to_num(...)

```python
result = nan_to_num(vals, copy=False)
```

**Verification:**
```python
assert_(result is vals)
```

### Step 9: Call assert_()

```python
assert_(result is vals)
```

**Verification:**
```python
assert_all(vals[0] < -10000000000.0) and assert_all(np.isfinite(vals[0]))
```

### Step 10: assert_all(vals[0] < -10000000000.0) and assert_all(np.isfinite(vals[0]))

```python
assert_all(vals[0] < -10000000000.0) and assert_all(np.isfinite(vals[0]))
```

**Verification:**
```python
assert_(vals[1] == 0)
```

### Step 11: Call assert_()

```python
assert_(vals[1] == 0)
```

**Verification:**
```python
assert_all(vals[2] > 10000000000.0) and assert_all(np.isfinite(vals[2]))
```

### Step 12: assert_all(vals[2] > 10000000000.0) and assert_all(np.isfinite(vals[2]))

```python
assert_all(vals[2] > 10000000000.0) and assert_all(np.isfinite(vals[2]))
```

**Verification:**
```python
assert_equal(type(vals), np.ndarray)
```

### Step 13: Call assert_equal()

```python
assert_equal(type(vals), np.ndarray)
```

**Verification:**
```python
assert_(result is vals)
```

### Step 14: Assign result = nan_to_num(...)

```python
result = nan_to_num(vals, copy=False, nan=10, posinf=20, neginf=30)
```

**Verification:**
```python
assert_equal(vals, [30, 10, 20])
```

### Step 15: Call assert_()

```python
assert_(result is vals)
```

**Verification:**
```python
assert_all(np.isfinite(vals[[0, 2]]))
```

### Step 16: Call assert_equal()

```python
assert_equal(vals, [30, 10, 20])
```

**Verification:**
```python
assert_equal(type(vals), np.ndarray)
```

### Step 17: Call assert_all()

```python
assert_all(np.isfinite(vals[[0, 2]]))
```

### Step 18: Call assert_equal()

```python
assert_equal(type(vals), np.ndarray)
```

### Step 19: Assign vals = nan_to_num(...)

```python
vals = nan_to_num(np.array((-1.0, 0, 1)) / 0.0)
```

### Step 20: Assign vals = nan_to_num(...)

```python
vals = nan_to_num(np.array((-1.0, 0, 1)) / 0.0, nan=10, posinf=20, neginf=30)
```

### Step 21: Assign vals = value

```python
vals = np.array((-1.0, 0, 1)) / 0.0
```

### Step 22: Assign vals = value

```python
vals = np.array((-1.0, 0, 1)) / 0.0
```


## Complete Example

```python
# Workflow
with np.errstate(divide='ignore', invalid='ignore'):
    vals = nan_to_num(np.array((-1.0, 0, 1)) / 0.0)
assert_all(vals[0] < -10000000000.0) and assert_all(np.isfinite(vals[0]))
assert_(vals[1] == 0)
assert_all(vals[2] > 10000000000.0) and assert_all(np.isfinite(vals[2]))
assert_equal(type(vals), np.ndarray)
with np.errstate(divide='ignore', invalid='ignore'):
    vals = nan_to_num(np.array((-1.0, 0, 1)) / 0.0, nan=10, posinf=20, neginf=30)
assert_equal(vals, [30, 10, 20])
assert_all(np.isfinite(vals[[0, 2]]))
assert_equal(type(vals), np.ndarray)
with np.errstate(divide='ignore', invalid='ignore'):
    vals = np.array((-1.0, 0, 1)) / 0.0
result = nan_to_num(vals, copy=False)
assert_(result is vals)
assert_all(vals[0] < -10000000000.0) and assert_all(np.isfinite(vals[0]))
assert_(vals[1] == 0)
assert_all(vals[2] > 10000000000.0) and assert_all(np.isfinite(vals[2]))
assert_equal(type(vals), np.ndarray)
with np.errstate(divide='ignore', invalid='ignore'):
    vals = np.array((-1.0, 0, 1)) / 0.0
result = nan_to_num(vals, copy=False, nan=10, posinf=20, neginf=30)
assert_(result is vals)
assert_equal(vals, [30, 10, 20])
assert_all(np.isfinite(vals[[0, 2]]))
assert_equal(type(vals), np.ndarray)
```

## Next Steps


---

*Source: test_type_check.py:360 | Complexity: Advanced | Last updated: 2026-06-02*