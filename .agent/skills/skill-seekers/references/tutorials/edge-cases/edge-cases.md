# How To: Edge Cases

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test edge cases

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `hashlib`
- `os.path`
- `sys`
- `warnings`
- `pytest`
- `numpy`
- `numpy.exceptions`
- `numpy.linalg`
- `numpy.random`
- `numpy.testing`
- `pickle`
- `gzip`
- `pickle`
- `threading`

**Setup Required:**
```python
# Fixtures: method
```

## Step-by-Step Guide

### Step 1: Assign random = Generator(...)

```python
random = Generator(MT19937(self.seed))
```

**Verification:**
```python
assert_array_equal(x, [0, 0, 0])
```

### Step 2: Assign x = random.multivariate_hypergeometric(...)

```python
x = random.multivariate_hypergeometric([0, 0, 0], 0, method=method)
```

**Verification:**
```python
assert_array_equal(x, [])
```

### Step 3: Call assert_array_equal()

```python
assert_array_equal(x, [0, 0, 0])
```

**Verification:**
```python
assert_array_equal(x, np.empty((1, 0), dtype=np.int64))
```

### Step 4: Assign x = random.multivariate_hypergeometric(...)

```python
x = random.multivariate_hypergeometric([], 0, method=method)
```

**Verification:**
```python
assert_array_equal(x, [0, 0, 0])
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(x, [])
```

**Verification:**
```python
assert_array_equal(x, [3, 0, 0])
```

### Step 6: Assign x = random.multivariate_hypergeometric(...)

```python
x = random.multivariate_hypergeometric([], 0, size=1, method=method)
```

**Verification:**
```python
assert_array_equal(x, colors)
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(x, np.empty((1, 0), dtype=np.int64))
```

**Verification:**
```python
assert_array_equal(x, [[3, 4, 5]] * 3)
```

### Step 8: Assign x = random.multivariate_hypergeometric(...)

```python
x = random.multivariate_hypergeometric([1, 2, 3], 0, method=method)
```

### Step 9: Call assert_array_equal()

```python
assert_array_equal(x, [0, 0, 0])
```

### Step 10: Assign x = random.multivariate_hypergeometric(...)

```python
x = random.multivariate_hypergeometric([9, 0, 0], 3, method=method)
```

### Step 11: Call assert_array_equal()

```python
assert_array_equal(x, [3, 0, 0])
```

### Step 12: Assign colors = value

```python
colors = [1, 1, 0, 1, 1]
```

### Step 13: Assign x = random.multivariate_hypergeometric(...)

```python
x = random.multivariate_hypergeometric(colors, sum(colors), method=method)
```

### Step 14: Call assert_array_equal()

```python
assert_array_equal(x, colors)
```

### Step 15: Assign x = random.multivariate_hypergeometric(...)

```python
x = random.multivariate_hypergeometric([3, 4, 5], 12, size=3, method=method)
```

### Step 16: Call assert_array_equal()

```python
assert_array_equal(x, [[3, 4, 5]] * 3)
```


## Complete Example

```python
# Setup
# Fixtures: method

# Workflow
random = Generator(MT19937(self.seed))
x = random.multivariate_hypergeometric([0, 0, 0], 0, method=method)
assert_array_equal(x, [0, 0, 0])
x = random.multivariate_hypergeometric([], 0, method=method)
assert_array_equal(x, [])
x = random.multivariate_hypergeometric([], 0, size=1, method=method)
assert_array_equal(x, np.empty((1, 0), dtype=np.int64))
x = random.multivariate_hypergeometric([1, 2, 3], 0, method=method)
assert_array_equal(x, [0, 0, 0])
x = random.multivariate_hypergeometric([9, 0, 0], 3, method=method)
assert_array_equal(x, [3, 0, 0])
colors = [1, 1, 0, 1, 1]
x = random.multivariate_hypergeometric(colors, sum(colors), method=method)
assert_array_equal(x, colors)
x = random.multivariate_hypergeometric([3, 4, 5], 12, size=3, method=method)
assert_array_equal(x, [[3, 4, 5]] * 3)
```

## Next Steps


---

*Source: test_generator_mt19937.py:214 | Complexity: Advanced | Last updated: 2026-06-02*