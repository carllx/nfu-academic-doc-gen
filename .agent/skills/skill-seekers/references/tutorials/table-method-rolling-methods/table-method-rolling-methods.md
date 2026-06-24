# How To: Table Method Rolling Methods

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test table method rolling methods

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
# Fixtures: axis, nogil, parallel, nopython, arithmetic_numba_supported_operators, step
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

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame(np.eye(3))
```

### Step 4: Assign roll_table = df.rolling(...)

```python
roll_table = df.rolling(2, method='table', axis=axis, min_periods=0, step=step)
```

### Step 5: Assign roll_single = df.rolling(...)

```python
roll_single = df.rolling(2, method='single', axis=axis, min_periods=0, step=step)
```

### Step 6: Assign result = getattr(...)

```python
result = getattr(roll_table, method)(engine_kwargs=engine_kwargs, engine='numba', **kwargs)
```

### Step 7: Assign expected = getattr(...)

```python
expected = getattr(roll_single, method)(engine_kwargs=engine_kwargs, engine='numba', **kwargs)
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Call getattr()

```python
getattr(roll_table, method)(engine_kwargs=engine_kwargs, engine='numba', **kwargs)
```


## Complete Example

```python
# Setup
# Fixtures: axis, nogil, parallel, nopython, arithmetic_numba_supported_operators, step

# Workflow
method, kwargs = arithmetic_numba_supported_operators
engine_kwargs = {'nogil': nogil, 'parallel': parallel, 'nopython': nopython}
df = DataFrame(np.eye(3))
roll_table = df.rolling(2, method='table', axis=axis, min_periods=0, step=step)
if method in ('var', 'std'):
    with pytest.raises(NotImplementedError, match=f'{method} not supported'):
        getattr(roll_table, method)(engine_kwargs=engine_kwargs, engine='numba', **kwargs)
else:
    roll_single = df.rolling(2, method='single', axis=axis, min_periods=0, step=step)
    result = getattr(roll_table, method)(engine_kwargs=engine_kwargs, engine='numba', **kwargs)
    expected = getattr(roll_single, method)(engine_kwargs=engine_kwargs, engine='numba', **kwargs)
    tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_numba.py:339 | Complexity: Advanced | Last updated: 2026-06-02*