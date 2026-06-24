# How To: Randomstate Ctor Old Style Pickle

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test randomstate ctor old style pickle

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

### Step 1: Assign rs = np.random.RandomState(...)

```python
rs = np.random.RandomState(MT19937(0))
```

**Verification:**
```python
assert args[0].__class__.__name__ == 'MT19937'
```

### Step 2: Call rs.standard_normal()

```python
rs.standard_normal(1)
```

**Verification:**
```python
assert_equal(state_a['bit_generator'], state_b['bit_generator'])
```

### Step 3: Assign unknown = rs.__reduce__(...)

```python
ctor, args, state_a = rs.__reduce__()
```

**Verification:**
```python
assert_array_equal(state_a['state']['key'], state_b['state']['key'])
```

### Step 4: Assign b = ctor(...)

```python
b = ctor(*('MT19937',))
```

**Verification:**
```python
assert_array_equal(state_a['state']['pos'], state_b['state']['pos'])
```

### Step 5: Call b.set_state()

```python
b.set_state(state_a)
```

**Verification:**
```python
assert_equal(state_a['has_gauss'], state_b['has_gauss'])
```

### Step 6: Assign state_b = b.get_state(...)

```python
state_b = b.get_state(legacy=False)
```

**Verification:**
```python
assert_equal(state_a['gauss'], state_b['gauss'])
```

### Step 7: Call assert_equal()

```python
assert_equal(state_a['bit_generator'], state_b['bit_generator'])
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(state_a['state']['key'], state_b['state']['key'])
```

### Step 9: Call assert_array_equal()

```python
assert_array_equal(state_a['state']['pos'], state_b['state']['pos'])
```

### Step 10: Call assert_equal()

```python
assert_equal(state_a['has_gauss'], state_b['has_gauss'])
```

### Step 11: Call assert_equal()

```python
assert_equal(state_a['gauss'], state_b['gauss'])
```


## Complete Example

```python
# Workflow
rs = np.random.RandomState(MT19937(0))
rs.standard_normal(1)
ctor, args, state_a = rs.__reduce__()
assert args[0].__class__.__name__ == 'MT19937'
b = ctor(*('MT19937',))
b.set_state(state_a)
state_b = b.get_state(legacy=False)
assert_equal(state_a['bit_generator'], state_b['bit_generator'])
assert_array_equal(state_a['state']['key'], state_b['state']['key'])
assert_array_equal(state_a['state']['pos'], state_b['state']['pos'])
assert_equal(state_a['has_gauss'], state_b['has_gauss'])
assert_equal(state_a['gauss'], state_b['gauss'])
```

## Next Steps


---

*Source: test_randomstate.py:2019 | Complexity: Advanced | Last updated: 2026-06-02*