# How To: Modular Power

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test modular power

## Prerequisites

**Required Modules:**
- `contextlib`
- `itertools`
- `operator`
- `platform`
- `sys`
- `warnings`
- `pytest`
- `hypothesis`
- `hypothesis.extra`
- `hypothesis.strategies`
- `numpy`
- `numpy._core._rational_tests`
- `numpy._utils`
- `numpy.exceptions`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign a = 5

```python
a = 5
```

**Verification:**
```python
assert_raises(TypeError, operator.pow, t(a), b, c)
```

### Step 2: Assign b = 4

```python
b = 4
```

**Verification:**
```python
assert_raises(TypeError, operator.pow, np.array(t(a)), b, c)
```

### Step 3: Assign c = 10

```python
c = 10
```

### Step 4: Assign expected = pow(...)

```python
expected = pow(a, b, c)
```

### Step 5: Call assert_raises()

```python
assert_raises(TypeError, operator.pow, t(a), b, c)
```

### Step 6: Call assert_raises()

```python
assert_raises(TypeError, operator.pow, np.array(t(a)), b, c)
```


## Complete Example

```python
# Workflow
a = 5
b = 4
c = 10
expected = pow(a, b, c)
for t in (np.int32, np.float32, np.complex64):
    assert_raises(TypeError, operator.pow, t(a), b, c)
    assert_raises(TypeError, operator.pow, np.array(t(a)), b, c)
```

## Next Steps


---

*Source: test_scalarmath.py:274 | Complexity: Intermediate | Last updated: 2026-06-02*