# How To: Float Modulus Exact

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test float modulus exact

## Prerequisites

**Required Modules:**
- `contextlib`
- `itertools`
- `operator`
- `platform`
- `sys`
- `warnings`
- `pytest`
- `hypothesis`
- `hypothesis.extra`
- `hypothesis.strategies`
- `numpy`
- `numpy._core._rational_tests`
- `numpy._utils`
- `numpy.exceptions`
- `numpy.testing`


## Step-by-Step Guide

### Step 1: Assign nlst = list(...)

```python
nlst = list(range(-127, 0))
```

**Verification:**
```python
assert_equal(div, tgtdiv, err_msg=msg)
```

### Step 2: Assign plst = list(...)

```python
plst = list(range(1, 128))
```

**Verification:**
```python
assert_equal(rem, tgtrem, err_msg=msg)
```

### Step 3: Assign dividend = value

```python
dividend = nlst + [0] + plst
```

### Step 4: Assign divisor = value

```python
divisor = nlst + plst
```

### Step 5: Assign arg = list(...)

```python
arg = list(itertools.product(dividend, divisor))
```

### Step 6: Assign tgt = value

```python
tgt = [divmod(*t) for t in arg]
```

### Step 7: Assign unknown = value

```python
a, b = np.array(arg, dtype=int).T
```

### Step 8: Assign unknown = value

```python
tgtdiv, tgtrem = np.array(tgt, dtype=float).T
```

### Step 9: Assign tgtdiv = np.where(...)

```python
tgtdiv = np.where((tgtdiv == 0.0) & ((b < 0) ^ (a < 0)), -0.0, tgtdiv)
```

### Step 10: Assign tgtrem = np.where(...)

```python
tgtrem = np.where((tgtrem == 0.0) & (b < 0), -0.0, tgtrem)
```

### Step 11: Assign msg = value

```python
msg = f'op: {op.__name__}, dtype: {dt}'
```

### Step 12: Assign fa = a.astype(...)

```python
fa = a.astype(dt)
```

### Step 13: Assign fb = b.astype(...)

```python
fb = b.astype(dt)
```

### Step 14: Assign unknown = zip(...)

```python
div, rem = zip(*[op(a_, b_) for a_, b_ in zip(fa, fb)])
```

### Step 15: Call assert_equal()

```python
assert_equal(div, tgtdiv, err_msg=msg)
```

### Step 16: Call assert_equal()

```python
assert_equal(rem, tgtrem, err_msg=msg)
```


## Complete Example

```python
# Workflow
nlst = list(range(-127, 0))
plst = list(range(1, 128))
dividend = nlst + [0] + plst
divisor = nlst + plst
arg = list(itertools.product(dividend, divisor))
tgt = [divmod(*t) for t in arg]
a, b = np.array(arg, dtype=int).T
tgtdiv, tgtrem = np.array(tgt, dtype=float).T
tgtdiv = np.where((tgtdiv == 0.0) & ((b < 0) ^ (a < 0)), -0.0, tgtdiv)
tgtrem = np.where((tgtrem == 0.0) & (b < 0), -0.0, tgtrem)
for op in [floordiv_and_mod, divmod]:
    for dt in np.typecodes['Float']:
        msg = f'op: {op.__name__}, dtype: {dt}'
        fa = a.astype(dt)
        fb = b.astype(dt)
        div, rem = zip(*[op(a_, b_) for a_, b_ in zip(fa, fb)])
        assert_equal(div, tgtdiv, err_msg=msg)
        assert_equal(rem, tgtrem, err_msg=msg)
```

## Next Steps


---

*Source: test_scalarmath.py:315 | Complexity: Advanced | Last updated: 2026-06-02*