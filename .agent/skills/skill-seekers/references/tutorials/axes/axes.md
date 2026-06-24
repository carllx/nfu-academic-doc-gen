# How To: Axes

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test axes

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `queue`
- `threading`
- `pytest`
- `numpy`
- `numpy.random`
- `numpy.testing`

**Setup Required:**
```python
# Fixtures: op
```

## Step-by-Step Guide

### Step 1: Assign x = random(...)

```python
x = random((30, 20, 10))
```

**Verification:**
```python
assert_allclose(op_tr, tr_op, atol=1e-06)
```

### Step 2: Assign axes = value

```python
axes = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
```

### Step 3: Assign op_tr = op(...)

```python
op_tr = op(np.transpose(x, a))
```

### Step 4: Assign tr_op = np.transpose(...)

```python
tr_op = np.transpose(op(x, axes=a), a)
```

### Step 5: Call assert_allclose()

```python
assert_allclose(op_tr, tr_op, atol=1e-06)
```


## Complete Example

```python
# Setup
# Fixtures: op

# Workflow
x = random((30, 20, 10))
axes = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
for a in axes:
    op_tr = op(np.transpose(x, a))
    tr_op = np.transpose(op(x, axes=a), a)
    assert_allclose(op_tr, tr_op, atol=1e-06)
```

## Next Steps


---

*Source: test_pocketfft.py:355 | Complexity: Intermediate | Last updated: 2026-06-02*