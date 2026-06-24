# How To: Assignment By Condition 2

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test assignment by condition 2

## Prerequisites

**Required Modules:**
- `pickle`
- `functools`
- `pytest`
- `numpy`
- `numpy._core.fromnumeric`
- `numpy._core.umath`
- `numpy.ma`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign a = masked_array(...)

```python
a = masked_array([0, 1], mask=[False, False])
```

**Verification:**
```python
assert_equal(b.mask, expected_mask)
```

### Step 2: Assign b = masked_array(...)

```python
b = masked_array([0, 1], mask=[True, True])
```

### Step 3: Assign mask = value

```python
mask = a < 1
```

### Step 4: Assign unknown = value

```python
b[mask] = a[mask]
```

### Step 5: Assign expected_mask = value

```python
expected_mask = [False, True]
```

### Step 6: Call assert_equal()

```python
assert_equal(b.mask, expected_mask)
```


## Complete Example

```python
# Workflow
a = masked_array([0, 1], mask=[False, False])
b = masked_array([0, 1], mask=[True, True])
mask = a < 1
b[mask] = a[mask]
expected_mask = [False, True]
assert_equal(b.mask, expected_mask)
```

## Next Steps


---

*Source: test_old_ma.py:769 | Complexity: Intermediate | Last updated: 2026-06-02*