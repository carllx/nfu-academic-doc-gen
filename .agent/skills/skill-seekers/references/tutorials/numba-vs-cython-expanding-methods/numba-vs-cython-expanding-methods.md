# How To: Numba Vs Cython Expanding Methods

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test numba vs cython expanding methods

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.util.version`
- `numba`
- `numba`

**Setup Required:**
```python
# Fixtures: data, nogil, parallel, nopython, arithmetic_numba_supported_operators
```

## Step-by-Step Guide

### Step 1: Assign unknown = arithmetic_numba_supported_operators

```python
method, kwargs = arithmetic_numba_supported_operators
```

### Step 2: Assign engine_kwargs = value

```python
engine_kwargs = {'nogil': nogil, 'parallel': parallel, 'nopython': nopython}
```

### Step 3: Assign data = DataFrame(...)

```python
data = DataFrame(np.eye(5))
```

### Step 4: Assign expand = data.expanding(...)

```python
expand = data.expanding()
```

### Step 5: Assign result = getattr(...)

```python
result = getattr(expand, method)(engine='numba', engine_kwargs=engine_kwargs, **kwargs)
```

### Step 6: Assign expected = getattr(...)

```python
expected = getattr(expand, method)(engine='cython', **kwargs)
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: data, nogil, parallel, nopython, arithmetic_numba_supported_operators

# Workflow
method, kwargs = arithmetic_numba_supported_operators
engine_kwargs = {'nogil': nogil, 'parallel': parallel, 'nopython': nopython}
data = DataFrame(np.eye(5))
expand = data.expanding()
result = getattr(expand, method)(engine='numba', engine_kwargs=engine_kwargs, **kwargs)
expected = getattr(expand, method)(engine='cython', **kwargs)
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_numba.py:119 | Complexity: Intermediate | Last updated: 2026-06-02*