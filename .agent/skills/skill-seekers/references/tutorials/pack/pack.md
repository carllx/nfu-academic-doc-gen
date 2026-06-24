# How To: Pack

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Pack multiple vectors into one
Test intrinsics:
    npyv_pack_b8_b16
    npyv_pack_b8_b32
    npyv_pack_b8_b64

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

### Step 1: '\n        Pack multiple vectors into one\n        Test intrinsics:\n            npyv_pack_b8_b16\n            npyv_pack_b8_b32\n            npyv_pack_b8_b64\n        '

```python
'\n        Pack multiple vectors into one\n        Test intrinsics:\n            npyv_pack_b8_b16\n            npyv_pack_b8_b32\n            npyv_pack_b8_b64\n        '
```

**Verification:**
```python
assert vpack == spack
```

### Step 2: Assign data = self._data(...)

```python
data = self._data()
```

### Step 3: Assign rdata = self._data(...)

```python
rdata = self._data(reverse=True)
```

### Step 4: Assign vdata = self._load_b(...)

```python
vdata = self._load_b(data)
```

### Step 5: Assign vrdata = self._load_b(...)

```python
vrdata = self._load_b(rdata)
```

### Step 6: Assign pack_simd = getattr(...)

```python
pack_simd = getattr(self.npyv, f'pack_b8_{self.sfx}')
```

**Verification:**
```python
assert vpack == spack
```

### Step 7: Assign spack = value

```python
spack = [i & 255 for i in list(rdata) + list(data)]
```

### Step 8: Assign vpack = pack_simd(...)

```python
vpack = pack_simd(vrdata, vdata)
```

### Step 9: Assign spack = value

```python
spack = [i & 255 for i in 2 * list(rdata) + 2 * list(data)]
```

### Step 10: Assign vpack = pack_simd(...)

```python
vpack = pack_simd(vrdata, vrdata, vdata, vdata)
```

### Step 11: Assign spack = value

```python
spack = [i & 255 for i in 4 * list(rdata) + 4 * list(data)]
```

### Step 12: Assign vpack = pack_simd(...)

```python
vpack = pack_simd(vrdata, vrdata, vrdata, vrdata, vdata, vdata, vdata, vdata)
```


## Complete Example

```python
# Workflow
'\n        Pack multiple vectors into one\n        Test intrinsics:\n            npyv_pack_b8_b16\n            npyv_pack_b8_b32\n            npyv_pack_b8_b64\n        '
if self.sfx not in ('b16', 'b32', 'b64'):
    return
data = self._data()
rdata = self._data(reverse=True)
vdata = self._load_b(data)
vrdata = self._load_b(rdata)
pack_simd = getattr(self.npyv, f'pack_b8_{self.sfx}')
if self.sfx == 'b16':
    spack = [i & 255 for i in list(rdata) + list(data)]
    vpack = pack_simd(vrdata, vdata)
elif self.sfx == 'b32':
    spack = [i & 255 for i in 2 * list(rdata) + 2 * list(data)]
    vpack = pack_simd(vrdata, vrdata, vdata, vdata)
elif self.sfx == 'b64':
    spack = [i & 255 for i in 4 * list(rdata) + 4 * list(data)]
    vpack = pack_simd(vrdata, vrdata, vrdata, vrdata, vdata, vdata, vdata, vdata)
assert vpack == spack
```

## Next Steps


---

*Source: test_simd.py:199 | Complexity: Advanced | Last updated: 2026-06-02*