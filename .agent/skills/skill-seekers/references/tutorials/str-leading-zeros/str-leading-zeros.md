# How To: Str Leading Zeros

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test str leading zeros

## Prerequisites

**Required Modules:**
- `pytest`
- `numpy`
- `numpy.polynomial.polynomial`
- `numpy.testing`
- `decimal`


## Step-by-Step Guide

### Step 1: Assign p = np.poly1d(...)

```python
p = np.poly1d([4, 3, 2, 1])
```

**Verification:**
```python
assert_equal(str(p), '   2\n3 x + 2 x + 1')
```

### Step 2: Assign unknown = 0

```python
p[3] = 0
```

**Verification:**
```python
assert_equal(str(p), ' \n0')
```

### Step 3: Call assert_equal()

```python
assert_equal(str(p), '   2\n3 x + 2 x + 1')
```

### Step 4: Assign p = np.poly1d(...)

```python
p = np.poly1d([1, 2])
```

### Step 5: Assign unknown = 0

```python
p[0] = 0
```

### Step 6: Assign unknown = 0

```python
p[1] = 0
```

### Step 7: Call assert_equal()

```python
assert_equal(str(p), ' \n0')
```


## Complete Example

```python
# Workflow
p = np.poly1d([4, 3, 2, 1])
p[3] = 0
assert_equal(str(p), '   2\n3 x + 2 x + 1')
p = np.poly1d([1, 2])
p[0] = 0
p[1] = 0
assert_equal(str(p), ' \n0')
```

## Next Steps


---

*Source: test_polynomial.py:146 | Complexity: Intermediate | Last updated: 2026-06-02*