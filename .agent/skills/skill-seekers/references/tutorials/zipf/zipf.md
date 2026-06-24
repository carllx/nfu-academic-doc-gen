# How To: Zipf

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test zipf

## Prerequisites

**Required Modules:**
- `pickle`
- `dataclasses`
- `functools`
- `pytest`
- `numpy`
- `numpy.random`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign rg = value

```python
rg = self._create_rng().rg
```

**Verification:**
```python
assert_(len(vals) == 10)
```

### Step 2: Assign vec_1d = np.arange(...)

```python
vec_1d = np.arange(2.0, 102.0)
```

**Verification:**
```python
assert_(len(vals) == 100)
```

### Step 3: Assign vec_2d = value

```python
vec_2d = np.arange(2.0, 102.0)[None, :]
```

**Verification:**
```python
assert_(vals.shape == (1, 100))
```

### Step 4: Assign mat = np.arange.reshape(...)

```python
mat = np.arange(2.0, 102.0, 0.01).reshape((100, 100))
```

**Verification:**
```python
assert_(vals.shape == (100, 100))
```

### Step 5: Assign vals = rg.zipf(...)

```python
vals = rg.zipf(10, 10)
```

### Step 6: Call assert_()

```python
assert_(len(vals) == 10)
```

### Step 7: Assign vals = rg.zipf(...)

```python
vals = rg.zipf(vec_1d)
```

### Step 8: Call assert_()

```python
assert_(len(vals) == 100)
```

### Step 9: Assign vals = rg.zipf(...)

```python
vals = rg.zipf(vec_2d)
```

### Step 10: Call assert_()

```python
assert_(vals.shape == (1, 100))
```

### Step 11: Assign vals = rg.zipf(...)

```python
vals = rg.zipf(mat)
```

### Step 12: Call assert_()

```python
assert_(vals.shape == (100, 100))
```


## Complete Example

```python
# Workflow
rg = self._create_rng().rg
vec_1d = np.arange(2.0, 102.0)
vec_2d = np.arange(2.0, 102.0)[None, :]
mat = np.arange(2.0, 102.0, 0.01).reshape((100, 100))
vals = rg.zipf(10, 10)
assert_(len(vals) == 10)
vals = rg.zipf(vec_1d)
assert_(len(vals) == 100)
vals = rg.zipf(vec_2d)
assert_(vals.shape == (1, 100))
vals = rg.zipf(mat)
assert_(vals.shape == (100, 100))
```

## Next Steps


---

*Source: test_smoke.py:433 | Complexity: Advanced | Last updated: 2026-06-02*