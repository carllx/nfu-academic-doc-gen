# How To: Special Values

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test special values

## Prerequisites

**Required Modules:**
- `platform`
- `sys`
- `pytest`
- `numpy`
- `numpy._core._multiarray_umath`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign check = check_complex_value

```python
check = check_complex_value
```

### Step 2: Assign f = value

```python
f = np.sqrt
```

### Step 3: Call check()

```python
check(f, ncu.PZERO, 0, 0, 0)
```

### Step 4: Call check()

```python
check(f, ncu.NZERO, 0, 0, 0)
```

### Step 5: Call check()

```python
check(f, 1, np.inf, np.inf, np.inf)
```

### Step 6: Call check()

```python
check(f, -1, np.inf, np.inf, np.inf)
```

### Step 7: Call check()

```python
check(f, ncu.PZERO, np.inf, np.inf, np.inf)
```

### Step 8: Call check()

```python
check(f, ncu.NZERO, np.inf, np.inf, np.inf)
```

### Step 9: Call check()

```python
check(f, np.inf, np.inf, np.inf, np.inf)
```

### Step 10: Call check()

```python
check(f, -np.inf, np.inf, np.inf, np.inf)
```

### Step 11: Call check()

```python
check(f, -np.nan, np.inf, np.inf, np.inf)
```

### Step 12: Call check()

```python
check(f, 1, np.nan, np.nan, np.nan)
```

### Step 13: Call check()

```python
check(f, -1, np.nan, np.nan, np.nan)
```

### Step 14: Call check()

```python
check(f, 0, np.nan, np.nan, np.nan)
```

### Step 15: Call check()

```python
check(f, -np.inf, 1, ncu.PZERO, np.inf)
```

### Step 16: Call check()

```python
check(f, np.inf, 1, np.inf, ncu.PZERO)
```

### Step 17: Call _check_ninf_nan()

```python
_check_ninf_nan(None)
```

### Step 18: Call check()

```python
check(f, np.inf, np.nan, np.inf, np.nan)
```

### Step 19: Call check()

```python
check(f, np.nan, 0, np.nan, np.nan)
```

### Step 20: Call check()

```python
check(f, np.nan, 1, np.nan, np.nan)
```

### Step 21: Call check()

```python
check(f, np.nan, np.nan, np.nan, np.nan)
```

### Step 22: Assign msgform = 'csqrt(-inf, nan) is (%f, %f), expected (nan, +-inf)'

```python
msgform = 'csqrt(-inf, nan) is (%f, %f), expected (nan, +-inf)'
```

### Step 23: Assign z = np.sqrt(...)

```python
z = np.sqrt(np.array(complex(-np.inf, np.nan)))
```


## Complete Example

```python
# Workflow
check = check_complex_value
f = np.sqrt
check(f, ncu.PZERO, 0, 0, 0)
check(f, ncu.NZERO, 0, 0, 0)
check(f, 1, np.inf, np.inf, np.inf)
check(f, -1, np.inf, np.inf, np.inf)
check(f, ncu.PZERO, np.inf, np.inf, np.inf)
check(f, ncu.NZERO, np.inf, np.inf, np.inf)
check(f, np.inf, np.inf, np.inf, np.inf)
check(f, -np.inf, np.inf, np.inf, np.inf)
check(f, -np.nan, np.inf, np.inf, np.inf)
check(f, 1, np.nan, np.nan, np.nan)
check(f, -1, np.nan, np.nan, np.nan)
check(f, 0, np.nan, np.nan, np.nan)
check(f, -np.inf, 1, ncu.PZERO, np.inf)
check(f, np.inf, 1, np.inf, ncu.PZERO)

def _check_ninf_nan(dummy):
    msgform = 'csqrt(-inf, nan) is (%f, %f), expected (nan, +-inf)'
    z = np.sqrt(np.array(complex(-np.inf, np.nan)))
    with np.errstate(invalid='ignore'):
        if not (np.isnan(z.real) and np.isinf(z.imag)):
            raise AssertionError(msgform % (z.real, z.imag))
_check_ninf_nan(None)
check(f, np.inf, np.nan, np.inf, np.nan)
check(f, np.nan, 0, np.nan, np.nan)
check(f, np.nan, 1, np.nan, np.nan)
check(f, np.nan, np.nan, np.nan, np.nan)
```

## Next Steps


---

*Source: test_umath_complex.py:307 | Complexity: Advanced | Last updated: 2026-06-02*