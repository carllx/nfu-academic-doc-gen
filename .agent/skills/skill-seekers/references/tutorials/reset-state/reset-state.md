# How To: Reset State

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reset state

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

### Step 1: Assign rg = value

```python
rg = self._create_rng().rg
```

**Verification:**
```python
assert_(int_1 == int_2)
```

### Step 2: Assign state = value

```python
state = rg.bit_generator.state
```

### Step 3: Assign int_1 = rg.integers(...)

```python
int_1 = rg.integers(2 ** 31)
```

### Step 4: Assign rg.bit_generator.state = state

```python
rg.bit_generator.state = state
```

### Step 5: Assign int_2 = rg.integers(...)

```python
int_2 = rg.integers(2 ** 31)
```

### Step 6: Call assert_()

```python
assert_(int_1 == int_2)
```


## Complete Example

```python
# Workflow
rg = self._create_rng().rg
state = rg.bit_generator.state
int_1 = rg.integers(2 ** 31)
rg.bit_generator.state = state
int_2 = rg.integers(2 ** 31)
assert_(int_1 == int_2)
```

## Next Steps


---

*Source: test_smoke.py:229 | Complexity: Intermediate | Last updated: 2026-06-02*