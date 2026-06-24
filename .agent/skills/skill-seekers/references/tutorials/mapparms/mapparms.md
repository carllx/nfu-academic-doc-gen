# How To: Mapparms

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test mapparms

## Prerequisites

**Required Modules:**
- `numpy`
- `numpy.polynomial.polyutils`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign dom1 = value

```python
dom1 = [0, 4]
```

**Verification:**
```python
assert_almost_equal(res, tgt)
```

### Step 2: Assign dom2 = value

```python
dom2 = [1, 3]
```

**Verification:**
```python
assert_almost_equal(res, tgt)
```

### Step 3: Assign tgt = value

```python
tgt = [1, 0.5]
```

### Step 4: Assign res = pu.mapparms(...)

```python
res = pu.mapparms(dom1, dom2)
```

### Step 5: Call assert_almost_equal()

```python
assert_almost_equal(res, tgt)
```

### Step 6: Assign dom1 = value

```python
dom1 = [0 - 1j, 2 + 1j]
```

### Step 7: Assign dom2 = value

```python
dom2 = [-2, 2]
```

### Step 8: Assign tgt = value

```python
tgt = [-1 + 1j, 1 - 1j]
```

### Step 9: Assign res = pu.mapparms(...)

```python
res = pu.mapparms(dom1, dom2)
```

### Step 10: Call assert_almost_equal()

```python
assert_almost_equal(res, tgt)
```


## Complete Example

```python
# Workflow
dom1 = [0, 4]
dom2 = [1, 3]
tgt = [1, 0.5]
res = pu.mapparms(dom1, dom2)
assert_almost_equal(res, tgt)
dom1 = [0 - 1j, 2 + 1j]
dom2 = [-2, 2]
tgt = [-1 + 1j, 1 - 1j]
res = pu.mapparms(dom1, dom2)
assert_almost_equal(res, tgt)
```

## Next Steps


---

*Source: test_polyutils.py:110 | Complexity: Advanced | Last updated: 2026-06-02*