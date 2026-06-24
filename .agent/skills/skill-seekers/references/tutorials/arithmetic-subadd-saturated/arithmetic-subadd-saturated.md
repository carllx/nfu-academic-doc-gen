# How To: Arithmetic Subadd Saturated

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test arithmetic subadd saturated

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

### Step 1: Assign data_a = self._data(...)

```python
data_a = self._data(self._int_max() - self.nlanes)
```

**Verification:**
```python
assert adds == data_adds
```

### Step 2: Assign data_b = self._data(...)

```python
data_b = self._data(self._int_min(), reverse=True)
```

**Verification:**
```python
assert subs == data_subs
```

### Step 3: Assign unknown = value

```python
vdata_a, vdata_b = (self.load(data_a), self.load(data_b))
```

### Step 4: Assign data_adds = self._int_clip(...)

```python
data_adds = self._int_clip([a + b for a, b in zip(data_a, data_b)])
```

### Step 5: Assign adds = self.adds(...)

```python
adds = self.adds(vdata_a, vdata_b)
```

**Verification:**
```python
assert adds == data_adds
```

### Step 6: Assign data_subs = self._int_clip(...)

```python
data_subs = self._int_clip([a - b for a, b in zip(data_a, data_b)])
```

### Step 7: Assign subs = self.subs(...)

```python
subs = self.subs(vdata_a, vdata_b)
```

**Verification:**
```python
assert subs == data_subs
```


## Complete Example

```python
# Workflow
if self.sfx in ('u32', 's32', 'u64', 's64'):
    return
data_a = self._data(self._int_max() - self.nlanes)
data_b = self._data(self._int_min(), reverse=True)
vdata_a, vdata_b = (self.load(data_a), self.load(data_b))
data_adds = self._int_clip([a + b for a, b in zip(data_a, data_b)])
adds = self.adds(vdata_a, vdata_b)
assert adds == data_adds
data_subs = self._int_clip([a - b for a, b in zip(data_a, data_b)])
subs = self.subs(vdata_a, vdata_b)
assert subs == data_subs
```

## Next Steps


---

*Source: test_simd.py:288 | Complexity: Intermediate | Last updated: 2026-06-02*