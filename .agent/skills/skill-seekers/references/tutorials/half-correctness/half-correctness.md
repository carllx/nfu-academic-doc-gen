# How To: Half Correctness

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Take every finite float16, and check the casting functions with
a manual conversion.

## Prerequisites

**Required Modules:**
- `platform`
- `pytest`
- `numpy`
- `numpy`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: 'Take every finite float16, and check the casting functions with\n           a manual conversion.'

```python
'Take every finite float16, and check the casting functions with\n           a manual conversion.'
```

**Verification:**
```python
assert_equal(finite_f32, a_manual, 'First non-equal is half value 0x%x -> %g != %g' % (a_bits[bad_index], finite_f32[bad_index], a_manual[bad_index]))
```

### Step 2: Assign unknown = self._create_arrays_finite(...)

```python
finite_f16, finite_f32, finite_f64 = self._create_arrays_finite()
```

**Verification:**
```python
assert_equal(finite_f64, a_manual, 'First non-equal is half value 0x%x -> %g != %g' % (a_bits[bad_index], finite_f64[bad_index], a_manual[bad_index]))
```

### Step 3: Assign a_bits = finite_f16.view(...)

```python
a_bits = finite_f16.view(dtype=uint16)
```

### Step 4: Assign a_sgn = value

```python
a_sgn = (-1.0) ** ((a_bits & 32768) >> 15)
```

### Step 5: Assign a_exp = value

```python
a_exp = np.array((a_bits & 31744) >> 10, dtype=np.int32) - 15
```

### Step 6: Assign a_man = value

```python
a_man = (a_bits & 1023) * 2.0 ** (-10)
```

### Step 7: Assign unknown = value

```python
a_exp[a_exp == -15] = -14
```

### Step 8: Assign a_manual = value

```python
a_manual = a_sgn * a_man * 2.0 ** a_exp
```

### Step 9: Assign a32_fail = value

```python
a32_fail = np.nonzero(finite_f32 != a_manual)[0]
```

### Step 10: Assign a64_fail = value

```python
a64_fail = np.nonzero(finite_f64 != a_manual)[0]
```

### Step 11: Assign bad_index = value

```python
bad_index = a32_fail[0]
```

### Step 12: Call assert_equal()

```python
assert_equal(finite_f32, a_manual, 'First non-equal is half value 0x%x -> %g != %g' % (a_bits[bad_index], finite_f32[bad_index], a_manual[bad_index]))
```

### Step 13: Assign bad_index = value

```python
bad_index = a64_fail[0]
```

### Step 14: Call assert_equal()

```python
assert_equal(finite_f64, a_manual, 'First non-equal is half value 0x%x -> %g != %g' % (a_bits[bad_index], finite_f64[bad_index], a_manual[bad_index]))
```


## Complete Example

```python
# Workflow
'Take every finite float16, and check the casting functions with\n           a manual conversion.'
finite_f16, finite_f32, finite_f64 = self._create_arrays_finite()
a_bits = finite_f16.view(dtype=uint16)
a_sgn = (-1.0) ** ((a_bits & 32768) >> 15)
a_exp = np.array((a_bits & 31744) >> 10, dtype=np.int32) - 15
a_man = (a_bits & 1023) * 2.0 ** (-10)
a_man[a_exp != -15] += 1
a_exp[a_exp == -15] = -14
a_manual = a_sgn * a_man * 2.0 ** a_exp
a32_fail = np.nonzero(finite_f32 != a_manual)[0]
if len(a32_fail) != 0:
    bad_index = a32_fail[0]
    assert_equal(finite_f32, a_manual, 'First non-equal is half value 0x%x -> %g != %g' % (a_bits[bad_index], finite_f32[bad_index], a_manual[bad_index]))
a64_fail = np.nonzero(finite_f64 != a_manual)[0]
if len(a64_fail) != 0:
    bad_index = a64_fail[0]
    assert_equal(finite_f64, a_manual, 'First non-equal is half value 0x%x -> %g != %g' % (a_bits[bad_index], finite_f64[bad_index], a_manual[bad_index]))
```

## Next Steps


---

*Source: test_half.py:278 | Complexity: Advanced | Last updated: 2026-06-02*