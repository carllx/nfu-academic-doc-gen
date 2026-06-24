# How To: Init

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test init

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
assert_(comp_state(state, new_state))
```

### Step 2: Assign data.rg = Generator(...)

```python
data.rg = Generator(data.bit_generator())
```

### Step 3: Assign state = value

```python
state = data.rg.bit_generator.state
```

### Step 4: Call data.rg.standard_normal()

```python
data.rg.standard_normal(1)
```

### Step 5: Call data.rg.standard_normal()

```python
data.rg.standard_normal(1)
```

### Step 6: Assign data.rg.bit_generator.state = state

```python
data.rg.bit_generator.state = state
```

### Step 7: Assign new_state = value

```python
new_state = data.rg.bit_generator.state
```

### Step 8: Call assert_()

```python
assert_(comp_state(state, new_state))
```


## Complete Example

```python
# Workflow
data = self._create_rng()
data.rg = Generator(data.bit_generator())
state = data.rg.bit_generator.state
data.rg.standard_normal(1)
data.rg.standard_normal(1)
data.rg.bit_generator.state = state
new_state = data.rg.bit_generator.state
assert_(comp_state(state, new_state))
```

## Next Steps


---

*Source: test_smoke.py:112 | Complexity: Advanced | Last updated: 2026-06-02*