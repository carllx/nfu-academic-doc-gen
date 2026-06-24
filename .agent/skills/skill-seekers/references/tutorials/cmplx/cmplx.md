# How To: Cmplx

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cmplx

## Prerequisites

**Required Modules:**
- `numpy`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign y = value

```python
y = np.random.rand(10) + 1j * np.random.rand(10)
```

**Verification:**
```python
assert_array_equal(y.imag, np.imag(y))
```

### Step 2: Call assert_array_equal()

```python
assert_array_equal(y.imag, np.imag(y))
```

**Verification:**
```python
assert_array_equal(y.imag, out)
```

### Step 3: Assign y = np.array(...)

```python
y = np.array(1 + 1j)
```

**Verification:**
```python
assert_(isinstance(out, np.ndarray))
```

### Step 4: Assign out = np.imag(...)

```python
out = np.imag(y)
```

**Verification:**
```python
assert_equal(1.0, out)
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(y.imag, out)
```

**Verification:**
```python
assert_(not isinstance(out, np.ndarray))
```

### Step 6: Call assert_()

```python
assert_(isinstance(out, np.ndarray))
```

### Step 7: Assign y = value

```python
y = 1 + 1j
```

### Step 8: Assign out = np.imag(...)

```python
out = np.imag(y)
```

### Step 9: Call assert_equal()

```python
assert_equal(1.0, out)
```

### Step 10: Call assert_()

```python
assert_(not isinstance(out, np.ndarray))
```


## Complete Example

```python
# Workflow
y = np.random.rand(10) + 1j * np.random.rand(10)
assert_array_equal(y.imag, np.imag(y))
y = np.array(1 + 1j)
out = np.imag(y)
assert_array_equal(y.imag, out)
assert_(isinstance(out, np.ndarray))
y = 1 + 1j
out = np.imag(y)
assert_equal(1.0, out)
assert_(not isinstance(out, np.ndarray))
```

## Next Steps


---

*Source: test_type_check.py:144 | Complexity: Advanced | Last updated: 2026-06-02*