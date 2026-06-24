# How To: Create Py Random State

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test create py random state

## Prerequisites

**Required Modules:**
- `random`
- `copy`
- `pytest`
- `networkx`
- `networkx.utils`
- `networkx.utils.misc`


## Step-by-Step Guide

### Step 1: Assign pyrs = value

```python
pyrs = random.Random
```

**Verification:**
```python
assert isinstance(create_py_random_state(1), pyrs)
```

### Step 2: Call pytest.raises()

```python
pytest.raises(ValueError, create_py_random_state, 'a')
```

**Verification:**
```python
assert isinstance(create_py_random_state(None), pyrs)
```

### Step 3: Assign np = pytest.importorskip(...)

```python
np = pytest.importorskip('numpy')
```

**Verification:**
```python
assert isinstance(create_py_random_state(pyrs(1)), pyrs)
```

### Step 4: Assign rs = value

```python
rs = np.random.RandomState
```

**Verification:**
```python
assert isinstance(create_py_random_state(np.random), nprs)
```

### Step 5: Assign rng = np.random.default_rng(...)

```python
rng = np.random.default_rng(1000)
```

**Verification:**
```python
assert isinstance(create_py_random_state(rs(1)), old_nprs)
```

### Step 6: Assign rng_explicit = np.random.Generator(...)

```python
rng_explicit = np.random.Generator(np.random.SFC64())
```

**Verification:**
```python
assert isinstance(create_py_random_state(rng), nprs)
```

### Step 7: Assign old_nprs = PythonRandomInterface

```python
old_nprs = PythonRandomInterface
```

**Verification:**
```python
assert isinstance(create_py_random_state(rng_explicit), nprs)
```

### Step 8: Assign nprs = PythonRandomViaNumpyBits

```python
nprs = PythonRandomViaNumpyBits
```

**Verification:**
```python
assert isinstance(old_nprs_instance, old_nprs)
```

### Step 9: Assign old_nprs_instance = old_nprs(...)

```python
old_nprs_instance = old_nprs()
```

**Verification:**
```python
assert isinstance(nprs_instance, nprs)
```

### Step 10: Assign nprs_instance = nprs(...)

```python
nprs_instance = nprs()
```

**Verification:**
```python
assert create_py_random_state(old_nprs_instance) == old_nprs_instance
```

### Step 11: Assign int64max = 9223372036854775807

```python
int64max = 9223372036854775807
```

**Verification:**
```python
assert create_py_random_state(nprs_instance) == nprs_instance
```

### Step 12: Assign prs = create_py_random_state(...)

```python
prs = create_py_random_state(r)
```

### Step 13: Call prs.randrange()

```python
prs.randrange(3, int64max + 5)
```

### Step 14: Call prs.randint()

```python
prs.randint(3, int64max + 5)
```


## Complete Example

```python
# Workflow
pyrs = random.Random
assert isinstance(create_py_random_state(1), pyrs)
assert isinstance(create_py_random_state(None), pyrs)
assert isinstance(create_py_random_state(pyrs(1)), pyrs)
pytest.raises(ValueError, create_py_random_state, 'a')
np = pytest.importorskip('numpy')
rs = np.random.RandomState
rng = np.random.default_rng(1000)
rng_explicit = np.random.Generator(np.random.SFC64())
old_nprs = PythonRandomInterface
nprs = PythonRandomViaNumpyBits
assert isinstance(create_py_random_state(np.random), nprs)
assert isinstance(create_py_random_state(rs(1)), old_nprs)
assert isinstance(create_py_random_state(rng), nprs)
assert isinstance(create_py_random_state(rng_explicit), nprs)
old_nprs_instance = old_nprs()
nprs_instance = nprs()
assert isinstance(old_nprs_instance, old_nprs)
assert isinstance(nprs_instance, nprs)
assert create_py_random_state(old_nprs_instance) == old_nprs_instance
assert create_py_random_state(nprs_instance) == nprs_instance
int64max = 9223372036854775807
for r in (rng, rs(1)):
    prs = create_py_random_state(r)
    prs.randrange(3, int64max + 5)
    prs.randint(3, int64max + 5)
```

## Next Steps


---

*Source: test_misc.py:176 | Complexity: Advanced | Last updated: 2026-06-02*