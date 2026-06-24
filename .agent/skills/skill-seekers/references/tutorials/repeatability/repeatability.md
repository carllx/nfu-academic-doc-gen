# How To: Repeatability

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test repeatability

## Prerequisites

**Required Modules:**
- `sys`
- `warnings`
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`
- `hashlib`
- `threading`


## Step-by-Step Guide

### Step 1: Assign tgt = value

```python
tgt = {'bool': '509aea74d792fb931784c4b0135392c65aec64beee12b0cc167548a2c3d31e71', 'int16': '7b07f1a920e46f6d0fe02314155a2330bcfd7635e708da50e536c5ebb631a7d4', 'int32': 'e577bfed6c935de944424667e3da285012e741892dcb7051a8f1ce68ab05c92f', 'int64': '0fbead0b06759df2cfb55e43148822d4a1ff953c7eb19a5b08445a63bb64fa9e', 'int8': '001aac3a5acb935a9b186cbe14a1ca064b8bb2dd0b045d48abeacf74d0203404', 'uint16': '7b07f1a920e46f6d0fe02314155a2330bcfd7635e708da50e536c5ebb631a7d4', 'uint32': 'e577bfed6c935de944424667e3da285012e741892dcb7051a8f1ce68ab05c92f', 'uint64': '0fbead0b06759df2cfb55e43148822d4a1ff953c7eb19a5b08445a63bb64fa9e', 'uint8': '001aac3a5acb935a9b186cbe14a1ca064b8bb2dd0b045d48abeacf74d0203404'}
```

**Verification:**
```python
assert_(tgt[np.dtype(dt).name] == res)
```

### Step 2: Assign rng = random.RandomState(...)

```python
rng = random.RandomState(1234)
```

**Verification:**
```python
assert_(tgt[np.dtype(bool).name] == res)
```

### Step 3: Assign val = rng.randint.view(...)

```python
val = rng.randint(0, 2, size=1000, dtype=bool).view(np.int8)
```

### Step 4: Assign res = hashlib.sha256.hexdigest(...)

```python
res = hashlib.sha256(val).hexdigest()
```

### Step 5: Call assert_()

```python
assert_(tgt[np.dtype(bool).name] == res)
```

### Step 6: Assign rng = random.RandomState(...)

```python
rng = random.RandomState(1234)
```

### Step 7: Assign res = hashlib.sha256.hexdigest(...)

```python
res = hashlib.sha256(val.view(np.int8)).hexdigest()
```

### Step 8: Call assert_()

```python
assert_(tgt[np.dtype(dt).name] == res)
```

### Step 9: Assign val = rng.randint(...)

```python
val = rng.randint(0, 6, size=1000, dtype=dt)
```

### Step 10: Assign val = rng.randint.byteswap(...)

```python
val = rng.randint(0, 6, size=1000, dtype=dt).byteswap()
```


## Complete Example

```python
# Workflow
import hashlib
tgt = {'bool': '509aea74d792fb931784c4b0135392c65aec64beee12b0cc167548a2c3d31e71', 'int16': '7b07f1a920e46f6d0fe02314155a2330bcfd7635e708da50e536c5ebb631a7d4', 'int32': 'e577bfed6c935de944424667e3da285012e741892dcb7051a8f1ce68ab05c92f', 'int64': '0fbead0b06759df2cfb55e43148822d4a1ff953c7eb19a5b08445a63bb64fa9e', 'int8': '001aac3a5acb935a9b186cbe14a1ca064b8bb2dd0b045d48abeacf74d0203404', 'uint16': '7b07f1a920e46f6d0fe02314155a2330bcfd7635e708da50e536c5ebb631a7d4', 'uint32': 'e577bfed6c935de944424667e3da285012e741892dcb7051a8f1ce68ab05c92f', 'uint64': '0fbead0b06759df2cfb55e43148822d4a1ff953c7eb19a5b08445a63bb64fa9e', 'uint8': '001aac3a5acb935a9b186cbe14a1ca064b8bb2dd0b045d48abeacf74d0203404'}
for dt in self.itype[1:]:
    rng = random.RandomState(1234)
    if sys.byteorder == 'little':
        val = rng.randint(0, 6, size=1000, dtype=dt)
    else:
        val = rng.randint(0, 6, size=1000, dtype=dt).byteswap()
    res = hashlib.sha256(val.view(np.int8)).hexdigest()
    assert_(tgt[np.dtype(dt).name] == res)
rng = random.RandomState(1234)
val = rng.randint(0, 2, size=1000, dtype=bool).view(np.int8)
res = hashlib.sha256(val).hexdigest()
assert_(tgt[np.dtype(bool).name] == res)
```

## Next Steps


---

*Source: test_random.py:231 | Complexity: Advanced | Last updated: 2026-06-02*