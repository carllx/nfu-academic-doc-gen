# How To: Invalid Legacy State Setting

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test invalid legacy state setting

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign unknown = self._create_state(...)

```python
random_state, state = self._create_state()
```

**Verification:**
```python
assert_raises(ValueError, random_state.set_state, new_state)
```

### Step 2: Assign state = random_state.get_state(...)

```python
state = random_state.get_state()
```

**Verification:**
```python
assert_raises(TypeError, random_state.set_state, np.array(new_state, dtype=object))
```

### Step 3: Assign new_state = value

```python
new_state = ('Unknown',) + state[1:]
```

**Verification:**
```python
assert_raises(ValueError, random_state.set_state, state)
```

### Step 4: Call assert_raises()

```python
assert_raises(ValueError, random_state.set_state, new_state)
```

### Step 5: Call assert_raises()

```python
assert_raises(TypeError, random_state.set_state, np.array(new_state, dtype=object))
```

### Step 6: Assign state = random_state.get_state(...)

```python
state = random_state.get_state(legacy=False)
```

### Step 7: Call assert_raises()

```python
assert_raises(ValueError, random_state.set_state, state)
```


## Complete Example

```python
# Workflow
random_state, state = self._create_state()
state = random_state.get_state()
new_state = ('Unknown',) + state[1:]
assert_raises(ValueError, random_state.set_state, new_state)
assert_raises(TypeError, random_state.set_state, np.array(new_state, dtype=object))
state = random_state.get_state(legacy=False)
del state['bit_generator']
assert_raises(ValueError, random_state.set_state, state)
```

## Next Steps


---

*Source: test_randomstate.py:254 | Complexity: Intermediate | Last updated: 2026-06-02*