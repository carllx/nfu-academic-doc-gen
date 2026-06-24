# How To: Spacing Nextafter

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test np.spacing and np.nextafter

## Prerequisites

**Required Modules:**
- `platform`
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: 'Test np.spacing and np.nextafter'

```python
'Test np.spacing and np.nextafter'
```

**Verification:**
```python
assert_equal(np.spacing(a_f16[:-1]), a_f16[1:] - a_f16[:-1])
```

### Step 2: Assign a = np.arange(...)

```python
a = np.arange(31744, dtype=uint16)
```

**Verification:**
```python
assert_equal(np.nextafter(a_f16[:-1], hinf), a_f16[1:])
```

### Step 3: Assign hinf = np.array(...)

```python
hinf = np.array((np.inf,), dtype=float16)
```

**Verification:**
```python
assert_equal(np.nextafter(a_f16[0], -hinf), -a_f16[1])
```

### Step 4: Assign hnan = np.array(...)

```python
hnan = np.array((np.nan,), dtype=float16)
```

**Verification:**
```python
assert_equal(np.nextafter(a_f16[1:], -hinf), a_f16[:-1])
```

### Step 5: Assign a_f16 = a.view(...)

```python
a_f16 = a.view(dtype=float16)
```

**Verification:**
```python
assert_equal(np.nextafter(hinf, a_f16), a_f16[-1])
```

### Step 6: Call assert_equal()

```python
assert_equal(np.spacing(a_f16[:-1]), a_f16[1:] - a_f16[:-1])
```

**Verification:**
```python
assert_equal(np.nextafter(-hinf, a_f16), -a_f16[-1])
```

### Step 7: Call assert_equal()

```python
assert_equal(np.nextafter(a_f16[:-1], hinf), a_f16[1:])
```

**Verification:**
```python
assert_equal(np.nextafter(hinf, hinf), hinf)
```

### Step 8: Call assert_equal()

```python
assert_equal(np.nextafter(a_f16[0], -hinf), -a_f16[1])
```

**Verification:**
```python
assert_equal(np.nextafter(hinf, -hinf), a_f16[-1])
```

### Step 9: Call assert_equal()

```python
assert_equal(np.nextafter(a_f16[1:], -hinf), a_f16[:-1])
```

**Verification:**
```python
assert_equal(np.nextafter(-hinf, hinf), -a_f16[-1])
```

### Step 10: Call assert_equal()

```python
assert_equal(np.nextafter(hinf, a_f16), a_f16[-1])
```

**Verification:**
```python
assert_equal(np.nextafter(-hinf, -hinf), -hinf)
```

### Step 11: Call assert_equal()

```python
assert_equal(np.nextafter(-hinf, a_f16), -a_f16[-1])
```

**Verification:**
```python
assert_equal(np.nextafter(a_f16, hnan), hnan[0])
```

### Step 12: Call assert_equal()

```python
assert_equal(np.nextafter(hinf, hinf), hinf)
```

**Verification:**
```python
assert_equal(np.nextafter(hnan, a_f16), hnan[0])
```

### Step 13: Call assert_equal()

```python
assert_equal(np.nextafter(hinf, -hinf), a_f16[-1])
```

**Verification:**
```python
assert_equal(np.nextafter(hnan, hnan), hnan)
```

### Step 14: Call assert_equal()

```python
assert_equal(np.nextafter(-hinf, hinf), -a_f16[-1])
```

**Verification:**
```python
assert_equal(np.nextafter(hinf, hnan), hnan)
```

### Step 15: Call assert_equal()

```python
assert_equal(np.nextafter(-hinf, -hinf), -hinf)
```

**Verification:**
```python
assert_equal(np.nextafter(hnan, hinf), hnan)
```

### Step 16: Call assert_equal()

```python
assert_equal(np.nextafter(a_f16, hnan), hnan[0])
```

**Verification:**
```python
assert_equal(np.spacing(a_f16[0]), np.spacing(a_f16[1]))
```

### Step 17: Call assert_equal()

```python
assert_equal(np.nextafter(hnan, a_f16), hnan[0])
```

**Verification:**
```python
assert_equal(np.spacing(a_f16[1:]), a_f16[:-1] - a_f16[1:])
```

### Step 18: Call assert_equal()

```python
assert_equal(np.nextafter(hnan, hnan), hnan)
```

**Verification:**
```python
assert_equal(np.nextafter(a_f16[0], hinf), -a_f16[1])
```

### Step 19: Call assert_equal()

```python
assert_equal(np.nextafter(hinf, hnan), hnan)
```

**Verification:**
```python
assert_equal(np.nextafter(a_f16[1:], hinf), a_f16[:-1])
```

### Step 20: Call assert_equal()

```python
assert_equal(np.nextafter(hnan, hinf), hnan)
```

**Verification:**
```python
assert_equal(np.nextafter(a_f16[:-1], -hinf), a_f16[1:])
```

### Step 21: Call assert_equal()

```python
assert_equal(np.spacing(a_f16[0]), np.spacing(a_f16[1]))
```

**Verification:**
```python
assert_equal(np.nextafter(hinf, a_f16), -a_f16[-1])
```

### Step 22: Call assert_equal()

```python
assert_equal(np.spacing(a_f16[1:]), a_f16[:-1] - a_f16[1:])
```

**Verification:**
```python
assert_equal(np.nextafter(-hinf, a_f16), a_f16[-1])
```

### Step 23: Call assert_equal()

```python
assert_equal(np.nextafter(a_f16[0], hinf), -a_f16[1])
```

**Verification:**
```python
assert_equal(np.nextafter(a_f16, hnan), hnan[0])
```

### Step 24: Call assert_equal()

```python
assert_equal(np.nextafter(a_f16[1:], hinf), a_f16[:-1])
```

**Verification:**
```python
assert_equal(np.nextafter(hnan, a_f16), hnan[0])
```

### Step 25: Call assert_equal()

```python
assert_equal(np.nextafter(a_f16[:-1], -hinf), a_f16[1:])
```

### Step 26: Call assert_equal()

```python
assert_equal(np.nextafter(hinf, a_f16), -a_f16[-1])
```

### Step 27: Call assert_equal()

```python
assert_equal(np.nextafter(-hinf, a_f16), a_f16[-1])
```

### Step 28: Call assert_equal()

```python
assert_equal(np.nextafter(a_f16, hnan), hnan[0])
```

### Step 29: Call assert_equal()

```python
assert_equal(np.nextafter(hnan, a_f16), hnan[0])
```


## Complete Example

```python
# Workflow
'Test np.spacing and np.nextafter'
a = np.arange(31744, dtype=uint16)
hinf = np.array((np.inf,), dtype=float16)
hnan = np.array((np.nan,), dtype=float16)
a_f16 = a.view(dtype=float16)
assert_equal(np.spacing(a_f16[:-1]), a_f16[1:] - a_f16[:-1])
assert_equal(np.nextafter(a_f16[:-1], hinf), a_f16[1:])
assert_equal(np.nextafter(a_f16[0], -hinf), -a_f16[1])
assert_equal(np.nextafter(a_f16[1:], -hinf), a_f16[:-1])
assert_equal(np.nextafter(hinf, a_f16), a_f16[-1])
assert_equal(np.nextafter(-hinf, a_f16), -a_f16[-1])
assert_equal(np.nextafter(hinf, hinf), hinf)
assert_equal(np.nextafter(hinf, -hinf), a_f16[-1])
assert_equal(np.nextafter(-hinf, hinf), -a_f16[-1])
assert_equal(np.nextafter(-hinf, -hinf), -hinf)
assert_equal(np.nextafter(a_f16, hnan), hnan[0])
assert_equal(np.nextafter(hnan, a_f16), hnan[0])
assert_equal(np.nextafter(hnan, hnan), hnan)
assert_equal(np.nextafter(hinf, hnan), hnan)
assert_equal(np.nextafter(hnan, hinf), hnan)
a |= 32768
assert_equal(np.spacing(a_f16[0]), np.spacing(a_f16[1]))
assert_equal(np.spacing(a_f16[1:]), a_f16[:-1] - a_f16[1:])
assert_equal(np.nextafter(a_f16[0], hinf), -a_f16[1])
assert_equal(np.nextafter(a_f16[1:], hinf), a_f16[:-1])
assert_equal(np.nextafter(a_f16[:-1], -hinf), a_f16[1:])
assert_equal(np.nextafter(hinf, a_f16), -a_f16[-1])
assert_equal(np.nextafter(-hinf, a_f16), a_f16[-1])
assert_equal(np.nextafter(a_f16, hnan), hnan[0])
assert_equal(np.nextafter(hnan, a_f16), hnan[0])
```

## Next Steps


---

*Source: test_half.py:379 | Complexity: Advanced | Last updated: 2026-06-02*