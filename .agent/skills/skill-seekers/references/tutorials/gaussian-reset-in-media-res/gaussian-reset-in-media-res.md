# How To: Gaussian Reset In Media Res

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test gaussian reset in media res

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
assert_(np.all(old == new))
```

### Step 2: Call prng.standard_normal()

```python
prng.standard_normal()
```

### Step 3: Assign state = prng.get_state(...)

```python
state = prng.get_state()
```

### Step 4: Assign old = prng.standard_normal(...)

```python
old = prng.standard_normal(size=3)
```

### Step 5: Call prng.set_state()

```python
prng.set_state(state)
```

### Step 6: Assign new = prng.standard_normal(...)

```python
new = prng.standard_normal(size=3)
```

### Step 7: Call assert_()

```python
assert_(np.all(old == new))
```


## Complete Example

```python
# Workflow
prng, state = self._create_rng()
prng.standard_normal()
state = prng.get_state()
old = prng.standard_normal(size=3)
prng.set_state(state)
new = prng.standard_normal(size=3)
assert_(np.all(old == new))
```

## Next Steps


---

*Source: test_random.py:129 | Complexity: Intermediate | Last updated: 2026-06-02*