# How To: Asym

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test asym

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign x = array(...)

```python
x = array([1, 1, 2, 3, 4, 4, 4, 5])
```

**Verification:**
```python
assert_array_almost_equal(H, answer / 8.0, 3)
```

### Step 2: Assign y = array(...)

```python
y = array([1, 3, 2, 0, 1, 2, 3, 4])
```

**Verification:**
```python
assert_array_equal(xed, np.linspace(0, 6, 7))
```

### Step 3: Assign unknown = histogram2d(...)

```python
H, xed, yed = histogram2d(x, y, (6, 5), range=[[0, 6], [0, 5]], density=True)
```

**Verification:**
```python
assert_array_equal(yed, np.linspace(0, 5, 6))
```

### Step 4: Assign answer = array(...)

```python
answer = array([[0.0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 1]])
```

### Step 5: Call assert_array_almost_equal()

```python
assert_array_almost_equal(H, answer / 8.0, 3)
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(xed, np.linspace(0, 6, 7))
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(yed, np.linspace(0, 5, 6))
```


## Complete Example

```python
# Workflow
x = array([1, 1, 2, 3, 4, 4, 4, 5])
y = array([1, 3, 2, 0, 1, 2, 3, 4])
H, xed, yed = histogram2d(x, y, (6, 5), range=[[0, 6], [0, 5]], density=True)
answer = array([[0.0, 0, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [1, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 1]])
assert_array_almost_equal(H, answer / 8.0, 3)
assert_array_equal(xed, np.linspace(0, 6, 7))
assert_array_equal(yed, np.linspace(0, 5, 6))
```

## Next Steps


---

*Source: test_twodim_base.py:229 | Complexity: Intermediate | Last updated: 2026-06-02*