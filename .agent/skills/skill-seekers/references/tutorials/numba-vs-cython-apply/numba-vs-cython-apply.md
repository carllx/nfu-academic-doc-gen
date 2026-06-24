# How To: Numba Vs Cython Apply

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test numba vs cython apply

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
# Fixtures: jit, nogil, parallel, nopython, center, step
```

## Step-by-Step Guide

### Step 1: Assign engine_kwargs = value

```python
engine_kwargs = {'nogil': nogil, 'parallel': parallel, 'nopython': nopython}
```

### Step 2: Assign args = value

```python
args = (2,)
```

### Step 3: Assign s = Series(...)

```python
s = Series(range(10))
```

### Step 4: Assign result = s.rolling.apply(...)

```python
result = s.rolling(2, center=center, step=step).apply(f, args=args, engine='numba', engine_kwargs=engine_kwargs, raw=True)
```

### Step 5: Assign expected = s.rolling.apply(...)

```python
expected = s.rolling(2, center=center, step=step).apply(f, engine='cython', args=args, raw=True)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign arg_sum = 0

```python
arg_sum = 0
```

### Step 8: Assign f = numba.jit(...)

```python
f = numba.jit(f)
```


## Complete Example

```python
# Setup
# Fixtures: jit, nogil, parallel, nopython, center, step

# Workflow
def f(x, *args):
    arg_sum = 0
    for arg in args:
        arg_sum += arg
    return np.mean(x) + arg_sum
if jit:
    import numba
    f = numba.jit(f)
engine_kwargs = {'nogil': nogil, 'parallel': parallel, 'nopython': nopython}
args = (2,)
s = Series(range(10))
result = s.rolling(2, center=center, step=step).apply(f, args=args, engine='numba', engine_kwargs=engine_kwargs, raw=True)
expected = s.rolling(2, center=center, step=step).apply(f, engine='cython', args=args, raw=True)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_numba.py:56 | Complexity: Advanced | Last updated: 2026-06-02*