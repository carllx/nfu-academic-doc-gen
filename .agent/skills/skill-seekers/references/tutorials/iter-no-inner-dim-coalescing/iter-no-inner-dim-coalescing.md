# How To: Iter No Inner Dim Coalescing

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test iter no inner dim coalescing

## Prerequisites

**Required Modules:**
- `inspect`
- `subprocess`
- `sys`
- `textwrap`
- `warnings`
- `pytest`
- `numpy`
- `numpy._core._multiarray_tests`
- `numpy._core.umath`
- `numpy`
- `numpy.testing`
- `numpy.testing._private.utils`


## Step-by-Step Guide

### Step 1: Assign a = value

```python
a = arange(24).reshape(2, 3, 4)[:, :, :-1]
```

**Verification:**
```python
assert_equal(i.ndim, 2)
```

### Step 2: Assign i = nditer(...)

```python
i = nditer(a, ['external_loop'], [['readonly']])
```

**Verification:**
```python
assert_equal(i[0].shape, (3,))
```

### Step 3: Call assert_equal()

```python
assert_equal(i.ndim, 2)
```

**Verification:**
```python
assert_equal(i.ndim, 2)
```

### Step 4: Call assert_equal()

```python
assert_equal(i[0].shape, (3,))
```

**Verification:**
```python
assert_equal(i[0].shape, (8,))
```

### Step 5: Assign a = value

```python
a = arange(24).reshape(2, 3, 4)[:, :-1, :]
```

**Verification:**
```python
assert_equal(i.ndim, 1)
```

### Step 6: Assign i = nditer(...)

```python
i = nditer(a, ['external_loop'], [['readonly']])
```

**Verification:**
```python
assert_equal(i[0].shape, (12,))
```

### Step 7: Call assert_equal()

```python
assert_equal(i.ndim, 2)
```

**Verification:**
```python
assert_equal(i.ndim, 1)
```

### Step 8: Call assert_equal()

```python
assert_equal(i[0].shape, (8,))
```

**Verification:**
```python
assert_equal(i[0].shape, (24,))
```

### Step 9: Assign a = value

```python
a = arange(24).reshape(2, 3, 4)[:-1, :, :]
```

### Step 10: Assign i = nditer(...)

```python
i = nditer(a, ['external_loop'], [['readonly']])
```

### Step 11: Call assert_equal()

```python
assert_equal(i.ndim, 1)
```

### Step 12: Call assert_equal()

```python
assert_equal(i[0].shape, (12,))
```

### Step 13: Assign a = arange.reshape(...)

```python
a = arange(24).reshape(1, 1, 2, 1, 1, 3, 1, 1, 4, 1, 1)
```

### Step 14: Assign i = nditer(...)

```python
i = nditer(a, ['external_loop'], [['readonly']])
```

### Step 15: Call assert_equal()

```python
assert_equal(i.ndim, 1)
```

### Step 16: Call assert_equal()

```python
assert_equal(i[0].shape, (24,))
```


## Complete Example

```python
# Workflow
a = arange(24).reshape(2, 3, 4)[:, :, :-1]
i = nditer(a, ['external_loop'], [['readonly']])
assert_equal(i.ndim, 2)
assert_equal(i[0].shape, (3,))
a = arange(24).reshape(2, 3, 4)[:, :-1, :]
i = nditer(a, ['external_loop'], [['readonly']])
assert_equal(i.ndim, 2)
assert_equal(i[0].shape, (8,))
a = arange(24).reshape(2, 3, 4)[:-1, :, :]
i = nditer(a, ['external_loop'], [['readonly']])
assert_equal(i.ndim, 1)
assert_equal(i[0].shape, (12,))
a = arange(24).reshape(1, 1, 2, 1, 1, 3, 1, 1, 4, 1, 1)
i = nditer(a, ['external_loop'], [['readonly']])
assert_equal(i.ndim, 1)
assert_equal(i[0].shape, (24,))
```

## Next Steps


---

*Source: test_nditer.py:487 | Complexity: Advanced | Last updated: 2026-06-02*