# How To: Reset State Float

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reset state float

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
assert_((n1 == n2).all())
```

### Step 2: Assign rg = Generator(...)

```python
rg = Generator(data.bit_generator(*data.seed))
```

### Step 3: Call rg.random()

```python
rg.random(dtype='float32')
```

### Step 4: Assign state = value

```python
state = rg.bit_generator.state
```

### Step 5: Assign n1 = rg.random(...)

```python
n1 = rg.random(size=10, dtype='float32')
```

### Step 6: Assign rg2 = Generator(...)

```python
rg2 = Generator(data.bit_generator())
```

### Step 7: Assign rg2.bit_generator.state = state

```python
rg2.bit_generator.state = state
```

### Step 8: Assign n2 = rg2.random(...)

```python
n2 = rg2.random(size=10, dtype='float32')
```

### Step 9: Call assert_()

```python
assert_((n1 == n2).all())
```


## Complete Example

```python
# Workflow
data = self._create_rng()
rg = Generator(data.bit_generator(*data.seed))
rg.random(dtype='float32')
state = rg.bit_generator.state
n1 = rg.random(size=10, dtype='float32')
rg2 = Generator(data.bit_generator())
rg2.bit_generator.state = state
n2 = rg2.random(size=10, dtype='float32')
assert_((n1 == n2).all())
```

## Next Steps


---

*Source: test_smoke.py:274 | Complexity: Advanced | Last updated: 2026-06-02*