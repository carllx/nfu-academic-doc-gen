# How To: Einsum Fixedstridebug

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test einsum fixedstridebug

## Prerequisites

**Required Modules:**
- `itertools`
- `warnings`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign A = np.arange.reshape.astype(...)

```python
A = np.arange(2 * 3).reshape(2, 3).astype(np.float32)
```

**Verification:**
```python
assert_equal(es, tp)
```

### Step 2: Assign B = np.arange.reshape.astype(...)

```python
B = np.arange(2 * 3 * 2731).reshape(2, 3, 2731).astype(np.int16)
```

**Verification:**
```python
assert_equal(es, tp)
```

### Step 3: Assign es = np.einsum(...)

```python
es = np.einsum('cl, cpx->lpx', A, B)
```

### Step 4: Assign tp = np.tensordot(...)

```python
tp = np.tensordot(A, B, axes=(0, 0))
```

### Step 5: Call assert_equal()

```python
assert_equal(es, tp)
```

### Step 6: Assign A = np.arange.reshape.astype(...)

```python
A = np.arange(3 * 3).reshape(3, 3).astype(np.float64)
```

### Step 7: Assign B = np.arange.reshape.astype(...)

```python
B = np.arange(3 * 3 * 64 * 64).reshape(3, 3, 64, 64).astype(np.float32)
```

### Step 8: Assign es = np.einsum(...)

```python
es = np.einsum('cl, cpxy->lpxy', A, B)
```

### Step 9: Assign tp = np.tensordot(...)

```python
tp = np.tensordot(A, B, axes=(0, 0))
```

### Step 10: Call assert_equal()

```python
assert_equal(es, tp)
```


## Complete Example

```python
# Workflow
A = np.arange(2 * 3).reshape(2, 3).astype(np.float32)
B = np.arange(2 * 3 * 2731).reshape(2, 3, 2731).astype(np.int16)
es = np.einsum('cl, cpx->lpx', A, B)
tp = np.tensordot(A, B, axes=(0, 0))
assert_equal(es, tp)
A = np.arange(3 * 3).reshape(3, 3).astype(np.float64)
B = np.arange(3 * 3 * 64 * 64).reshape(3, 3, 64, 64).astype(np.float32)
es = np.einsum('cl, cpxy->lpxy', A, B)
tp = np.tensordot(A, B, axes=(0, 0))
assert_equal(es, tp)
```

## Next Steps


---

*Source: test_einsum.py:833 | Complexity: Advanced | Last updated: 2026-06-02*