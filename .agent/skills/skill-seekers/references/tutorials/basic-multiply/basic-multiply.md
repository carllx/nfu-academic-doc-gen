# How To: Basic Multiply

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test basic multiply

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
assert res.dtype.get_scaling() == 8.0
```

### Step 2: Assign b = self._get_array(...)

```python
b = self._get_array(4.0)
```

**Verification:**
```python
assert_array_equal(res.view(np.float64), expected_view)
```

### Step 3: Assign res = value

```python
res = a * b
```

**Verification:**
```python
assert res.dtype.get_scaling() == 8.0
```

### Step 4: Assign expected_view = value

```python
expected_view = a.view(np.float64) * b.view(np.float64)
```

### Step 5: Call assert_array_equal()

```python
assert_array_equal(res.view(np.float64), expected_view)
```


## Complete Example

```python
# Workflow
a = self._get_array(2.0)
b = self._get_array(4.0)
res = a * b
assert res.dtype.get_scaling() == 8.0
expected_view = a.view(np.float64) * b.view(np.float64)
assert_array_equal(res.view(np.float64), expected_view)
```

## Next Steps


---

*Source: test_custom_dtypes.py:109 | Complexity: Intermediate | Last updated: 2026-06-02*