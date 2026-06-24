# How To: Generator Ctor Old Style Pickle

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test generator ctor old style pickle

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
rg = np.random.Generator(np.random.PCG64DXSM(0))
```

**Verification:**
```python
assert bit_gen.__class__.__name__ == 'PCG64DXSM'
```

### Step 2: Call rg.standard_normal()

```python
rg.standard_normal(1)
```

**Verification:**
```python
assert bit_gen.state == state_b
```

### Step 3: Assign unknown = rg.__reduce__(...)

```python
ctor, (bit_gen,), _ = rg.__reduce__()
```

**Verification:**
```python
assert bit_gen.__class__.__name__ == 'PCG64DXSM'
```

### Step 4: Call print()

```python
print(ctor)
```

### Step 5: Assign b = ctor(...)

```python
b = ctor(*('PCG64DXSM',))
```

### Step 6: Call print()

```python
print(b)
```

### Step 7: Assign b.bit_generator.state = value

```python
b.bit_generator.state = bit_gen.state
```

### Step 8: Assign state_b = value

```python
state_b = b.bit_generator.state
```

**Verification:**
```python
assert bit_gen.state == state_b
```


## Complete Example

```python
# Workflow
rg = np.random.Generator(np.random.PCG64DXSM(0))
rg.standard_normal(1)
ctor, (bit_gen,), _ = rg.__reduce__()
assert bit_gen.__class__.__name__ == 'PCG64DXSM'
print(ctor)
b = ctor(*('PCG64DXSM',))
print(b)
b.bit_generator.state = bit_gen.state
state_b = b.bit_generator.state
assert bit_gen.state == state_b
```

## Next Steps


---

*Source: test_generator_mt19937.py:2775 | Complexity: Advanced | Last updated: 2026-06-02*