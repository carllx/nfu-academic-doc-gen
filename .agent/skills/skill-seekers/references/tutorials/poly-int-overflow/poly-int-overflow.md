# How To: Poly Int Overflow

**Difficulty**: Beginner
**Estimated Time**: 5 minutes
**Tags**: workflow, integration

## Overview

Workflow: Regression test for gh-5096.

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy.polynomial.polynomial`
- `numpy.testing`
- `decimal`


## Step-by-Step Guide

### Step 1: '\n        Regression test for gh-5096.\n        '

```python
'\n        Regression test for gh-5096.\n        '
```

**Verification:**
```python
assert_almost_equal(np.poly(v), np.poly(np.diag(v)))
```

### Step 2: Assign v = np.arange(...)

```python
v = np.arange(1, 21)
```

### Step 3: Call assert_almost_equal()

```python
assert_almost_equal(np.poly(v), np.poly(np.diag(v)))
```


## Complete Example

```python
# Workflow
'\n        Regression test for gh-5096.\n        '
v = np.arange(1, 21)
assert_almost_equal(np.poly(v), np.poly(np.diag(v)))
```

## Next Steps


---

*Source: test_polynomial.py:266 | Complexity: Beginner | Last updated: 2026-06-02*