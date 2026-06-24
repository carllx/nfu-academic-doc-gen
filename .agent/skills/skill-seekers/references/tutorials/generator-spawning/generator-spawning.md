# How To: Generator Spawning

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test spawning new generators and bit_generators directly.
    

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

### Step 1: ' Test spawning new generators and bit_generators directly.\n    '

```python
' Test spawning new generators and bit_generators directly.\n    '
```

**Verification:**
```python
assert [c.spawn_key for c in new_ss] == expected_keys
```

### Step 2: Assign rng = np.random.default_rng(...)

```python
rng = np.random.default_rng()
```

**Verification:**
```python
assert [bg.seed_seq.spawn_key for bg in new_bgs] == expected_keys
```

### Step 3: Assign seq = value

```python
seq = rng.bit_generator.seed_seq
```

**Verification:**
```python
assert found_keys == expected_keys
```

### Step 4: Assign new_ss = seq.spawn(...)

```python
new_ss = seq.spawn(5)
```

**Verification:**
```python
assert new_rngs[0].uniform() != new_rngs[1].uniform()
```

### Step 5: Assign expected_keys = value

```python
expected_keys = [seq.spawn_key + (i,) for i in range(5)]
```

**Verification:**
```python
assert [c.spawn_key for c in new_ss] == expected_keys
```

### Step 6: Assign new_bgs = rng.bit_generator.spawn(...)

```python
new_bgs = rng.bit_generator.spawn(5)
```

### Step 7: Assign expected_keys = value

```python
expected_keys = [seq.spawn_key + (i,) for i in range(5, 10)]
```

**Verification:**
```python
assert [bg.seed_seq.spawn_key for bg in new_bgs] == expected_keys
```

### Step 8: Assign new_rngs = rng.spawn(...)

```python
new_rngs = rng.spawn(5)
```

### Step 9: Assign expected_keys = value

```python
expected_keys = [seq.spawn_key + (i,) for i in range(10, 15)]
```

### Step 10: Assign found_keys = value

```python
found_keys = [rng.bit_generator.seed_seq.spawn_key for rng in new_rngs]
```

**Verification:**
```python
assert found_keys == expected_keys
```


## Complete Example

```python
# Workflow
' Test spawning new generators and bit_generators directly.\n    '
rng = np.random.default_rng()
seq = rng.bit_generator.seed_seq
new_ss = seq.spawn(5)
expected_keys = [seq.spawn_key + (i,) for i in range(5)]
assert [c.spawn_key for c in new_ss] == expected_keys
new_bgs = rng.bit_generator.spawn(5)
expected_keys = [seq.spawn_key + (i,) for i in range(5, 10)]
assert [bg.seed_seq.spawn_key for bg in new_bgs] == expected_keys
new_rngs = rng.spawn(5)
expected_keys = [seq.spawn_key + (i,) for i in range(10, 15)]
found_keys = [rng.bit_generator.seed_seq.spawn_key for rng in new_rngs]
assert found_keys == expected_keys
assert new_rngs[0].uniform() != new_rngs[1].uniform()
```

## Next Steps


---

*Source: test_direct.py:164 | Complexity: Advanced | Last updated: 2026-06-02*