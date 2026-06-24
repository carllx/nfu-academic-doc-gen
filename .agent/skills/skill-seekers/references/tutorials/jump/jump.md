# How To: Jump

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test jump

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
assert_(not comp_state(state, jumped_state))
```

### Step 2: Assign state = value

```python
state = rg.bit_generator.state
```

**Verification:**
```python
assert_(comp_state(jumped_state, rejumped_state))
```

### Step 3: Assign bit_gen2 = rg.bit_generator.jumped(...)

```python
bit_gen2 = rg.bit_generator.jumped()
```

### Step 4: Assign jumped_state = value

```python
jumped_state = bit_gen2.state
```

### Step 5: Call assert_()

```python
assert_(not comp_state(state, jumped_state))
```

### Step 6: Call rg.random()

```python
rg.random(2 * 3 * 5 * 7 * 11 * 13 * 17)
```

### Step 7: Assign rg.bit_generator.state = state

```python
rg.bit_generator.state = state
```

### Step 8: Assign bit_gen3 = rg.bit_generator.jumped(...)

```python
bit_gen3 = rg.bit_generator.jumped()
```

### Step 9: Assign rejumped_state = value

```python
rejumped_state = bit_gen3.state
```

### Step 10: Call assert_()

```python
assert_(comp_state(jumped_state, rejumped_state))
```

### Step 11: Assign bitgen_name = value

```python
bitgen_name = rg.bit_generator.__class__.__name__
```

### Step 12: Call pytest.skip()

```python
pytest.skip(f'Jump is not supported by {bitgen_name}')
```


## Complete Example

```python
# Workflow
rg = self._create_rng().rg
state = rg.bit_generator.state
if hasattr(rg.bit_generator, 'jumped'):
    bit_gen2 = rg.bit_generator.jumped()
    jumped_state = bit_gen2.state
    assert_(not comp_state(state, jumped_state))
    rg.random(2 * 3 * 5 * 7 * 11 * 13 * 17)
    rg.bit_generator.state = state
    bit_gen3 = rg.bit_generator.jumped()
    rejumped_state = bit_gen3.state
    assert_(comp_state(jumped_state, rejumped_state))
else:
    bitgen_name = rg.bit_generator.__class__.__name__
    if bitgen_name not in ('SFC64',):
        raise AttributeError(f'no "jumped" in {bitgen_name}')
    pytest.skip(f'Jump is not supported by {bitgen_name}')
```

## Next Steps


---

*Source: test_smoke.py:132 | Complexity: Advanced | Last updated: 2026-06-02*