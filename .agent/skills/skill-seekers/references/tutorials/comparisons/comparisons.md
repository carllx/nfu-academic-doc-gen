# How To: Comparisons

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test comparisons

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
# Fixtures: string_list, dtype, op, o_dtype
```

## Step-by-Step Guide

### Step 1: Assign sarr = np.array(...)

```python
sarr = np.array(string_list, dtype=dtype)
```

**Verification:**
```python
assert_array_equal(res, ores)
```

### Step 2: Assign oarr = np.array(...)

```python
oarr = np.array(string_list, dtype=o_dtype)
```

**Verification:**
```python
assert_array_equal(res, orres)
```

### Step 3: Assign res = op(...)

```python
res = op(sarr, sarr)
```

**Verification:**
```python
assert_array_equal(res, olres)
```

### Step 4: Assign ores = op(...)

```python
ores = op(oarr, oarr)
```

**Verification:**
```python
assert_array_equal(res, ores)
```

### Step 5: Assign orres = op(...)

```python
orres = op(sarr, oarr)
```

**Verification:**
```python
assert_array_equal(res, olres)
```

### Step 6: Assign olres = op(...)

```python
olres = op(oarr, sarr)
```

**Verification:**
```python
assert_array_equal(res, orres)
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(res, ores)
```

**Verification:**
```python
assert_array_equal(res, ores)
```

### Step 8: Call assert_array_equal()

```python
assert_array_equal(res, orres)
```

**Verification:**
```python
assert_array_equal(res, olres)
```

### Step 9: Call assert_array_equal()

```python
assert_array_equal(res, olres)
```

**Verification:**
```python
assert_array_equal(res, orres)
```

### Step 10: Assign sarr2 = np.array(...)

```python
sarr2 = np.array([s + '2' for s in string_list], dtype=dtype)
```

### Step 11: Assign oarr2 = np.array(...)

```python
oarr2 = np.array([s + '2' for s in string_list], dtype=o_dtype)
```

### Step 12: Assign res = op(...)

```python
res = op(sarr, sarr2)
```

### Step 13: Assign ores = op(...)

```python
ores = op(oarr, oarr2)
```

### Step 14: Assign olres = op(...)

```python
olres = op(oarr, sarr2)
```

### Step 15: Assign orres = op(...)

```python
orres = op(sarr, oarr2)
```

### Step 16: Call assert_array_equal()

```python
assert_array_equal(res, ores)
```

### Step 17: Call assert_array_equal()

```python
assert_array_equal(res, olres)
```

### Step 18: Call assert_array_equal()

```python
assert_array_equal(res, orres)
```

### Step 19: Assign res = op(...)

```python
res = op(sarr2, sarr)
```

### Step 20: Assign ores = op(...)

```python
ores = op(oarr2, oarr)
```

### Step 21: Assign olres = op(...)

```python
olres = op(oarr2, sarr)
```

### Step 22: Assign orres = op(...)

```python
orres = op(sarr2, oarr)
```

### Step 23: Call assert_array_equal()

```python
assert_array_equal(res, ores)
```

### Step 24: Call assert_array_equal()

```python
assert_array_equal(res, olres)
```

### Step 25: Call assert_array_equal()

```python
assert_array_equal(res, orres)
```


## Complete Example

```python
# Setup
# Fixtures: string_list, dtype, op, o_dtype

# Workflow
sarr = np.array(string_list, dtype=dtype)
oarr = np.array(string_list, dtype=o_dtype)
res = op(sarr, sarr)
ores = op(oarr, oarr)
orres = op(sarr, oarr)
olres = op(oarr, sarr)
assert_array_equal(res, ores)
assert_array_equal(res, orres)
assert_array_equal(res, olres)
sarr2 = np.array([s + '2' for s in string_list], dtype=dtype)
oarr2 = np.array([s + '2' for s in string_list], dtype=o_dtype)
res = op(sarr, sarr2)
ores = op(oarr, oarr2)
olres = op(oarr, sarr2)
orres = op(sarr, oarr2)
assert_array_equal(res, ores)
assert_array_equal(res, olres)
assert_array_equal(res, orres)
res = op(sarr2, sarr)
ores = op(oarr2, oarr)
olres = op(oarr2, sarr)
orres = op(sarr2, oarr)
assert_array_equal(res, ores)
assert_array_equal(res, olres)
assert_array_equal(res, orres)
```

## Next Steps


---

*Source: test_stringdtype.py:342 | Complexity: Advanced | Last updated: 2026-06-02*