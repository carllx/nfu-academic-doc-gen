# How To: Polynomial Str Domains

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test polynomial str domains

## Prerequisites

**Required Modules:**
- `decimal`
- `fractions`
- `math`
- `pytest`
- `numpy.polynomial`
- `numpy._core`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign res = str(...)

```python
res = str(poly.Polynomial([0, 1]))
```

**Verification:**
```python
assert_equal(res, tgt)
```

### Step 2: Assign tgt = '0.0 + 1.0 x'

```python
tgt = '0.0 + 1.0 x'
```

**Verification:**
```python
assert_equal(res, tgt)
```

### Step 3: Call assert_equal()

```python
assert_equal(res, tgt)
```

### Step 4: Assign res = str(...)

```python
res = str(poly.Polynomial([0, 1], domain=[1, 2]))
```

### Step 5: Assign tgt = '0.0 + 1.0 (-3.0 + 2.0x)'

```python
tgt = '0.0 + 1.0 (-3.0 + 2.0x)'
```

### Step 6: Call assert_equal()

```python
assert_equal(res, tgt)
```


## Complete Example

```python
# Workflow
res = str(poly.Polynomial([0, 1]))
tgt = '0.0 + 1.0 x'
assert_equal(res, tgt)
res = str(poly.Polynomial([0, 1], domain=[1, 2]))
tgt = '0.0 + 1.0 (-3.0 + 2.0x)'
assert_equal(res, tgt)
```

## Next Steps


---

*Source: test_printing.py:174 | Complexity: Intermediate | Last updated: 2026-06-02*