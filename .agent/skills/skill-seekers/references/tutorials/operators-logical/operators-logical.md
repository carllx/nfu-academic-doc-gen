# How To: Operators Logical

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Logical operations for boolean types.
Test intrinsics:
    npyv_xor_##SFX, npyv_and_##SFX, npyv_or_##SFX, npyv_not_##SFX,
    npyv_andc_b8, npvy_orc_b8, nvpy_xnor_b8

## Prerequisites

**Required Modules:**
- `itertools`
- `math`
- `operator`
- `re`
- `pytest`
- `numpy._core._multiarray_umath`
- `numpy._core._simd`


## Step-by-Step Guide

### Step 1: '\n        Logical operations for boolean types.\n        Test intrinsics:\n            npyv_xor_##SFX, npyv_and_##SFX, npyv_or_##SFX, npyv_not_##SFX,\n            npyv_andc_b8, npvy_orc_b8, nvpy_xnor_b8\n        '

```python
'\n        Logical operations for boolean types.\n        Test intrinsics:\n            npyv_xor_##SFX, npyv_and_##SFX, npyv_or_##SFX, npyv_not_##SFX,\n            npyv_andc_b8, npvy_orc_b8, nvpy_xnor_b8\n        '
```

**Verification:**
```python
assert vand == data_and
```

### Step 2: Assign data_a = self._data(...)

```python
data_a = self._data()
```

**Verification:**
```python
assert vor == data_or
```

### Step 3: Assign data_b = self._data(...)

```python
data_b = self._data(reverse=True)
```

**Verification:**
```python
assert vxor == data_xor
```

### Step 4: Assign vdata_a = self._load_b(...)

```python
vdata_a = self._load_b(data_a)
```

**Verification:**
```python
assert vnot == data_b
```

### Step 5: Assign vdata_b = self._load_b(...)

```python
vdata_b = self._load_b(data_b)
```

**Verification:**
```python
assert data_andc == vandc
```

### Step 6: Assign data_and = value

```python
data_and = [a & b for a, b in zip(data_a, data_b)]
```

**Verification:**
```python
assert data_orc == vorc
```

### Step 7: Assign vand = getattr(...)

```python
vand = getattr(self, 'and')(vdata_a, vdata_b)
```

**Verification:**
```python
assert data_xnor == vxnor
```

### Step 8: Assign data_or = value

```python
data_or = [a | b for a, b in zip(data_a, data_b)]
```

### Step 9: Assign vor = getattr(...)

```python
vor = getattr(self, 'or')(vdata_a, vdata_b)
```

**Verification:**
```python
assert vor == data_or
```

### Step 10: Assign data_xor = value

```python
data_xor = [a ^ b for a, b in zip(data_a, data_b)]
```

### Step 11: Assign vxor = self.xor(...)

```python
vxor = self.xor(vdata_a, vdata_b)
```

**Verification:**
```python
assert vxor == data_xor
```

### Step 12: Assign vnot = getattr(...)

```python
vnot = getattr(self, 'not')(vdata_a)
```

**Verification:**
```python
assert vnot == data_b
```

### Step 13: Assign data_andc = value

```python
data_andc = [a & ~b & 255 for a, b in zip(data_a, data_b)]
```

### Step 14: Assign vandc = self.andc(...)

```python
vandc = self.andc(vdata_a, vdata_b)
```

**Verification:**
```python
assert data_andc == vandc
```

### Step 15: Assign data_orc = value

```python
data_orc = [(a | ~b) & 255 for a, b in zip(data_a, data_b)]
```

### Step 16: Assign vorc = self.orc(...)

```python
vorc = self.orc(vdata_a, vdata_b)
```

**Verification:**
```python
assert data_orc == vorc
```

### Step 17: Assign data_xnor = value

```python
data_xnor = [~(a ^ b) & 255 for a, b in zip(data_a, data_b)]
```

### Step 18: Assign vxnor = self.xnor(...)

```python
vxnor = self.xnor(vdata_a, vdata_b)
```

**Verification:**
```python
assert data_xnor == vxnor
```


## Complete Example

```python
# Workflow
'\n        Logical operations for boolean types.\n        Test intrinsics:\n            npyv_xor_##SFX, npyv_and_##SFX, npyv_or_##SFX, npyv_not_##SFX,\n            npyv_andc_b8, npvy_orc_b8, nvpy_xnor_b8\n        '
data_a = self._data()
data_b = self._data(reverse=True)
vdata_a = self._load_b(data_a)
vdata_b = self._load_b(data_b)
data_and = [a & b for a, b in zip(data_a, data_b)]
vand = getattr(self, 'and')(vdata_a, vdata_b)
assert vand == data_and
data_or = [a | b for a, b in zip(data_a, data_b)]
vor = getattr(self, 'or')(vdata_a, vdata_b)
assert vor == data_or
data_xor = [a ^ b for a, b in zip(data_a, data_b)]
vxor = self.xor(vdata_a, vdata_b)
assert vxor == data_xor
vnot = getattr(self, 'not')(vdata_a)
assert vnot == data_b
if self.sfx not in 'b8':
    return
data_andc = [a & ~b & 255 for a, b in zip(data_a, data_b)]
vandc = self.andc(vdata_a, vdata_b)
assert data_andc == vandc
data_orc = [(a | ~b) & 255 for a, b in zip(data_a, data_b)]
vorc = self.orc(vdata_a, vdata_b)
assert data_orc == vorc
data_xnor = [~(a ^ b) & 255 for a, b in zip(data_a, data_b)]
vxnor = self.xnor(vdata_a, vdata_b)
assert data_xnor == vxnor
```

## Next Steps


---

*Source: test_simd.py:147 | Complexity: Advanced | Last updated: 2026-06-02*