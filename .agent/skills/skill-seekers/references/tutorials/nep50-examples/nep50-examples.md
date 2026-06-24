# How To: Nep50 Examples

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test nep50 examples

## Prerequisites

**Required Modules:**
- `operator`
- `hypothesis`
- `pytest`
- `hypothesis`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign res = value

```python
res = np.uint8(1) + 2
```

**Verification:**
```python
assert res.dtype == np.uint8
```

### Step 2: Assign res = value

```python
res = np.array([1], np.uint8) + np.int64(1)
```

**Verification:**
```python
assert res.dtype == np.int64
```

### Step 3: Assign res = value

```python
res = np.array([1], np.uint8) + np.array(1, dtype=np.int64)
```

**Verification:**
```python
assert res.dtype == np.int64
```

### Step 4: Assign res = value

```python
res = np.array([0.1], np.float32) == np.float64(0.1)
```

**Verification:**
```python
assert res.dtype == np.uint8
```

### Step 5: Assign res = value

```python
res = np.array([0.1], np.float32) + np.float64(0.1)
```

**Verification:**
```python
assert np.isinf(res)
```

### Step 6: Assign res = value

```python
res = np.array([1.0], np.float32) + np.int64(3)
```

**Verification:**
```python
assert res.dtype == np.float32
```

### Step 7: Assign res = value

```python
res = np.uint8(100) + 200
```

**Verification:**
```python
assert res[0] == False
```

### Step 8: Assign res = value

```python
res = np.float32(1) + 3e+100
```

**Verification:**
```python
assert res.dtype == np.float64
```


## Complete Example

```python
# Workflow
res = np.uint8(1) + 2
assert res.dtype == np.uint8
res = np.array([1], np.uint8) + np.int64(1)
assert res.dtype == np.int64
res = np.array([1], np.uint8) + np.array(1, dtype=np.int64)
assert res.dtype == np.int64
with pytest.warns(RuntimeWarning, match='overflow'):
    res = np.uint8(100) + 200
assert res.dtype == np.uint8
with pytest.warns(RuntimeWarning, match='overflow'):
    res = np.float32(1) + 3e+100
assert np.isinf(res)
assert res.dtype == np.float32
res = np.array([0.1], np.float32) == np.float64(0.1)
assert res[0] == False
res = np.array([0.1], np.float32) + np.float64(0.1)
assert res.dtype == np.float64
res = np.array([1.0], np.float32) + np.int64(3)
assert res.dtype == np.float64
```

## Next Steps


---

*Source: test_nep50_promotions.py:18 | Complexity: Advanced | Last updated: 2026-06-02*