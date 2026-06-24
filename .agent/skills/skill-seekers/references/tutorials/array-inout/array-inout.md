# How To: Array Inout

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test array inout

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `textwrap`
- `pytest`
- `numpy`
- `numpy.f2py.tests`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: dtype
```

## Step-by-Step Guide

### Step 1: Assign f = getattr(...)

```python
f = getattr(self.module, self.fprefix + '_array_inout')
```

**Verification:**
```python
assert_array_equal(a, n)
```

### Step 2: Assign n = np.array(...)

```python
n = np.array(['A', 'B', 'C'], dtype=dtype, order='F')
```

**Verification:**
```python
assert_array_equal(a, np.array(['a', 'A', 'B', 'C'], dtype=dtype))
```

### Step 3: Assign a = np.array(...)

```python
a = np.array(['a', 'b', 'c'], dtype=dtype, order='F')
```

**Verification:**
```python
assert_array_equal(a, np.array([['A', 'B', 'C']], dtype=dtype))
```

### Step 4: Call f()

```python
f(a, n)
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(a, n)
```

### Step 6: Assign a = np.array(...)

```python
a = np.array(['a', 'b', 'c', 'd'], dtype=dtype)
```

### Step 7: Call f()

```python
f(a[1:], n)
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(a, np.array(['a', 'A', 'B', 'C'], dtype=dtype))
```

### Step 9: Assign a = np.array(...)

```python
a = np.array([['a', 'b', 'c']], dtype=dtype, order='F')
```

### Step 10: Call f()

```python
f(a, n)
```

### Step 11: Call assert_array_equal()

```python
assert_array_equal(a, np.array([['A', 'B', 'C']], dtype=dtype))
```

### Step 12: Assign a = np.array(...)

```python
a = np.array(['a', 'b', 'c', 'd'], dtype=dtype, order='F')
```

### Step 13: Call f()

```python
f(a, n)
```


## Complete Example

```python
# Setup
# Fixtures: dtype

# Workflow
f = getattr(self.module, self.fprefix + '_array_inout')
n = np.array(['A', 'B', 'C'], dtype=dtype, order='F')
a = np.array(['a', 'b', 'c'], dtype=dtype, order='F')
f(a, n)
assert_array_equal(a, n)
a = np.array(['a', 'b', 'c', 'd'], dtype=dtype)
f(a[1:], n)
assert_array_equal(a, np.array(['a', 'A', 'B', 'C'], dtype=dtype))
a = np.array([['a', 'b', 'c']], dtype=dtype, order='F')
f(a, n)
assert_array_equal(a, np.array([['A', 'B', 'C']], dtype=dtype))
a = np.array(['a', 'b', 'c', 'd'], dtype=dtype, order='F')
try:
    f(a, n)
except ValueError as msg:
    if not str(msg).endswith('th dimension must be fixed to 3 but got 4'):
        raise
else:
    raise SystemError(f'{f.__name__} should have failed on wrong input')
```

## Next Steps


---

*Source: test_character.py:377 | Complexity: Advanced | Last updated: 2026-06-02*