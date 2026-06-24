# How To: Swap Worked

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test swap worked

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `hashlib`
- `pickle`
- `sys`
- `warnings`
- `pytest`
- `numpy`
- `numpy`
- `numpy.random`
- `numpy.testing`
- `threading`

**Setup Required:**
```python
# Fixtures: restore_singleton_bitgen
```

## Step-by-Step Guide

### Step 1: Call np.random.seed()

```python
np.random.seed(98765)
```

**Verification:**
```python
assert state[field] == state_direct[field]
```

### Step 2: Assign vals = np.random.randint(...)

```python
vals = np.random.randint(0, 2 ** 30, 10)
```

**Verification:**
```python
assert not np.all(vals == pcg_vals)
```

### Step 3: Assign bg = PCG64(...)

```python
bg = PCG64(0)
```

**Verification:**
```python
assert new_state['state']['state'] != state['state']['state']
```

### Step 4: Assign state = value

```python
state = bg.state
```

**Verification:**
```python
assert new_state['state']['inc'] == new_state['state']['inc']
```

### Step 5: Call np.random.set_bit_generator()

```python
np.random.set_bit_generator(bg)
```

### Step 6: Assign state_direct = np.random.get_state(...)

```python
state_direct = np.random.get_state(legacy=False)
```

### Step 7: Call np.random.seed()

```python
np.random.seed(98765)
```

### Step 8: Assign pcg_vals = np.random.randint(...)

```python
pcg_vals = np.random.randint(0, 2 ** 30, 10)
```

**Verification:**
```python
assert not np.all(vals == pcg_vals)
```

### Step 9: Assign new_state = value

```python
new_state = bg.state
```

**Verification:**
```python
assert new_state['state']['state'] != state['state']['state']
```


## Complete Example

```python
# Setup
# Fixtures: restore_singleton_bitgen

# Workflow
np.random.seed(98765)
vals = np.random.randint(0, 2 ** 30, 10)
bg = PCG64(0)
state = bg.state
np.random.set_bit_generator(bg)
state_direct = np.random.get_state(legacy=False)
for field in state:
    assert state[field] == state_direct[field]
np.random.seed(98765)
pcg_vals = np.random.randint(0, 2 ** 30, 10)
assert not np.all(vals == pcg_vals)
new_state = bg.state
assert new_state['state']['state'] != state['state']['state']
assert new_state['state']['inc'] == new_state['state']['inc']
```

## Next Steps


---

*Source: test_randomstate.py:2075 | Complexity: Advanced | Last updated: 2026-06-02*