# How To: Dont Cache Args

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dont cache args

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
# Fixtures: window, window_kwargs, nogil, parallel, nopython, method
```

## Step-by-Step Guide

### Step 1: Assign engine_kwargs = value

```python
engine_kwargs = {'nopython': nopython, 'nogil': nogil, 'parallel': parallel}
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'value': [0, 0, 0]})
```

### Step 3: Assign result = getattr.apply(...)

```python
result = getattr(df, window)(method=method, **window_kwargs).apply(add, raw=True, engine='numba', engine_kwargs=engine_kwargs, args=(1,))
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({'value': [1.0, 1.0, 1.0]})
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign result = getattr.apply(...)

```python
result = getattr(df, window)(method=method, **window_kwargs).apply(add, raw=True, engine='numba', engine_kwargs=engine_kwargs, args=(2,))
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame({'value': [2.0, 2.0, 2.0]})
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: window, window_kwargs, nogil, parallel, nopython, method

# Workflow
def add(values, x):
    return np.sum(values) + x
engine_kwargs = {'nopython': nopython, 'nogil': nogil, 'parallel': parallel}
df = DataFrame({'value': [0, 0, 0]})
result = getattr(df, window)(method=method, **window_kwargs).apply(add, raw=True, engine='numba', engine_kwargs=engine_kwargs, args=(1,))
expected = DataFrame({'value': [1.0, 1.0, 1.0]})
tm.assert_frame_equal(result, expected)
result = getattr(df, window)(method=method, **window_kwargs).apply(add, raw=True, engine='numba', engine_kwargs=engine_kwargs, args=(2,))
expected = DataFrame({'value': [2.0, 2.0, 2.0]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_numba.py:177 | Complexity: Advanced | Last updated: 2026-06-02*