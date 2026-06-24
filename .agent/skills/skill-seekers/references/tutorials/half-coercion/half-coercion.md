# How To: Half Coercion

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test that half gets coerced properly with the other types

## Prerequisites

**Required Modules:**
- `platform`
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: 'Test that half gets coerced properly with the other types'

```python
'Test that half gets coerced properly with the other types'
```

**Verification:**
```python
assert np.power(a16, 2).dtype == float16
```

### Step 2: Assign a16 = np.array(...)

```python
a16 = np.array((1,), dtype=float16)
```

**Verification:**
```python
assert np.power(a16, 2.0).dtype == float16
```

### Step 3: Assign a32 = np.array(...)

```python
a32 = np.array((1,), dtype=float32)
```

**Verification:**
```python
assert np.power(a16, b16).dtype == float16
```

### Step 4: Assign b16 = float16(...)

```python
b16 = float16(1)
```

**Verification:**
```python
assert np.power(a16, b32).dtype == float32
```

### Step 5: Assign b32 = float32(...)

```python
b32 = float32(1)
```

**Verification:**
```python
assert np.power(a16, a16).dtype == float16
```


## Complete Example

```python
# Workflow
'Test that half gets coerced properly with the other types'
a16 = np.array((1,), dtype=float16)
a32 = np.array((1,), dtype=float32)
b16 = float16(1)
b32 = float32(1)
assert np.power(a16, 2).dtype == float16
assert np.power(a16, 2.0).dtype == float16
assert np.power(a16, b16).dtype == float16
assert np.power(a16, b32).dtype == float32
assert np.power(a16, a16).dtype == float16
assert np.power(a16, a32).dtype == float32
assert np.power(b16, 2).dtype == float16
assert np.power(b16, 2.0).dtype == float16
assert np.power(b16, b16).dtype, float16
assert np.power(b16, b32).dtype, float32
assert np.power(b16, a16).dtype, float16
assert np.power(b16, a32).dtype, float32
assert np.power(a32, a16).dtype == float32
assert np.power(a32, b16).dtype == float32
assert np.power(b32, a16).dtype == float32
assert np.power(b32, b16).dtype == float32
```

## Next Steps


---

*Source: test_half.py:488 | Complexity: Intermediate | Last updated: 2026-06-02*