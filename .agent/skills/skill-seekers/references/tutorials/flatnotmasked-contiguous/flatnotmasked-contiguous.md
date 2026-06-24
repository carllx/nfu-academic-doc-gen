# How To: Flatnotmasked Contiguous

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test flatnotmasked contiguous

## Prerequisites

**Required Modules:**
- `inspect`
- `itertools`
- `pytest`
- `numpy`
- `numpy._core.numeric`
- `numpy.ma.core`
- `numpy.ma.extras`
- `numpy.ma.testutils`


## Step-by-Step Guide

### Step 1: Assign a = arange(...)

```python
a = arange(10)
```

**Verification:**
```python
assert_equal(test, [slice(0, a.size)])
```

### Step 2: Assign test = flatnotmasked_contiguous(...)

```python
test = flatnotmasked_contiguous(a)
```

**Verification:**
```python
assert_equal(test, [slice(0, a.size)])
```

### Step 3: Call assert_equal()

```python
assert_equal(test, [slice(0, a.size)])
```

**Verification:**
```python
assert_equal(test, [slice(3, 5), slice(6, 9)])
```

### Step 4: Assign a.mask = np.zeros(...)

```python
a.mask = np.zeros(10, dtype=bool)
```

**Verification:**
```python
assert_equal(test, [])
```

### Step 5: Call assert_equal()

```python
assert_equal(test, [slice(0, a.size)])
```

### Step 6: Assign unknown = masked

```python
a[(a < 3) | (a > 8) | (a == 5)] = masked
```

### Step 7: Assign test = flatnotmasked_contiguous(...)

```python
test = flatnotmasked_contiguous(a)
```

### Step 8: Call assert_equal()

```python
assert_equal(test, [slice(3, 5), slice(6, 9)])
```

### Step 9: Assign unknown = masked

```python
a[:] = masked
```

### Step 10: Assign test = flatnotmasked_contiguous(...)

```python
test = flatnotmasked_contiguous(a)
```

### Step 11: Call assert_equal()

```python
assert_equal(test, [])
```


## Complete Example

```python
# Workflow
a = arange(10)
test = flatnotmasked_contiguous(a)
assert_equal(test, [slice(0, a.size)])
a.mask = np.zeros(10, dtype=bool)
assert_equal(test, [slice(0, a.size)])
a[(a < 3) | (a > 8) | (a == 5)] = masked
test = flatnotmasked_contiguous(a)
assert_equal(test, [slice(3, 5), slice(6, 9)])
a[:] = masked
test = flatnotmasked_contiguous(a)
assert_equal(test, [])
```

## Next Steps


---

*Source: test_extras.py:184 | Complexity: Advanced | Last updated: 2026-06-02*