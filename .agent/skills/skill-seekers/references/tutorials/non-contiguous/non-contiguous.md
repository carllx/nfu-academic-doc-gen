# How To: Non Contiguous

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test non contiguous

## Prerequisites

**Required Modules:**
- `sys`
- `pytest`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign x = np.arange.reshape(...)

```python
x = np.arange(25).reshape((5, 5))
```

**Verification:**
```python
assert_array_equal(y1, np.from_dlpack(y1))
```

### Step 2: Assign y1 = value

```python
y1 = x[0]
```

**Verification:**
```python
assert_array_equal(y2, np.from_dlpack(y2))
```

### Step 3: Call assert_array_equal()

```python
assert_array_equal(y1, np.from_dlpack(y1))
```

**Verification:**
```python
assert_array_equal(y3, np.from_dlpack(y3))
```

### Step 4: Assign y2 = value

```python
y2 = x[:, 0]
```

**Verification:**
```python
assert_array_equal(y4, np.from_dlpack(y4))
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(y2, np.from_dlpack(y2))
```

**Verification:**
```python
assert_array_equal(y5, np.from_dlpack(y5))
```

### Step 6: Assign y3 = value

```python
y3 = x[1, :]
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(y3, np.from_dlpack(y3))
```

### Step 8: Assign y4 = value

```python
y4 = x[1]
```

### Step 9: Call assert_array_equal()

```python
assert_array_equal(y4, np.from_dlpack(y4))
```

### Step 10: Assign y5 = np.diagonal.copy(...)

```python
y5 = np.diagonal(x).copy()
```

### Step 11: Call assert_array_equal()

```python
assert_array_equal(y5, np.from_dlpack(y5))
```


## Complete Example

```python
# Workflow
x = np.arange(25).reshape((5, 5))
y1 = x[0]
assert_array_equal(y1, np.from_dlpack(y1))
y2 = x[:, 0]
assert_array_equal(y2, np.from_dlpack(y2))
y3 = x[1, :]
assert_array_equal(y3, np.from_dlpack(y3))
y4 = x[1]
assert_array_equal(y4, np.from_dlpack(y4))
y5 = np.diagonal(x).copy()
assert_array_equal(y5, np.from_dlpack(y5))
```

## Next Steps


---

*Source: test_dlpack.py:94 | Complexity: Advanced | Last updated: 2026-06-02*