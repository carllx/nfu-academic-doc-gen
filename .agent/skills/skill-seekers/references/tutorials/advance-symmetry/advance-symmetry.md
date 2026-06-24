# How To: Advance Symmetry

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test advance symmetry

## Prerequisites

**Required Modules:**
- `os`
- `sys`
- `os.path`
- `pytest`
- `numpy`
- `numpy.random`
- `numpy.random._common`
- `numpy.testing`
- `cffi`
- `ctypes`
- `numpy.random.bit_generator`
- `numpy.random.bit_generator`
- `pickle`
- `pickle`
- `gzip`
- `pickle`


## Step-by-Step Guide

### Step 1: Assign rs = Generator(...)

```python
rs = Generator(self.bit_generator(*self.data1['seed']))
```

**Verification:**
```python
assert val_neg == val_pos
```

### Step 2: Assign state = value

```python
state = rs.bit_generator.state
```

**Verification:**
```python
assert val_big == val_pos
```

### Step 3: Assign step = value

```python
step = -210306068529402873148182252916320501760
```

### Step 4: Call rs.bit_generator.advance()

```python
rs.bit_generator.advance(step)
```

### Step 5: Assign val_neg = rs.integers(...)

```python
val_neg = rs.integers(10)
```

### Step 6: Assign rs.bit_generator.state = state

```python
rs.bit_generator.state = state
```

### Step 7: Call rs.bit_generator.advance()

```python
rs.bit_generator.advance(2 ** 128 + step)
```

### Step 8: Assign val_pos = rs.integers(...)

```python
val_pos = rs.integers(10)
```

### Step 9: Assign rs.bit_generator.state = state

```python
rs.bit_generator.state = state
```

### Step 10: Call rs.bit_generator.advance()

```python
rs.bit_generator.advance(10 * 2 ** 128 + step)
```

### Step 11: Assign val_big = rs.integers(...)

```python
val_big = rs.integers(10)
```

**Verification:**
```python
assert val_neg == val_pos
```


## Complete Example

```python
# Workflow
rs = Generator(self.bit_generator(*self.data1['seed']))
state = rs.bit_generator.state
step = -210306068529402873148182252916320501760
rs.bit_generator.advance(step)
val_neg = rs.integers(10)
rs.bit_generator.state = state
rs.bit_generator.advance(2 ** 128 + step)
val_pos = rs.integers(10)
rs.bit_generator.state = state
rs.bit_generator.advance(10 * 2 ** 128 + step)
val_big = rs.integers(10)
assert val_neg == val_pos
assert val_big == val_pos
```

## Next Steps


---

*Source: test_direct.py:421 | Complexity: Advanced | Last updated: 2026-06-02*