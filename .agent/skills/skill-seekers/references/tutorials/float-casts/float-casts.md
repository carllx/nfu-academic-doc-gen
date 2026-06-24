# How To: Float Casts

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test float casts

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `copy`
- `itertools`
- `os`
- `pickle`
- `string`
- `sys`
- `tempfile`
- `pytest`
- `numpy`
- `numpy._core.tests._natype`
- `numpy.dtypes`
- `numpy.testing`
- `numpy.lib._stride_tricks_impl`

**Setup Required:**
```python
# Fixtures: typename
```

## Step-by-Step Guide

### Step 1: Assign inp = value

```python
inp = [1.1, 2.8, -3.2, 27000.0]
```

**Verification:**
```python
assert_array_equal(ainp, ainp.astype('T').astype(typename))
```

### Step 2: Assign ainp = np.array(...)

```python
ainp = np.array(inp, dtype=typename)
```

**Verification:**
```python
assert_array_equal(np.array(inp, dtype=typename), res)
```

### Step 3: Call assert_array_equal()

```python
assert_array_equal(ainp, ainp.astype('T').astype(typename))
```

**Verification:**
```python
assert sres[0] == '0.1'
```

### Step 4: Assign inp = value

```python
inp = [0.1]
```

**Verification:**
```python
assert_array_equal(eres, res)
```

### Step 5: Assign sres = np.array.astype(...)

```python
sres = np.array(inp, dtype=typename).astype('T')
```

**Verification:**
```python
assert_array_equal(eres, res)
```

### Step 6: Assign res = sres.astype(...)

```python
res = sres.astype(typename)
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(np.array(inp, dtype=typename), res)
```

**Verification:**
```python
assert sres[0] == '0.1'
```

### Step 8: Assign fi = np.finfo(...)

```python
fi = np.finfo(typename)
```

### Step 9: Assign inp = value

```python
inp = [0.0, fi.smallest_subnormal, -0.0, -fi.smallest_subnormal]
```

### Step 10: Assign eres = value

```python
eres = [0, fi.smallest_subnormal, -0, -fi.smallest_subnormal]
```

### Step 11: Assign res = np.array.astype.astype(...)

```python
res = np.array(inp, dtype=typename).astype('T').astype(typename)
```

### Step 12: Call assert_array_equal()

```python
assert_array_equal(eres, res)
```

### Step 13: Assign inp = value

```python
inp = [1e309, fi.max, -1e309, fi.min]
```

### Step 14: Assign eres = value

```python
eres = [np.inf, fi.max, -np.inf, fi.min]
```

### Step 15: Assign res = np.array.astype.astype(...)

```python
res = np.array(inp, dtype=typename).astype('T').astype(typename)
```

### Step 16: Call assert_array_equal()

```python
assert_array_equal(eres, res)
```


## Complete Example

```python
# Setup
# Fixtures: typename

# Workflow
inp = [1.1, 2.8, -3.2, 27000.0]
ainp = np.array(inp, dtype=typename)
assert_array_equal(ainp, ainp.astype('T').astype(typename))
inp = [0.1]
sres = np.array(inp, dtype=typename).astype('T')
res = sres.astype(typename)
assert_array_equal(np.array(inp, dtype=typename), res)
assert sres[0] == '0.1'
if typename == 'longdouble':
    return
fi = np.finfo(typename)
inp = [0.0, fi.smallest_subnormal, -0.0, -fi.smallest_subnormal]
eres = [0, fi.smallest_subnormal, -0, -fi.smallest_subnormal]
res = np.array(inp, dtype=typename).astype('T').astype(typename)
assert_array_equal(eres, res)
inp = [1e309, fi.max, -1e309, fi.min]
eres = [np.inf, fi.max, -np.inf, fi.min]
res = np.array(inp, dtype=typename).astype('T').astype(typename)
assert_array_equal(eres, res)
```

## Next Steps


---

*Source: test_stringdtype.py:755 | Complexity: Advanced | Last updated: 2026-06-02*