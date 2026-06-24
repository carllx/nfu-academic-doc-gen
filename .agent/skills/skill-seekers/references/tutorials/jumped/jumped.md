# How To: Jumped

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test jumped

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
# Fixtures: config
```

## Step-by-Step Guide

### Step 1: Assign seed = value

```python
seed = config['seed']
```

**Verification:**
```python
assert mt19937.state['state']['pos'] == config['initial']['pos']
```

### Step 2: Assign steps = value

```python
steps = config['steps']
```

**Verification:**
```python
assert sha256.hexdigest() == config['initial']['key_sha256']
```

### Step 3: Assign mt19937 = MT19937(...)

```python
mt19937 = MT19937(seed)
```

**Verification:**
```python
assert jumped.state['state']['pos'] == config['jumped']['pos']
```

### Step 4: Call mt19937.random_raw()

```python
mt19937.random_raw(steps)
```

**Verification:**
```python
assert sha256.hexdigest() == config['jumped']['key_sha256']
```

### Step 5: Assign key = value

```python
key = mt19937.state['state']['key']
```

### Step 6: Assign sha256 = hashlib.sha256(...)

```python
sha256 = hashlib.sha256(key)
```

**Verification:**
```python
assert mt19937.state['state']['pos'] == config['initial']['pos']
```

### Step 7: Assign jumped = mt19937.jumped(...)

```python
jumped = mt19937.jumped()
```

### Step 8: Assign key = value

```python
key = jumped.state['state']['key']
```

### Step 9: Assign sha256 = hashlib.sha256(...)

```python
sha256 = hashlib.sha256(key)
```

**Verification:**
```python
assert jumped.state['state']['pos'] == config['jumped']['pos']
```

### Step 10: Assign key = key.byteswap(...)

```python
key = key.byteswap()
```

### Step 11: Assign key = key.byteswap(...)

```python
key = key.byteswap()
```


## Complete Example

```python
# Setup
# Fixtures: config

# Workflow
seed = config['seed']
steps = config['steps']
mt19937 = MT19937(seed)
mt19937.random_raw(steps)
key = mt19937.state['state']['key']
if sys.byteorder == 'big':
    key = key.byteswap()
sha256 = hashlib.sha256(key)
assert mt19937.state['state']['pos'] == config['initial']['pos']
assert sha256.hexdigest() == config['initial']['key_sha256']
jumped = mt19937.jumped()
key = jumped.state['state']['key']
if sys.byteorder == 'big':
    key = key.byteswap()
sha256 = hashlib.sha256(key)
assert jumped.state['state']['pos'] == config['jumped']['pos']
assert sha256.hexdigest() == config['jumped']['key_sha256']
```

## Next Steps


---

*Source: test_generator_mt19937.py:2651 | Complexity: Advanced | Last updated: 2026-06-02*