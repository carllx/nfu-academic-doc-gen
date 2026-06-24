# How To: Numba Vs Cython Rolling Methods

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test numba vs cython rolling methods

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
# Fixtures: data, nogil, parallel, nopython, arithmetic_numba_supported_operators, step
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

### Step 3: Assign roll = data.rolling(...)

```python
roll = data.rolling(3, step=step)
```

### Step 4: Assign result = getattr(...)

```python
result = getattr(roll, method)(engine='numba', engine_kwargs=engine_kwargs, **kwargs)
```

### Step 5: Assign expected = getattr(...)

```python
expected = getattr(roll, method)(engine='cython', **kwargs)
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: data, nogil, parallel, nopython, arithmetic_numba_supported_operators, step

# Workflow
method, kwargs = arithmetic_numba_supported_operators
engine_kwargs = {'nogil': nogil, 'parallel': parallel, 'nopython': nopython}
roll = data.rolling(3, step=step)
result = getattr(roll, method)(engine='numba', engine_kwargs=engine_kwargs, **kwargs)
expected = getattr(roll, method)(engine='cython', **kwargs)
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_numba.py:96 | Complexity: Intermediate | Last updated: 2026-06-02*