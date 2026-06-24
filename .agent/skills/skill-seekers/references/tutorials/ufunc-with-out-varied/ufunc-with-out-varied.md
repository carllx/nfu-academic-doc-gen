# How To: Ufunc With Out Varied

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: Test that masked arrays are immune to gh-10459 

## Prerequisites

**Required Modules:**
- `copy`
- `inspect`
- `itertools`
- `operator`
- `pickle`
- `sys`
- `textwrap`
- `warnings`
- `functools`
- `pytest`
- `numpy`
- `numpy._core.fromnumeric`
- `numpy._core.umath`
- `numpy.ma.core`
- `numpy`
- `numpy._utils`
- `numpy.exceptions`
- `numpy.ma.core`
- `numpy.ma.testutils`
- `numpy.testing`
- `numpy.testing._private.utils`
- `datetime`
- `copy`
- `io`
- `copy`
- `copy`


## Step-by-Step Guide

### Step 1: ' Test that masked arrays are immune to gh-10459 '

```python
' Test that masked arrays are immune to gh-10459 '
```

**Verification:**
```python
assert_equal(res_kw.mask, expected.mask)
```

### Step 2: Assign a = array(...)

```python
a = array([1, 2, 3], mask=[1, 0, 0])
```

**Verification:**
```python
assert_equal(res_kw.data, expected.data)
```

### Step 3: Assign b = array(...)

```python
b = array([10, 20, 30], mask=[1, 0, 0])
```

**Verification:**
```python
assert_equal(res_tup.mask, expected.mask)
```

### Step 4: Assign out = array(...)

```python
out = array([0, 0, 0], mask=[0, 0, 1])
```

**Verification:**
```python
assert_equal(res_tup.data, expected.data)
```

### Step 5: Assign expected = array(...)

```python
expected = array([11, 22, 33], mask=[1, 0, 0])
```

**Verification:**
```python
assert_equal(res_pos.mask, expected.mask)
```

### Step 6: Assign out_pos = out.copy(...)

```python
out_pos = out.copy()
```

**Verification:**
```python
assert_equal(res_pos.data, expected.data)
```

### Step 7: Assign res_pos = np.add(...)

```python
res_pos = np.add(a, b, out_pos)
```

### Step 8: Assign out_kw = out.copy(...)

```python
out_kw = out.copy()
```

### Step 9: Assign res_kw = np.add(...)

```python
res_kw = np.add(a, b, out=out_kw)
```

### Step 10: Assign out_tup = out.copy(...)

```python
out_tup = out.copy()
```

### Step 11: Assign res_tup = np.add(...)

```python
res_tup = np.add(a, b, out=(out_tup,))
```

### Step 12: Call assert_equal()

```python
assert_equal(res_kw.mask, expected.mask)
```

### Step 13: Call assert_equal()

```python
assert_equal(res_kw.data, expected.data)
```

### Step 14: Call assert_equal()

```python
assert_equal(res_tup.mask, expected.mask)
```

### Step 15: Call assert_equal()

```python
assert_equal(res_tup.data, expected.data)
```

### Step 16: Call assert_equal()

```python
assert_equal(res_pos.mask, expected.mask)
```

### Step 17: Call assert_equal()

```python
assert_equal(res_pos.data, expected.data)
```


## Complete Example

```python
# Workflow
' Test that masked arrays are immune to gh-10459 '
a = array([1, 2, 3], mask=[1, 0, 0])
b = array([10, 20, 30], mask=[1, 0, 0])
out = array([0, 0, 0], mask=[0, 0, 1])
expected = array([11, 22, 33], mask=[1, 0, 0])
out_pos = out.copy()
res_pos = np.add(a, b, out_pos)
out_kw = out.copy()
res_kw = np.add(a, b, out=out_kw)
out_tup = out.copy()
res_tup = np.add(a, b, out=(out_tup,))
assert_equal(res_kw.mask, expected.mask)
assert_equal(res_kw.data, expected.data)
assert_equal(res_tup.mask, expected.mask)
assert_equal(res_tup.data, expected.data)
assert_equal(res_pos.mask, expected.mask)
assert_equal(res_pos.data, expected.data)
```

## Next Steps


---

*Source: test_core.py:5784 | Complexity: Advanced | Last updated: 2026-06-02*