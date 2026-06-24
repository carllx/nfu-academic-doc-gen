# How To: Seedsequence

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test seedsequence

## Prerequisites

**Required Modules:**
- `os`
- `sys`
- `os.path`
- `pytest`
- `numpy`
- `numpy.random`
- `numpy.random._common`
- `numpy.testing`
- `cffi`
- `ctypes`
- `numpy.random.bit_generator`
- `numpy.random.bit_generator`
- `pickle`
- `pickle`
- `gzip`
- `pickle`


## Step-by-Step Guide

### Step 1: Assign s1 = SeedSequence(...)

```python
s1 = SeedSequence(range(10), spawn_key=(1, 2), pool_size=6)
```

**Verification:**
```python
assert_equal(s1.state, s2.state)
```

### Step 2: Call s1.spawn()

```python
s1.spawn(10)
```

**Verification:**
```python
assert_equal(s1.n_children_spawned, s2.n_children_spawned)
```

### Step 3: Assign s2 = SeedSequence(...)

```python
s2 = SeedSequence(**s1.state)
```

**Verification:**
```python
assert_raises(TypeError, ISeedSequence)
```

### Step 4: Call assert_equal()

```python
assert_equal(s1.state, s2.state)
```

**Verification:**
```python
assert_raises(TypeError, ISpawnableSeedSequence)
```

### Step 5: Call assert_equal()

```python
assert_equal(s1.n_children_spawned, s2.n_children_spawned)
```

**Verification:**
```python
assert_raises(NotImplementedError, dummy.generate_state, 10)
```

### Step 6: Call assert_raises()

```python
assert_raises(TypeError, ISeedSequence)
```

**Verification:**
```python
assert len(dummy.spawn(10)) == 10
```

### Step 7: Call assert_raises()

```python
assert_raises(TypeError, ISpawnableSeedSequence)
```

### Step 8: Assign dummy = SeedlessSeedSequence(...)

```python
dummy = SeedlessSeedSequence()
```

### Step 9: Call assert_raises()

```python
assert_raises(NotImplementedError, dummy.generate_state, 10)
```

**Verification:**
```python
assert len(dummy.spawn(10)) == 10
```


## Complete Example

```python
# Workflow
from numpy.random.bit_generator import ISeedSequence, ISpawnableSeedSequence, SeedlessSeedSequence
s1 = SeedSequence(range(10), spawn_key=(1, 2), pool_size=6)
s1.spawn(10)
s2 = SeedSequence(**s1.state)
assert_equal(s1.state, s2.state)
assert_equal(s1.n_children_spawned, s2.n_children_spawned)
assert_raises(TypeError, ISeedSequence)
assert_raises(TypeError, ISpawnableSeedSequence)
dummy = SeedlessSeedSequence()
assert_raises(NotImplementedError, dummy.generate_state, 10)
assert len(dummy.spawn(10)) == 10
```

## Next Steps


---

*Source: test_direct.py:143 | Complexity: Advanced | Last updated: 2026-06-02*