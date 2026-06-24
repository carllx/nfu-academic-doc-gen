# How To: Arithmetic Fused

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test arithmetic fused

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

### Step 1: Assign unknown = value

```python
vdata_a, vdata_b, vdata_c = [self.load(self._data())] * 3
```

**Verification:**
```python
assert fma == data_fma
```

### Step 2: Assign vdata_cx2 = self.add(...)

```python
vdata_cx2 = self.add(vdata_c, vdata_c)
```

**Verification:**
```python
assert fms == data_fms
```

### Step 3: Assign data_fma = self.load(...)

```python
data_fma = self.load([a * b + c for a, b, c in zip(vdata_a, vdata_b, vdata_c)])
```

**Verification:**
```python
assert nfma == data_nfma
```

### Step 4: Assign fma = self.muladd(...)

```python
fma = self.muladd(vdata_a, vdata_b, vdata_c)
```

**Verification:**
```python
assert nfms == data_nfms
```

### Step 5: Assign fms = self.mulsub(...)

```python
fms = self.mulsub(vdata_a, vdata_b, vdata_c)
```

**Verification:**
```python
assert fmas[0::2] == list(data_fms)[0::2]
```

### Step 6: Assign data_fms = self.sub(...)

```python
data_fms = self.sub(data_fma, vdata_cx2)
```

**Verification:**
```python
assert fmas[1::2] == list(data_fma)[1::2]
```

### Step 7: Assign nfma = self.nmuladd(...)

```python
nfma = self.nmuladd(vdata_a, vdata_b, vdata_c)
```

### Step 8: Assign data_nfma = self.sub(...)

```python
data_nfma = self.sub(vdata_cx2, data_fma)
```

**Verification:**
```python
assert nfma == data_nfma
```

### Step 9: Assign nfms = self.nmulsub(...)

```python
nfms = self.nmulsub(vdata_a, vdata_b, vdata_c)
```

### Step 10: Assign data_nfms = self.mul(...)

```python
data_nfms = self.mul(data_fma, self.setall(-1))
```

**Verification:**
```python
assert nfms == data_nfms
```

### Step 11: Assign fmas = list(...)

```python
fmas = list(self.muladdsub(vdata_a, vdata_b, vdata_c))
```

**Verification:**
```python
assert fmas[0::2] == list(data_fms)[0::2]
```


## Complete Example

```python
# Workflow
vdata_a, vdata_b, vdata_c = [self.load(self._data())] * 3
vdata_cx2 = self.add(vdata_c, vdata_c)
data_fma = self.load([a * b + c for a, b, c in zip(vdata_a, vdata_b, vdata_c)])
fma = self.muladd(vdata_a, vdata_b, vdata_c)
assert fma == data_fma
fms = self.mulsub(vdata_a, vdata_b, vdata_c)
data_fms = self.sub(data_fma, vdata_cx2)
assert fms == data_fms
nfma = self.nmuladd(vdata_a, vdata_b, vdata_c)
data_nfma = self.sub(vdata_cx2, data_fma)
assert nfma == data_nfma
nfms = self.nmulsub(vdata_a, vdata_b, vdata_c)
data_nfms = self.mul(data_fma, self.setall(-1))
assert nfms == data_nfms
fmas = list(self.muladdsub(vdata_a, vdata_b, vdata_c))
assert fmas[0::2] == list(data_fms)[0::2]
assert fmas[1::2] == list(data_fma)[1::2]
```

## Next Steps


---

*Source: test_simd.py:373 | Complexity: Advanced | Last updated: 2026-06-02*