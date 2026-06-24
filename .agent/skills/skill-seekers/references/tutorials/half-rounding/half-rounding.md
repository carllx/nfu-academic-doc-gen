# How To: Half Rounding

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: Checks that rounding when converting to half is correct

## Prerequisites

**Required Modules:**
- `platform`
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: 'Checks that rounding when converting to half is correct'

```python
'Checks that rounding when converting to half is correct'
```

**Verification:**
```python
assert_equal(b, rounded)
```

### Step 2: Assign a = np.array(...)

```python
a = np.array([2.0 ** (-25) + 2.0 ** (-35), 2.0 ** (-25), 2.0 ** (-26), 1.0 + 2.0 ** (-11) + 2.0 ** (-16), 1.0 + 2.0 ** (-11), 1.0 + 2.0 ** (-12), 65519, 65520], dtype=float64)
```

**Verification:**
```python
assert_equal(b, rounded)
```

### Step 3: Assign rounded = value

```python
rounded = [2.0 ** (-24), 0.0, 0.0, 1.0 + 2.0 ** (-10), 1.0, 1.0, 65504, np.inf]
```

### Step 4: Call assert_equal()

```python
assert_equal(b, rounded)
```

### Step 5: Assign a = np.array(...)

```python
a = np.array(a, dtype=float32)
```

### Step 6: Call assert_equal()

```python
assert_equal(b, rounded)
```

### Step 7: Assign b = np.array(...)

```python
b = np.array(a, dtype=float16)
```

### Step 8: Assign b = np.array(...)

```python
b = np.array(a, dtype=float16)
```


## Complete Example

```python
# Workflow
'Checks that rounding when converting to half is correct'
a = np.array([2.0 ** (-25) + 2.0 ** (-35), 2.0 ** (-25), 2.0 ** (-26), 1.0 + 2.0 ** (-11) + 2.0 ** (-16), 1.0 + 2.0 ** (-11), 1.0 + 2.0 ** (-12), 65519, 65520], dtype=float64)
rounded = [2.0 ** (-24), 0.0, 0.0, 1.0 + 2.0 ** (-10), 1.0, 1.0, 65504, np.inf]
with np.errstate(over='ignore'):
    b = np.array(a, dtype=float16)
assert_equal(b, rounded)
a = np.array(a, dtype=float32)
with np.errstate(over='ignore'):
    b = np.array(a, dtype=float16)
assert_equal(b, rounded)
```

## Next Steps


---

*Source: test_half.py:247 | Complexity: Advanced | Last updated: 2026-06-02*