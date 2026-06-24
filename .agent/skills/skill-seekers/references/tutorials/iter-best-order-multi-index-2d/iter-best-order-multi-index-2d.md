# How To: Iter Best Order Multi Index 2D

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test iter best order multi index 2d

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

### Step 1: Assign a = arange(...)

```python
a = arange(6)
```

**Verification:**
```python
assert_equal(iter_multi_index(i), [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)])
```

### Step 2: Assign i = nditer(...)

```python
i = nditer(a.reshape(2, 3), ['multi_index'], [['readonly']])
```

**Verification:**
```python
assert_equal(iter_multi_index(i), [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2)])
```

### Step 3: Call assert_equal()

```python
assert_equal(iter_multi_index(i), [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)])
```

**Verification:**
```python
assert_equal(iter_multi_index(i), [(1, 0), (1, 1), (1, 2), (0, 0), (0, 1), (0, 2)])
```

### Step 4: Assign i = nditer(...)

```python
i = nditer(a.reshape(2, 3).copy(order='F'), ['multi_index'], [['readonly']])
```

**Verification:**
```python
assert_equal(iter_multi_index(i), [(0, 2), (0, 1), (0, 0), (1, 2), (1, 1), (1, 0)])
```

### Step 5: Call assert_equal()

```python
assert_equal(iter_multi_index(i), [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2)])
```

**Verification:**
```python
assert_equal(iter_multi_index(i), [(1, 2), (1, 1), (1, 0), (0, 2), (0, 1), (0, 0)])
```

### Step 6: Assign i = nditer(...)

```python
i = nditer(a.reshape(2, 3)[::-1], ['multi_index'], [['readonly']])
```

**Verification:**
```python
assert_equal(iter_multi_index(i), [(1, 0), (0, 0), (1, 1), (0, 1), (1, 2), (0, 2)])
```

### Step 7: Call assert_equal()

```python
assert_equal(iter_multi_index(i), [(1, 0), (1, 1), (1, 2), (0, 0), (0, 1), (0, 2)])
```

**Verification:**
```python
assert_equal(iter_multi_index(i), [(0, 2), (1, 2), (0, 1), (1, 1), (0, 0), (1, 0)])
```

### Step 8: Assign i = nditer(...)

```python
i = nditer(a.reshape(2, 3)[:, ::-1], ['multi_index'], [['readonly']])
```

**Verification:**
```python
assert_equal(iter_multi_index(i), [(1, 2), (0, 2), (1, 1), (0, 1), (1, 0), (0, 0)])
```

### Step 9: Call assert_equal()

```python
assert_equal(iter_multi_index(i), [(0, 2), (0, 1), (0, 0), (1, 2), (1, 1), (1, 0)])
```

### Step 10: Assign i = nditer(...)

```python
i = nditer(a.reshape(2, 3)[::-1, ::-1], ['multi_index'], [['readonly']])
```

### Step 11: Call assert_equal()

```python
assert_equal(iter_multi_index(i), [(1, 2), (1, 1), (1, 0), (0, 2), (0, 1), (0, 0)])
```

### Step 12: Assign i = nditer(...)

```python
i = nditer(a.reshape(2, 3).copy(order='F')[::-1], ['multi_index'], [['readonly']])
```

### Step 13: Call assert_equal()

```python
assert_equal(iter_multi_index(i), [(1, 0), (0, 0), (1, 1), (0, 1), (1, 2), (0, 2)])
```

### Step 14: Assign i = nditer(...)

```python
i = nditer(a.reshape(2, 3).copy(order='F')[:, ::-1], ['multi_index'], [['readonly']])
```

### Step 15: Call assert_equal()

```python
assert_equal(iter_multi_index(i), [(0, 2), (1, 2), (0, 1), (1, 1), (0, 0), (1, 0)])
```

### Step 16: Assign i = nditer(...)

```python
i = nditer(a.reshape(2, 3).copy(order='F')[::-1, ::-1], ['multi_index'], [['readonly']])
```

### Step 17: Call assert_equal()

```python
assert_equal(iter_multi_index(i), [(1, 2), (0, 2), (1, 1), (0, 1), (1, 0), (0, 0)])
```


## Complete Example

```python
# Workflow
a = arange(6)
i = nditer(a.reshape(2, 3), ['multi_index'], [['readonly']])
assert_equal(iter_multi_index(i), [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2)])
i = nditer(a.reshape(2, 3).copy(order='F'), ['multi_index'], [['readonly']])
assert_equal(iter_multi_index(i), [(0, 0), (1, 0), (0, 1), (1, 1), (0, 2), (1, 2)])
i = nditer(a.reshape(2, 3)[::-1], ['multi_index'], [['readonly']])
assert_equal(iter_multi_index(i), [(1, 0), (1, 1), (1, 2), (0, 0), (0, 1), (0, 2)])
i = nditer(a.reshape(2, 3)[:, ::-1], ['multi_index'], [['readonly']])
assert_equal(iter_multi_index(i), [(0, 2), (0, 1), (0, 0), (1, 2), (1, 1), (1, 0)])
i = nditer(a.reshape(2, 3)[::-1, ::-1], ['multi_index'], [['readonly']])
assert_equal(iter_multi_index(i), [(1, 2), (1, 1), (1, 0), (0, 2), (0, 1), (0, 0)])
i = nditer(a.reshape(2, 3).copy(order='F')[::-1], ['multi_index'], [['readonly']])
assert_equal(iter_multi_index(i), [(1, 0), (0, 0), (1, 1), (0, 1), (1, 2), (0, 2)])
i = nditer(a.reshape(2, 3).copy(order='F')[:, ::-1], ['multi_index'], [['readonly']])
assert_equal(iter_multi_index(i), [(0, 2), (1, 2), (0, 1), (1, 1), (0, 0), (1, 0)])
i = nditer(a.reshape(2, 3).copy(order='F')[::-1, ::-1], ['multi_index'], [['readonly']])
assert_equal(iter_multi_index(i), [(1, 2), (0, 2), (1, 1), (0, 1), (1, 0), (0, 0)])
```

## Next Steps


---

*Source: test_nditer.py:232 | Complexity: Advanced | Last updated: 2026-06-02*