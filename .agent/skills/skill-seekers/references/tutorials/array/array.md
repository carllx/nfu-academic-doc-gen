# How To: Array

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test array

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

### Step 1: Assign s = np.random.RandomState(...)

```python
s = np.random.RandomState(range(10))
```

**Verification:**
```python
assert_equal(s.randint(1000), 468)
```

### Step 2: Call assert_equal()

```python
assert_equal(s.randint(1000), 468)
```

**Verification:**
```python
assert_equal(s.randint(1000), 468)
```

### Step 3: Assign s = np.random.RandomState(...)

```python
s = np.random.RandomState(np.arange(10))
```

**Verification:**
```python
assert_equal(s.randint(1000), 973)
```

### Step 4: Call assert_equal()

```python
assert_equal(s.randint(1000), 468)
```

**Verification:**
```python
assert_equal(s.randint(1000), 265)
```

### Step 5: Assign s = np.random.RandomState(...)

```python
s = np.random.RandomState([0])
```

### Step 6: Call assert_equal()

```python
assert_equal(s.randint(1000), 973)
```

### Step 7: Assign s = np.random.RandomState(...)

```python
s = np.random.RandomState([4294967295])
```

### Step 8: Call assert_equal()

```python
assert_equal(s.randint(1000), 265)
```


## Complete Example

```python
# Workflow
s = np.random.RandomState(range(10))
assert_equal(s.randint(1000), 468)
s = np.random.RandomState(np.arange(10))
assert_equal(s.randint(1000), 468)
s = np.random.RandomState([0])
assert_equal(s.randint(1000), 973)
s = np.random.RandomState([4294967295])
assert_equal(s.randint(1000), 265)
```

## Next Steps


---

*Source: test_random.py:26 | Complexity: Advanced | Last updated: 2026-06-02*