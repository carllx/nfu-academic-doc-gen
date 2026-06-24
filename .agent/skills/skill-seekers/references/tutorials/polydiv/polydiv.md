# How To: Polydiv

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test polydiv

## Prerequisites

**Required Modules:**
- `pickle`
- `copy`
- `fractions`
- `functools`
- `pytest`
- `numpy`
- `numpy.polynomial.polynomial`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Call assert_raises()

```python
assert_raises(ZeroDivisionError, poly.polydiv, [1], [0])
```

**Verification:**
```python
assert_raises(ZeroDivisionError, poly.polydiv, [1], [0])
```

### Step 2: Assign unknown = poly.polydiv(...)

```python
quo, rem = poly.polydiv([2], [2])
```

**Verification:**
```python
assert_equal((quo, rem), (1, 0))
```

### Step 3: Call assert_equal()

```python
assert_equal((quo, rem), (1, 0))
```

**Verification:**
```python
assert_equal((quo, rem), ((1, 1), 0))
```

### Step 4: Assign unknown = poly.polydiv(...)

```python
quo, rem = poly.polydiv([2, 2], [2])
```

**Verification:**
```python
assert_equal(res, tgt, err_msg=msg)
```

### Step 5: Call assert_equal()

```python
assert_equal((quo, rem), ((1, 1), 0))
```

### Step 6: Assign msg = value

```python
msg = f'At i={i}, j={j}'
```

### Step 7: Assign ci = value

```python
ci = [0] * i + [1, 2]
```

### Step 8: Assign cj = value

```python
cj = [0] * j + [1, 2]
```

### Step 9: Assign tgt = poly.polyadd(...)

```python
tgt = poly.polyadd(ci, cj)
```

### Step 10: Assign unknown = poly.polydiv(...)

```python
quo, rem = poly.polydiv(tgt, ci)
```

### Step 11: Assign res = poly.polyadd(...)

```python
res = poly.polyadd(poly.polymul(quo, ci), rem)
```

### Step 12: Call assert_equal()

```python
assert_equal(res, tgt, err_msg=msg)
```


## Complete Example

```python
# Workflow
assert_raises(ZeroDivisionError, poly.polydiv, [1], [0])
quo, rem = poly.polydiv([2], [2])
assert_equal((quo, rem), (1, 0))
quo, rem = poly.polydiv([2, 2], [2])
assert_equal((quo, rem), ((1, 1), 0))
for i in range(5):
    for j in range(5):
        msg = f'At i={i}, j={j}'
        ci = [0] * i + [1, 2]
        cj = [0] * j + [1, 2]
        tgt = poly.polyadd(ci, cj)
        quo, rem = poly.polydiv(tgt, ci)
        res = poly.polyadd(poly.polymul(quo, ci), rem)
        assert_equal(res, tgt, err_msg=msg)
```

## Next Steps


---

*Source: test_polynomial.py:104 | Complexity: Advanced | Last updated: 2026-06-02*