# How To: Basic Multiply Promotion

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test basic multiply promotion

## Prerequisites

**Required Modules:**
- `tempfile`
- `pytest`
- `numpy`
- `numpy._core._multiarray_umath`
- `numpy.testing`
- `pickle`


## Step-by-Step Guide

### Step 1: Assign float_a = np.array(...)

```python
float_a = np.array([1.0, 2.0, 3.0])
```

**Verification:**
```python
assert res1.dtype == res2.dtype == b.dtype
```

### Step 2: Assign b = self._get_array(...)

```python
b = self._get_array(2.0)
```

**Verification:**
```python
assert_array_equal(res1.view(np.float64), expected_view)
```

### Step 3: Assign res1 = value

```python
res1 = float_a * b
```

**Verification:**
```python
assert_array_equal(res2.view(np.float64), expected_view)
```

### Step 4: Assign res2 = value

```python
res2 = b * float_a
```

**Verification:**
```python
assert res1.dtype == res2.dtype == b.dtype
```

### Step 5: Assign expected_view = value

```python
expected_view = float_a * b.view(np.float64)
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(res1.view(np.float64), expected_view)
```

### Step 7: Call assert_array_equal()

```python
assert_array_equal(res2.view(np.float64), expected_view)
```

### Step 8: Call np.multiply()

```python
np.multiply(b, float_a, out=res2)
```

### Step 9: Call np.multiply()

```python
np.multiply(b, float_a, out=np.arange(3))
```


## Complete Example

```python
# Workflow
float_a = np.array([1.0, 2.0, 3.0])
b = self._get_array(2.0)
res1 = float_a * b
res2 = b * float_a
assert res1.dtype == res2.dtype == b.dtype
expected_view = float_a * b.view(np.float64)
assert_array_equal(res1.view(np.float64), expected_view)
assert_array_equal(res2.view(np.float64), expected_view)
np.multiply(b, float_a, out=res2)
with pytest.raises(TypeError):
    np.multiply(b, float_a, out=np.arange(3))
```

## Next Steps


---

*Source: test_custom_dtypes.py:145 | Complexity: Advanced | Last updated: 2026-06-02*