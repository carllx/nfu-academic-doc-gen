# How To: Shuffle Memoryview

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test shuffle memoryview

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
assert_equal(np.asarray(a), [0, 1, 4, 3, 2])
```

### Step 2: Assign a = value

```python
a = np.arange(5).data
```

**Verification:**
```python
assert_equal(np.asarray(a), [0, 1, 2, 3, 4])
```

### Step 3: Call rng.shuffle()

```python
rng.shuffle(a)
```

**Verification:**
```python
assert_equal(np.asarray(a), [4, 1, 0, 3, 2])
```

### Step 4: Call assert_equal()

```python
assert_equal(np.asarray(a), [0, 1, 4, 3, 2])
```

### Step 5: Assign rng = random.RandomState(...)

```python
rng = random.RandomState(self.seed)
```

### Step 6: Call rng.shuffle()

```python
rng.shuffle(a)
```

### Step 7: Call assert_equal()

```python
assert_equal(np.asarray(a), [0, 1, 2, 3, 4])
```

### Step 8: Assign rng = np.random.default_rng(...)

```python
rng = np.random.default_rng(self.seed)
```

### Step 9: Call rng.shuffle()

```python
rng.shuffle(a)
```

### Step 10: Call assert_equal()

```python
assert_equal(np.asarray(a), [4, 1, 0, 3, 2])
```


## Complete Example

```python
# Workflow
rng = random.RandomState(self.seed)
a = np.arange(5).data
rng.shuffle(a)
assert_equal(np.asarray(a), [0, 1, 4, 3, 2])
rng = random.RandomState(self.seed)
rng.shuffle(a)
assert_equal(np.asarray(a), [0, 1, 2, 3, 4])
rng = np.random.default_rng(self.seed)
rng.shuffle(a)
assert_equal(np.asarray(a), [4, 1, 0, 3, 2])
```

## Next Steps


---

*Source: test_random.py:565 | Complexity: Advanced | Last updated: 2026-06-02*