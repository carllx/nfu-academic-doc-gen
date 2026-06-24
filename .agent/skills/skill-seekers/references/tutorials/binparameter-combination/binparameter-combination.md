# How To: Binparameter Combination

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test binparameter combination

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign x = array(...)

```python
x = array([0, 0.09207008, 0.64575234, 0.12875982, 0.47390599, 0.59944483, 1])
```

**Verification:**
```python
assert_array_equal(H, answer)
```

### Step 2: Assign y = array(...)

```python
y = array([0, 0.14344267, 0.48988575, 0.30558665, 0.44700682, 0.15886423, 1])
```

**Verification:**
```python
assert_array_equal(ye, array([0.0, 0.25, 0.5, 0.75, 1]))
```

### Step 3: Assign edges = value

```python
edges = (0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1)
```

**Verification:**
```python
assert_array_equal(H, answer)
```

### Step 4: Assign unknown = histogram2d(...)

```python
H, xe, ye = histogram2d(x, y, (edges, 4))
```

**Verification:**
```python
assert_array_equal(xe, array([0.0, 0.25, 0.5, 0.75, 1]))
```

### Step 5: Assign answer = array(...)

```python
answer = array([[2.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]])
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(H, answer)
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(ye, array([0.0, 0.25, 0.5, 0.75, 1]))
```

### Step 8: Assign unknown = histogram2d(...)

```python
H, xe, ye = histogram2d(x, y, (4, edges))
```

### Step 9: Assign answer = array(...)

```python
answer = array([[1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]])
```

### Step 10: Call assert_array_equal()

```python
assert_array_equal(H, answer)
```

### Step 11: Call assert_array_equal()

```python
assert_array_equal(xe, array([0.0, 0.25, 0.5, 0.75, 1]))
```


## Complete Example

```python
# Workflow
x = array([0, 0.09207008, 0.64575234, 0.12875982, 0.47390599, 0.59944483, 1])
y = array([0, 0.14344267, 0.48988575, 0.30558665, 0.44700682, 0.15886423, 1])
edges = (0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1)
H, xe, ye = histogram2d(x, y, (edges, 4))
answer = array([[2.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [1.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 1.0]])
assert_array_equal(H, answer)
assert_array_equal(ye, array([0.0, 0.25, 0.5, 0.75, 1]))
H, xe, ye = histogram2d(x, y, (4, edges))
answer = array([[1.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0]])
assert_array_equal(H, answer)
assert_array_equal(xe, array([0.0, 0.25, 0.5, 0.75, 1]))
```

## Next Steps


---

*Source: test_twodim_base.py:267 | Complexity: Advanced | Last updated: 2026-06-02*