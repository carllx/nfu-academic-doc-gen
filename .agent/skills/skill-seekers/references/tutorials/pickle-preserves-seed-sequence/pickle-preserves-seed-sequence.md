# How To: Pickle Preserves Seed Sequence

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pickle preserves seed sequence

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign rg = np.random.Generator(...)

```python
rg = np.random.Generator(np.random.PCG64DXSM(20240411))
```

**Verification:**
```python
assert_equal(ss.state, ss_plk.state)
```

### Step 2: Assign ss = value

```python
ss = rg.bit_generator.seed_seq
```

**Verification:**
```python
assert_equal(ss.pool, ss_plk.pool)
```

### Step 3: Assign rg_plk = pickle.loads(...)

```python
rg_plk = pickle.loads(pickle.dumps(rg))
```

**Verification:**
```python
assert_equal(ss.state, ss_plk.state)
```

### Step 4: Assign ss_plk = value

```python
ss_plk = rg_plk.bit_generator.seed_seq
```

### Step 5: Call assert_equal()

```python
assert_equal(ss.state, ss_plk.state)
```

### Step 6: Call assert_equal()

```python
assert_equal(ss.pool, ss_plk.pool)
```

### Step 7: Call rg.bit_generator.seed_seq.spawn()

```python
rg.bit_generator.seed_seq.spawn(10)
```

### Step 8: Assign rg_plk = pickle.loads(...)

```python
rg_plk = pickle.loads(pickle.dumps(rg))
```

### Step 9: Assign ss_plk = value

```python
ss_plk = rg_plk.bit_generator.seed_seq
```

### Step 10: Call assert_equal()

```python
assert_equal(ss.state, ss_plk.state)
```


## Complete Example

```python
# Workflow
import pickle
rg = np.random.Generator(np.random.PCG64DXSM(20240411))
ss = rg.bit_generator.seed_seq
rg_plk = pickle.loads(pickle.dumps(rg))
ss_plk = rg_plk.bit_generator.seed_seq
assert_equal(ss.state, ss_plk.state)
assert_equal(ss.pool, ss_plk.pool)
rg.bit_generator.seed_seq.spawn(10)
rg_plk = pickle.loads(pickle.dumps(rg))
ss_plk = rg_plk.bit_generator.seed_seq
assert_equal(ss.state, ss_plk.state)
```

## Next Steps


---

*Source: test_generator_mt19937.py:2790 | Complexity: Advanced | Last updated: 2026-06-02*