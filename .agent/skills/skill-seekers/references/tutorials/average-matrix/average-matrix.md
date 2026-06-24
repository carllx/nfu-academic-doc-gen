# How To: Average Matrix

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test average matrix

## Prerequisites

**Required Modules:**
- `textwrap`
- `warnings`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign y = np.matrix(...)

```python
y = np.matrix(np.random.rand(5, 5))
```

**Verification:**
```python
assert_array_equal(y.mean(0), np.average(y, 0))
```

### Step 2: Call assert_array_equal()

```python
assert_array_equal(y.mean(0), np.average(y, 0))
```

**Verification:**
```python
assert_equal(type(r), np.matrix)
```

### Step 3: Assign a = np.matrix(...)

```python
a = np.matrix([[1, 2], [3, 4]])
```

**Verification:**
```python
assert_equal(r, [[2.5, 10.0 / 3]])
```

### Step 4: Assign w = np.matrix(...)

```python
w = np.matrix([[1, 2], [3, 4]])
```

### Step 5: Assign r = np.average(...)

```python
r = np.average(a, axis=0, weights=w)
```

### Step 6: Call assert_equal()

```python
assert_equal(type(r), np.matrix)
```

### Step 7: Call assert_equal()

```python
assert_equal(r, [[2.5, 10.0 / 3]])
```


## Complete Example

```python
# Workflow
y = np.matrix(np.random.rand(5, 5))
assert_array_equal(y.mean(0), np.average(y, 0))
a = np.matrix([[1, 2], [3, 4]])
w = np.matrix([[1, 2], [3, 4]])
r = np.average(a, axis=0, weights=w)
assert_equal(type(r), np.matrix)
assert_equal(r, [[2.5, 10.0 / 3]])
```

## Next Steps


---

*Source: test_interaction.py:237 | Complexity: Intermediate | Last updated: 2026-06-02*