# How To: Cache Apply

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test cache apply

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
# Fixtures: jit, nogil, parallel, nopython, step
```

## Step-by-Step Guide

### Step 1: Assign engine_kwargs = value

```python
engine_kwargs = {'nogil': nogil, 'parallel': parallel, 'nopython': nopython}
```

### Step 2: Assign roll = Series.rolling(...)

```python
roll = Series(range(10)).rolling(2, step=step)
```

### Step 3: Assign result = roll.apply(...)

```python
result = roll.apply(func_1, engine='numba', engine_kwargs=engine_kwargs, raw=True)
```

### Step 4: Assign expected = roll.apply(...)

```python
expected = roll.apply(func_1, engine='cython', raw=True)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign result = roll.apply(...)

```python
result = roll.apply(func_2, engine='numba', engine_kwargs=engine_kwargs, raw=True)
```

### Step 7: Assign expected = roll.apply(...)

```python
expected = roll.apply(func_2, engine='cython', raw=True)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 9: Assign result = roll.apply(...)

```python
result = roll.apply(func_1, engine='numba', engine_kwargs=engine_kwargs, raw=True)
```

### Step 10: Assign expected = roll.apply(...)

```python
expected = roll.apply(func_1, engine='cython', raw=True)
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 12: Assign func_1 = numba.jit(...)

```python
func_1 = numba.jit(func_1)
```

### Step 13: Assign func_2 = numba.jit(...)

```python
func_2 = numba.jit(func_2)
```


## Complete Example

```python
# Setup
# Fixtures: jit, nogil, parallel, nopython, step

# Workflow
def func_1(x):
    return np.mean(x) + 4

def func_2(x):
    return np.std(x) * 5
if jit:
    import numba
    func_1 = numba.jit(func_1)
    func_2 = numba.jit(func_2)
engine_kwargs = {'nogil': nogil, 'parallel': parallel, 'nopython': nopython}
roll = Series(range(10)).rolling(2, step=step)
result = roll.apply(func_1, engine='numba', engine_kwargs=engine_kwargs, raw=True)
expected = roll.apply(func_1, engine='cython', raw=True)
tm.assert_series_equal(result, expected)
result = roll.apply(func_2, engine='numba', engine_kwargs=engine_kwargs, raw=True)
expected = roll.apply(func_2, engine='cython', raw=True)
tm.assert_series_equal(result, expected)
result = roll.apply(func_1, engine='numba', engine_kwargs=engine_kwargs, raw=True)
expected = roll.apply(func_1, engine='cython', raw=True)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_numba.py:135 | Complexity: Advanced | Last updated: 2026-06-02*