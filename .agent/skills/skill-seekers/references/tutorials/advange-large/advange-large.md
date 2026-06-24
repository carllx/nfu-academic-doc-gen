# How To: Advange Large

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test advange large

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
rs = Generator(self.bit_generator(38219308213743))
```

**Verification:**
```python
assert state['state'] == initial_state
```

### Step 2: Assign pcg = value

```python
pcg = rs.bit_generator
```

**Verification:**
```python
assert state['state'] == advanced_state
```

### Step 3: Assign state = value

```python
state = pcg.state['state']
```

### Step 4: Assign initial_state = 287608843259529770491897792873167516365

```python
initial_state = 287608843259529770491897792873167516365
```

**Verification:**
```python
assert state['state'] == initial_state
```

### Step 5: Call pcg.advance()

```python
pcg.advance(sum((2 ** i for i in (96, 64, 32, 16, 8, 4, 2, 1))))
```

### Step 6: Assign state = value

```python
state = pcg.state['state']
```

### Step 7: Assign advanced_state = 135275564607035429730177404003164635391

```python
advanced_state = 135275564607035429730177404003164635391
```

**Verification:**
```python
assert state['state'] == advanced_state
```


## Complete Example

```python
# Workflow
rs = Generator(self.bit_generator(38219308213743))
pcg = rs.bit_generator
state = pcg.state['state']
initial_state = 287608843259529770491897792873167516365
assert state['state'] == initial_state
pcg.advance(sum((2 ** i for i in (96, 64, 32, 16, 8, 4, 2, 1))))
state = pcg.state['state']
advanced_state = 135275564607035429730177404003164635391
assert state['state'] == advanced_state
```

## Next Steps


---

*Source: test_direct.py:436 | Complexity: Intermediate | Last updated: 2026-06-02*