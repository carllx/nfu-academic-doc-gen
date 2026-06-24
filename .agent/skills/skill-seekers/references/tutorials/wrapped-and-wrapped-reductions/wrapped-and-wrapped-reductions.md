# How To: Wrapped And Wrapped Reductions

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test wrapped and wrapped reductions

## Prerequisites

**Required Modules:**
- `tempfile`
- `pytest`
- `numpy`
- `numpy._core._multiarray_umath`
- `numpy.testing`
- `pickle`


## Step-by-Step Guide

### Step 1: Assign a = self._get_array(...)

```python
a = self._get_array(2.0)
```

**Verification:**
```python
assert res.dtype == a.dtype
```

### Step 2: Assign float_equiv = a.astype(...)

```python
float_equiv = a.astype(float)
```

**Verification:**
```python
assert_array_equal(res_float, expected)
```

### Step 3: Assign expected = np.hypot(...)

```python
expected = np.hypot(float_equiv, float_equiv)
```

**Verification:**
```python
assert res.dtype == a.dtype
```

### Step 4: Assign res = np.hypot(...)

```python
res = np.hypot(a, a)
```

**Verification:**
```python
assert res.view(np.float64) * 2 == expected
```

### Step 5: Assign res_float = value

```python
res_float = res.view(np.float64) * 2
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(res_float, expected)
```

### Step 7: Assign res = np.hypot.reduce(...)

```python
res = np.hypot.reduce(a, keepdims=True)
```

**Verification:**
```python
assert res.dtype == a.dtype
```

### Step 8: Assign expected = np.hypot.reduce(...)

```python
expected = np.hypot.reduce(float_equiv, keepdims=True)
```

**Verification:**
```python
assert res.view(np.float64) * 2 == expected
```


## Complete Example

```python
# Workflow
a = self._get_array(2.0)
float_equiv = a.astype(float)
expected = np.hypot(float_equiv, float_equiv)
res = np.hypot(a, a)
assert res.dtype == a.dtype
res_float = res.view(np.float64) * 2
assert_array_equal(res_float, expected)
res = np.hypot.reduce(a, keepdims=True)
assert res.dtype == a.dtype
expected = np.hypot.reduce(float_equiv, keepdims=True)
assert res.view(np.float64) * 2 == expected
```

## Next Steps


---

*Source: test_custom_dtypes.py:218 | Complexity: Advanced | Last updated: 2026-06-02*