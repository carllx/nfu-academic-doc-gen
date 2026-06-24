# How To: Uniform Array

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test uniform array

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
assert_(len(r) == 10)
```

### Step 2: Assign r = rg.uniform(...)

```python
r = rg.uniform(np.array([-1.0] * 10), 0.0, size=10)
```

**Verification:**
```python
assert_((r > -1).all())
```

### Step 3: Call assert_()

```python
assert_(len(r) == 10)
```

**Verification:**
```python
assert_((r <= 0).all())
```

### Step 4: Call assert_()

```python
assert_((r > -1).all())
```

**Verification:**
```python
assert_(len(r) == 10)
```

### Step 5: Call assert_()

```python
assert_((r <= 0).all())
```

**Verification:**
```python
assert_((r > -1).all())
```

### Step 6: Assign r = rg.uniform(...)

```python
r = rg.uniform(np.array([-1.0] * 10), np.array([0.0] * 10), size=10)
```

**Verification:**
```python
assert_((r <= 0).all())
```

### Step 7: Call assert_()

```python
assert_(len(r) == 10)
```

**Verification:**
```python
assert_(len(r) == 10)
```

### Step 8: Call assert_()

```python
assert_((r > -1).all())
```

**Verification:**
```python
assert_((r > -1).all())
```

### Step 9: Call assert_()

```python
assert_((r <= 0).all())
```

**Verification:**
```python
assert_((r <= 0).all())
```

### Step 10: Assign r = rg.uniform(...)

```python
r = rg.uniform(-1.0, np.array([0.0] * 10), size=10)
```

### Step 11: Call assert_()

```python
assert_(len(r) == 10)
```

### Step 12: Call assert_()

```python
assert_((r > -1).all())
```

### Step 13: Call assert_()

```python
assert_((r <= 0).all())
```


## Complete Example

```python
# Workflow
rg = self._create_rng().rg
r = rg.uniform(np.array([-1.0] * 10), 0.0, size=10)
assert_(len(r) == 10)
assert_((r > -1).all())
assert_((r <= 0).all())
r = rg.uniform(np.array([-1.0] * 10), np.array([0.0] * 10), size=10)
assert_(len(r) == 10)
assert_((r > -1).all())
assert_((r <= 0).all())
r = rg.uniform(-1.0, np.array([0.0] * 10), size=10)
assert_(len(r) == 10)
assert_((r > -1).all())
assert_((r <= 0).all())
```

## Next Steps


---

*Source: test_smoke.py:157 | Complexity: Advanced | Last updated: 2026-06-02*