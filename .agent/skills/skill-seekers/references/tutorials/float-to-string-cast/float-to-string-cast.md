# How To: Float To String Cast

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test float to string cast

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `operator`
- `sys`
- `pytest`
- `numpy`
- `numpy._core._exceptions`
- `numpy.testing`
- `numpy.testing._private.utils`

**Setup Required:**
```python
# Fixtures: str_dt, float_dt
```

## Step-by-Step Guide

### Step 1: Assign float_dt = np.dtype(...)

```python
float_dt = np.dtype(float_dt)
```

**Verification:**
```python
assert_array_equal(res, np.array(expected, dtype=str_dt))
```

### Step 2: Assign fi = np.finfo(...)

```python
fi = np.finfo(float_dt)
```

### Step 3: Assign arr = np.array(...)

```python
arr = np.array([np.nan, np.inf, -np.inf, fi.max, fi.min], dtype=float_dt)
```

### Step 4: Assign expected = value

```python
expected = ['nan', 'inf', '-inf', str(fi.max), str(fi.min)]
```

### Step 5: Assign res = arr.astype(...)

```python
res = arr.astype(str_dt)
```

### Step 6: Call assert_array_equal()

```python
assert_array_equal(res, np.array(expected, dtype=str_dt))
```

### Step 7: Assign expected = value

```python
expected = [f'({r}+0j)' for r in expected]
```


## Complete Example

```python
# Setup
# Fixtures: str_dt, float_dt

# Workflow
float_dt = np.dtype(float_dt)
fi = np.finfo(float_dt)
arr = np.array([np.nan, np.inf, -np.inf, fi.max, fi.min], dtype=float_dt)
expected = ['nan', 'inf', '-inf', str(fi.max), str(fi.min)]
if float_dt.kind == 'c':
    expected = [f'({r}+0j)' for r in expected]
res = arr.astype(str_dt)
assert_array_equal(res, np.array(expected, dtype=str_dt))
```

## Next Steps


---

*Source: test_strings.py:101 | Complexity: Intermediate | Last updated: 2026-06-02*