# How To: Legacy Pickle

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test legacy pickle

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
# Fixtures: version
```

## Step-by-Step Guide

### Step 1: Assign base_path = value

```python
base_path = os.path.split(os.path.abspath(__file__))[0]
```

**Verification:**
```python
assert isinstance(rg, Generator)
```

### Step 2: Assign pkl_file = os.path.join(...)

```python
pkl_file = os.path.join(base_path, 'data', f'generator_pcg64_np{version}.pkl.gz')
```

**Verification:**
```python
assert isinstance(rg.bit_generator, np.random.PCG64)
```

### Step 3: Assign state = value

```python
state = rg.bit_generator.state['state']
```

**Verification:**
```python
assert state['state'] == 35399562948360463058890781895381311971
```

### Step 4: Assign rg = pickle.load(...)

```python
rg = pickle.load(gz)
```

**Verification:**
```python
assert state['inc'] == 87136372517582989555478159403783844777
```


## Complete Example

```python
# Setup
# Fixtures: version

# Workflow
import gzip
import pickle
base_path = os.path.split(os.path.abspath(__file__))[0]
pkl_file = os.path.join(base_path, 'data', f'generator_pcg64_np{version}.pkl.gz')
with gzip.open(pkl_file) as gz:
    rg = pickle.load(gz)
state = rg.bit_generator.state['state']
assert isinstance(rg, Generator)
assert isinstance(rg.bit_generator, np.random.PCG64)
assert state['state'] == 35399562948360463058890781895381311971
assert state['inc'] == 87136372517582989555478159403783844777
```

## Next Steps


---

*Source: test_generator_mt19937.py:2809 | Complexity: Intermediate | Last updated: 2026-06-02*