# How To: Reset State Uint32

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reset state uint32

## Prerequisites

**Required Modules:**
- `pickle`
- `dataclasses`
- `functools`
- `pytest`
- `numpy`
- `numpy.random`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign data = self._create_rng(...)

```python
data = self._create_rng()
```

**Verification:**
```python
assert_array_equal(n1, n2)
```

### Step 2: Assign rg = Generator(...)

```python
rg = Generator(data.bit_generator(*data.seed))
```

### Step 3: Call rg.integers()

```python
rg.integers(0, 2 ** 24, 120, dtype=np.uint32)
```

### Step 4: Assign state = value

```python
state = rg.bit_generator.state
```

### Step 5: Assign n1 = rg.integers(...)

```python
n1 = rg.integers(0, 2 ** 24, 10, dtype=np.uint32)
```

### Step 6: Assign rg2 = Generator(...)

```python
rg2 = Generator(data.bit_generator())
```

### Step 7: Assign rg2.bit_generator.state = state

```python
rg2.bit_generator.state = state
```

### Step 8: Assign n2 = rg2.integers(...)

```python
n2 = rg2.integers(0, 2 ** 24, 10, dtype=np.uint32)
```

### Step 9: Call assert_array_equal()

```python
assert_array_equal(n1, n2)
```


## Complete Example

```python
# Workflow
data = self._create_rng()
rg = Generator(data.bit_generator(*data.seed))
rg.integers(0, 2 ** 24, 120, dtype=np.uint32)
state = rg.bit_generator.state
n1 = rg.integers(0, 2 ** 24, 10, dtype=np.uint32)
rg2 = Generator(data.bit_generator())
rg2.bit_generator.state = state
n2 = rg2.integers(0, 2 ** 24, 10, dtype=np.uint32)
assert_array_equal(n1, n2)
```

## Next Steps


---

*Source: test_smoke.py:263 | Complexity: Advanced | Last updated: 2026-06-02*