# How To: Hypergeometric

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test hypergeometric

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

### Step 1: Assign rng = random.RandomState(...)

```python
rng = random.RandomState(self.seed)
```

**Verification:**
```python
assert_array_equal(actual, desired)
```

### Step 2: Assign actual = rng.hypergeometric(...)

```python
actual = rng.hypergeometric(10, 5, 14, size=(3, 2))
```

**Verification:**
```python
assert_array_equal(actual, desired)
```

### Step 3: Assign desired = np.array(...)

```python
desired = np.array([[10, 10], [10, 10], [9, 9]])
```

**Verification:**
```python
assert_array_equal(actual, desired)
```

### Step 4: Call assert_array_equal()

```python
assert_array_equal(actual, desired)
```

**Verification:**
```python
assert_array_equal(actual, desired)
```

### Step 5: Assign actual = rng.hypergeometric(...)

```python
actual = rng.hypergeometric(5, 0, 3, size=4)
```

**Verification:**
```python
assert_array_equal(actual, desired)
```

### Step 6: Assign desired = np.array(...)

```python
desired = np.array([3, 3, 3, 3])
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(actual, desired)
```

### Step 8: Assign actual = rng.hypergeometric(...)

```python
actual = rng.hypergeometric(15, 0, 12, size=4)
```

### Step 9: Assign desired = np.array(...)

```python
desired = np.array([12, 12, 12, 12])
```

### Step 10: Call assert_array_equal()

```python
assert_array_equal(actual, desired)
```

### Step 11: Assign actual = rng.hypergeometric(...)

```python
actual = rng.hypergeometric(0, 5, 3, size=4)
```

### Step 12: Assign desired = np.array(...)

```python
desired = np.array([0, 0, 0, 0])
```

### Step 13: Call assert_array_equal()

```python
assert_array_equal(actual, desired)
```

### Step 14: Assign actual = rng.hypergeometric(...)

```python
actual = rng.hypergeometric(0, 15, 12, size=4)
```

### Step 15: Assign desired = np.array(...)

```python
desired = np.array([0, 0, 0, 0])
```

### Step 16: Call assert_array_equal()

```python
assert_array_equal(actual, desired)
```


## Complete Example

```python
# Workflow
rng = random.RandomState(self.seed)
actual = rng.hypergeometric(10, 5, 14, size=(3, 2))
desired = np.array([[10, 10], [10, 10], [9, 9]])
assert_array_equal(actual, desired)
actual = rng.hypergeometric(5, 0, 3, size=4)
desired = np.array([3, 3, 3, 3])
assert_array_equal(actual, desired)
actual = rng.hypergeometric(15, 0, 12, size=4)
desired = np.array([12, 12, 12, 12])
assert_array_equal(actual, desired)
actual = rng.hypergeometric(0, 5, 3, size=4)
desired = np.array([0, 0, 0, 0])
assert_array_equal(actual, desired)
actual = rng.hypergeometric(0, 15, 12, size=4)
desired = np.array([0, 0, 0, 0])
assert_array_equal(actual, desired)
```

## Next Steps


---

*Source: test_random.py:698 | Complexity: Advanced | Last updated: 2026-06-02*