# How To: Logical Ufuncs Casts To Bool

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test logical ufuncs casts to bool

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `tempfile`
- `pytest`
- `numpy`
- `numpy._core._multiarray_umath`
- `numpy.testing`
- `pickle`

**Setup Required:**
```python
# Fixtures: ufunc
```

## Step-by-Step Guide

### Step 1: Assign a = self._get_array(...)

```python
a = self._get_array(2.0)
```

**Verification:**
```python
assert_array_equal(res, expected)
```

### Step 2: Assign unknown = 0.0

```python
a[0] = 0.0
```

**Verification:**
```python
assert_array_equal(res, expected)
```

### Step 3: Assign float_equiv = a.astype(...)

```python
float_equiv = a.astype(float)
```

### Step 4: Assign expected = ufunc(...)

```python
expected = ufunc(float_equiv, float_equiv)
```

### Step 5: Assign res = ufunc(...)

```python
res = ufunc(a, a)
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(res, expected)
```

### Step 7: Assign expected = ufunc.reduce(...)

```python
expected = ufunc.reduce(float_equiv)
```

### Step 8: Assign res = ufunc.reduce(...)

```python
res = ufunc.reduce(a)
```

### Step 9: Call assert_array_equal()

```python
assert_array_equal(res, expected)
```

### Step 10: Call ufunc()

```python
ufunc(a, a, out=np.empty(a.shape, dtype=int), casting='equiv')
```


## Complete Example

```python
# Setup
# Fixtures: ufunc

# Workflow
a = self._get_array(2.0)
a[0] = 0.0
float_equiv = a.astype(float)
expected = ufunc(float_equiv, float_equiv)
res = ufunc(a, a)
assert_array_equal(res, expected)
expected = ufunc.reduce(float_equiv)
res = ufunc.reduce(a)
assert_array_equal(res, expected)
with pytest.raises(TypeError):
    ufunc(a, a, out=np.empty(a.shape, dtype=int), casting='equiv')
```

## Next Steps


---

*Source: test_custom_dtypes.py:200 | Complexity: Advanced | Last updated: 2026-06-02*