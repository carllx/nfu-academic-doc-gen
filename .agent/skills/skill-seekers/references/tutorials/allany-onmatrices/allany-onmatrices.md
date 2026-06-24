# How To: Allany Onmatrices

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test allany onmatrices

## Prerequisites

**Required Modules:**
- `pickle`
- `numpy`
- `numpy.ma.core`
- `numpy.ma.extras`
- `numpy.ma.testutils`


## Step-by-Step Guide

### Step 1: Assign x = np.array(...)

```python
x = np.array([[0.13, 0.26, 0.9], [0.28, 0.33, 0.63], [0.31, 0.87, 0.7]])
```

**Verification:**
```python
assert_(not mXbig.all())
```

### Step 2: Assign X = np.matrix(...)

```python
X = np.matrix(x)
```

**Verification:**
```python
assert_(mXbig.any())
```

### Step 3: Assign m = np.array(...)

```python
m = np.array([[True, False, False], [False, False, False], [True, True, False]], dtype=np.bool)
```

**Verification:**
```python
assert_equal(mXbig.all(0), np.matrix([False, False, True]))
```

### Step 4: Assign mX = masked_array(...)

```python
mX = masked_array(X, mask=m)
```

**Verification:**
```python
assert_equal(mXbig.all(1), np.matrix([False, False, True]).T)
```

### Step 5: Assign mXbig = value

```python
mXbig = mX > 0.5
```

**Verification:**
```python
assert_equal(mXbig.any(0), np.matrix([False, False, True]))
```

### Step 6: Assign mXsmall = value

```python
mXsmall = mX < 0.5
```

**Verification:**
```python
assert_equal(mXbig.any(1), np.matrix([True, True, True]).T)
```

### Step 7: Call assert_()

```python
assert_(not mXbig.all())
```

**Verification:**
```python
assert_(not mXsmall.all())
```

### Step 8: Call assert_()

```python
assert_(mXbig.any())
```

**Verification:**
```python
assert_(mXsmall.any())
```

### Step 9: Call assert_equal()

```python
assert_equal(mXbig.all(0), np.matrix([False, False, True]))
```

**Verification:**
```python
assert_equal(mXsmall.all(0), np.matrix([True, True, False]))
```

### Step 10: Call assert_equal()

```python
assert_equal(mXbig.all(1), np.matrix([False, False, True]).T)
```

**Verification:**
```python
assert_equal(mXsmall.all(1), np.matrix([False, False, False]).T)
```

### Step 11: Call assert_equal()

```python
assert_equal(mXbig.any(0), np.matrix([False, False, True]))
```

**Verification:**
```python
assert_equal(mXsmall.any(0), np.matrix([True, True, False]))
```

### Step 12: Call assert_equal()

```python
assert_equal(mXbig.any(1), np.matrix([True, True, True]).T)
```

**Verification:**
```python
assert_equal(mXsmall.any(1), np.matrix([True, True, False]).T)
```

### Step 13: Call assert_()

```python
assert_(not mXsmall.all())
```

### Step 14: Call assert_()

```python
assert_(mXsmall.any())
```

### Step 15: Call assert_equal()

```python
assert_equal(mXsmall.all(0), np.matrix([True, True, False]))
```

### Step 16: Call assert_equal()

```python
assert_equal(mXsmall.all(1), np.matrix([False, False, False]).T)
```

### Step 17: Call assert_equal()

```python
assert_equal(mXsmall.any(0), np.matrix([True, True, False]))
```

### Step 18: Call assert_equal()

```python
assert_equal(mXsmall.any(1), np.matrix([True, True, False]).T)
```


## Complete Example

```python
# Workflow
x = np.array([[0.13, 0.26, 0.9], [0.28, 0.33, 0.63], [0.31, 0.87, 0.7]])
X = np.matrix(x)
m = np.array([[True, False, False], [False, False, False], [True, True, False]], dtype=np.bool)
mX = masked_array(X, mask=m)
mXbig = mX > 0.5
mXsmall = mX < 0.5
assert_(not mXbig.all())
assert_(mXbig.any())
assert_equal(mXbig.all(0), np.matrix([False, False, True]))
assert_equal(mXbig.all(1), np.matrix([False, False, True]).T)
assert_equal(mXbig.any(0), np.matrix([False, False, True]))
assert_equal(mXbig.any(1), np.matrix([True, True, True]).T)
assert_(not mXsmall.all())
assert_(mXsmall.any())
assert_equal(mXsmall.all(0), np.matrix([True, True, False]))
assert_equal(mXsmall.all(1), np.matrix([False, False, False]).T)
assert_equal(mXsmall.any(0), np.matrix([True, True, False]))
assert_equal(mXsmall.any(1), np.matrix([True, True, False]).T)
```

## Next Steps


---

*Source: test_masked_matrix.py:129 | Complexity: Advanced | Last updated: 2026-06-02*