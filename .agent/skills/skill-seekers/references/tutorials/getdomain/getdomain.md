# How To: Getdomain

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test getdomain

## Prerequisites

**Required Modules:**
- `numpy`
- `numpy.polynomial.polyutils`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign x = value

```python
x = [1, 10, 3, -1]
```

**Verification:**
```python
assert_almost_equal(res, tgt)
```

### Step 2: Assign tgt = value

```python
tgt = [-1, 10]
```

**Verification:**
```python
assert_almost_equal(res, tgt)
```

### Step 3: Assign res = pu.getdomain(...)

```python
res = pu.getdomain(x)
```

### Step 4: Call assert_almost_equal()

```python
assert_almost_equal(res, tgt)
```

### Step 5: Assign x = value

```python
x = [1 + 1j, 1 - 1j, 0, 2]
```

### Step 6: Assign tgt = value

```python
tgt = [-1j, 2 + 1j]
```

### Step 7: Assign res = pu.getdomain(...)

```python
res = pu.getdomain(x)
```

### Step 8: Call assert_almost_equal()

```python
assert_almost_equal(res, tgt)
```


## Complete Example

```python
# Workflow
x = [1, 10, 3, -1]
tgt = [-1, 10]
res = pu.getdomain(x)
assert_almost_equal(res, tgt)
x = [1 + 1j, 1 - 1j, 0, 2]
tgt = [-1j, 2 + 1j]
res = pu.getdomain(x)
assert_almost_equal(res, tgt)
```

## Next Steps


---

*Source: test_polyutils.py:63 | Complexity: Advanced | Last updated: 2026-06-02*