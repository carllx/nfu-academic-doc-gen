# How To: Beta

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test beta

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

### Step 2: Assign vals = rg.beta(...)

```python
vals = rg.beta(2.0, 2.0, 10)
```

**Verification:**
```python
assert_(len(vals) == 10)
```

### Step 3: Call assert_()

```python
assert_(len(vals) == 10)
```

**Verification:**
```python
assert_(len(vals) == 10)
```

### Step 4: Assign vals = rg.beta(...)

```python
vals = rg.beta(np.array([2.0] * 10), 2.0)
```

**Verification:**
```python
assert_(len(vals) == 10)
```

### Step 5: Call assert_()

```python
assert_(len(vals) == 10)
```

**Verification:**
```python
assert_(vals.shape == (10, 10))
```

### Step 6: Assign vals = rg.beta(...)

```python
vals = rg.beta(2.0, np.array([2.0] * 10))
```

### Step 7: Call assert_()

```python
assert_(len(vals) == 10)
```

### Step 8: Assign vals = rg.beta(...)

```python
vals = rg.beta(np.array([2.0] * 10), np.array([2.0] * 10))
```

### Step 9: Call assert_()

```python
assert_(len(vals) == 10)
```

### Step 10: Assign vals = rg.beta(...)

```python
vals = rg.beta(np.array([2.0] * 10), np.array([[2.0]] * 10))
```

### Step 11: Call assert_()

```python
assert_(vals.shape == (10, 10))
```


## Complete Example

```python
# Workflow
rg = self._create_rng().rg
vals = rg.beta(2.0, 2.0, 10)
assert_(len(vals) == 10)
vals = rg.beta(np.array([2.0] * 10), 2.0)
assert_(len(vals) == 10)
vals = rg.beta(2.0, np.array([2.0] * 10))
assert_(len(vals) == 10)
vals = rg.beta(np.array([2.0] * 10), np.array([2.0] * 10))
assert_(len(vals) == 10)
vals = rg.beta(np.array([2.0] * 10), np.array([[2.0]] * 10))
assert_(vals.shape == (10, 10))
```

## Next Steps


---

*Source: test_smoke.py:297 | Complexity: Advanced | Last updated: 2026-06-02*