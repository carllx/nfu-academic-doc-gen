# How To: Copies

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test copies

## Prerequisites

**Required Modules:**
- `inspect`
- `itertools`
- `math`
- `platform`
- `sys`
- `warnings`
- `decimal`
- `pytest`
- `hypothesis`
- `hypothesis.extra`
- `numpy`
- `numpy`
- `numpy._core`
- `numpy._core._rational_tests`
- `numpy._core.numerictypes`
- `numpy.exceptions`
- `numpy.random`
- `numpy.testing`
- `fractions`
- `numbers`
- `itertools`


## Step-by-Step Guide

### Step 1: Assign A = np.array(...)

```python
A = np.array([[1, 2], [3, 4]])
```

**Verification:**
```python
assert_equal(np.resize(A, (2, 4)), Ar1)
```

### Step 2: Assign Ar1 = np.array(...)

```python
Ar1 = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
```

**Verification:**
```python
assert_equal(np.resize(A, (4, 2)), Ar2)
```

### Step 3: Call assert_equal()

```python
assert_equal(np.resize(A, (2, 4)), Ar1)
```

**Verification:**
```python
assert_equal(np.resize(A, (4, 3)), Ar3)
```

### Step 4: Assign Ar2 = np.array(...)

```python
Ar2 = np.array([[1, 2], [3, 4], [1, 2], [3, 4]])
```

### Step 5: Call assert_equal()

```python
assert_equal(np.resize(A, (4, 2)), Ar2)
```

### Step 6: Assign Ar3 = np.array(...)

```python
Ar3 = np.array([[1, 2, 3], [4, 1, 2], [3, 4, 1], [2, 3, 4]])
```

### Step 7: Call assert_equal()

```python
assert_equal(np.resize(A, (4, 3)), Ar3)
```


## Complete Example

```python
# Workflow
A = np.array([[1, 2], [3, 4]])
Ar1 = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
assert_equal(np.resize(A, (2, 4)), Ar1)
Ar2 = np.array([[1, 2], [3, 4], [1, 2], [3, 4]])
assert_equal(np.resize(A, (4, 2)), Ar2)
Ar3 = np.array([[1, 2, 3], [4, 1, 2], [3, 4, 1], [2, 3, 4]])
assert_equal(np.resize(A, (4, 3)), Ar3)
```

## Next Steps


---

*Source: test_numeric.py:36 | Complexity: Intermediate | Last updated: 2026-06-02*