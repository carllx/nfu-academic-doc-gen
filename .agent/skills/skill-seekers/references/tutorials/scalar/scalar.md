# How To: Scalar

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test scalar

## Prerequisites

**Required Modules:**
- `numpy`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign x = value

```python
x = np.inf
```

**Verification:**
```python
assert_equal(actual, expected)
```

### Step 2: Assign actual = np.isposinf(...)

```python
actual = np.isposinf(x)
```

**Verification:**
```python
assert_equal(type(actual), type(expected))
```

### Step 3: Assign expected = value

```python
expected = np.True_
```

**Verification:**
```python
assert_equal(actual, expected)
```

### Step 4: Call assert_equal()

```python
assert_equal(actual, expected)
```

**Verification:**
```python
assert_equal(type(actual), type(expected))
```

### Step 5: Call assert_equal()

```python
assert_equal(type(actual), type(expected))
```

**Verification:**
```python
assert_(actual is out)
```

### Step 6: Assign x = value

```python
x = -3.4
```

### Step 7: Assign actual = np.fix(...)

```python
actual = np.fix(x)
```

### Step 8: Assign expected = np.float64(...)

```python
expected = np.float64(-3.0)
```

### Step 9: Call assert_equal()

```python
assert_equal(actual, expected)
```

### Step 10: Call assert_equal()

```python
assert_equal(type(actual), type(expected))
```

### Step 11: Assign out = np.array(...)

```python
out = np.array(0.0)
```

### Step 12: Assign actual = np.fix(...)

```python
actual = np.fix(x, out=out)
```

### Step 13: Call assert_()

```python
assert_(actual is out)
```


## Complete Example

```python
# Workflow
x = np.inf
actual = np.isposinf(x)
expected = np.True_
assert_equal(actual, expected)
assert_equal(type(actual), type(expected))
x = -3.4
actual = np.fix(x)
expected = np.float64(-3.0)
assert_equal(actual, expected)
assert_equal(type(actual), type(expected))
out = np.array(0.0)
actual = np.fix(x, out=out)
assert_(actual is out)
```

## Next Steps


---

*Source: test_ufunclike.py:82 | Complexity: Advanced | Last updated: 2026-06-02*