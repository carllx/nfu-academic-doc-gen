# How To: Operators Shift

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test operators shift

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
assert shl == data_shl_a
```

### Step 2: Assign data_b = self._data(...)

```python
data_b = self._data(self._int_min(), reverse=True)
```

**Verification:**
```python
assert shr == data_shr_a
```

### Step 3: Assign unknown = value

```python
vdata_a, vdata_b = (self.load(data_a), self.load(data_b))
```

**Verification:**
```python
assert shli == data_shl_a
```

### Step 4: Assign data_shl_a = self.load(...)

```python
data_shl_a = self.load([a << count for a in data_a])
```

**Verification:**
```python
assert shri == data_shr_a
```

### Step 5: Assign shl = self.shl(...)

```python
shl = self.shl(vdata_a, count)
```

**Verification:**
```python
assert shl == data_shl_a
```

### Step 6: Assign data_shr_a = self.load(...)

```python
data_shr_a = self.load([a >> count for a in data_a])
```

### Step 7: Assign shr = self.shr(...)

```python
shr = self.shr(vdata_a, count)
```

**Verification:**
```python
assert shr == data_shr_a
```

### Step 8: Assign data_shl_a = self.load(...)

```python
data_shl_a = self.load([a << count for a in data_a])
```

### Step 9: Assign shli = self.shli(...)

```python
shli = self.shli(vdata_a, count)
```

**Verification:**
```python
assert shli == data_shl_a
```

### Step 10: Assign data_shr_a = self.load(...)

```python
data_shr_a = self.load([a >> count for a in data_a])
```

### Step 11: Assign shri = self.shri(...)

```python
shri = self.shri(vdata_a, count)
```

**Verification:**
```python
assert shri == data_shr_a
```


## Complete Example

```python
# Workflow
if self.sfx in ('u8', 's8'):
    return
data_a = self._data(self._int_max() - self.nlanes)
data_b = self._data(self._int_min(), reverse=True)
vdata_a, vdata_b = (self.load(data_a), self.load(data_b))
for count in range(self._scalar_size()):
    data_shl_a = self.load([a << count for a in data_a])
    shl = self.shl(vdata_a, count)
    assert shl == data_shl_a
    data_shr_a = self.load([a >> count for a in data_a])
    shr = self.shr(vdata_a, count)
    assert shr == data_shr_a
for count in range(1, self._scalar_size()):
    data_shl_a = self.load([a << count for a in data_a])
    shli = self.shli(vdata_a, count)
    assert shli == data_shl_a
    data_shr_a = self.load([a >> count for a in data_a])
    shri = self.shri(vdata_a, count)
    assert shri == data_shr_a
```

## Next Steps


---

*Source: test_simd.py:254 | Complexity: Advanced | Last updated: 2026-06-02*