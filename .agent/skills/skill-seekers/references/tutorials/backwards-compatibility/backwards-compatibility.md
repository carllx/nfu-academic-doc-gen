# How To: Backwards Compatibility

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test backwards compatibility

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

### Step 1: Assign unknown = self._create_rng(...)

```python
prng, state = self._create_rng()
```

**Verification:**
```python
assert_(np.all(x1 == x2))
```

### Step 2: Assign old_state = value

```python
old_state = state[:-2]
```

**Verification:**
```python
assert_(np.all(x1 == x3))
```

### Step 3: Assign x1 = prng.standard_normal(...)

```python
x1 = prng.standard_normal(size=16)
```

### Step 4: Call prng.set_state()

```python
prng.set_state(old_state)
```

### Step 5: Assign x2 = prng.standard_normal(...)

```python
x2 = prng.standard_normal(size=16)
```

### Step 6: Call prng.set_state()

```python
prng.set_state(state)
```

### Step 7: Assign x3 = prng.standard_normal(...)

```python
x3 = prng.standard_normal(size=16)
```

### Step 8: Call assert_()

```python
assert_(np.all(x1 == x2))
```

### Step 9: Call assert_()

```python
assert_(np.all(x1 == x3))
```


## Complete Example

```python
# Workflow
prng, state = self._create_rng()
old_state = state[:-2]
x1 = prng.standard_normal(size=16)
prng.set_state(old_state)
x2 = prng.standard_normal(size=16)
prng.set_state(state)
x3 = prng.standard_normal(size=16)
assert_(np.all(x1 == x2))
assert_(np.all(x1 == x3))
```

## Next Steps


---

*Source: test_random.py:140 | Complexity: Advanced | Last updated: 2026-06-02*