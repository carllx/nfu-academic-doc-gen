# How To: Table Method Rolling Apply

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test table method rolling apply

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
# Fixtures: axis, nogil, parallel, nopython, step
```

## Step-by-Step Guide

### Step 1: Assign engine_kwargs = value

```python
engine_kwargs = {'nogil': nogil, 'parallel': parallel, 'nopython': nopython}
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(np.eye(3))
```

### Step 3: Assign result = df.rolling.apply(...)

```python
result = df.rolling(2, method='table', axis=axis, min_periods=0, step=step).apply(f, raw=True, engine_kwargs=engine_kwargs, engine='numba')
```

### Step 4: Assign expected = df.rolling.apply(...)

```python
expected = df.rolling(2, method='single', axis=axis, min_periods=0, step=step).apply(f, raw=True, engine_kwargs=engine_kwargs, engine='numba')
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: axis, nogil, parallel, nopython, step

# Workflow
engine_kwargs = {'nogil': nogil, 'parallel': parallel, 'nopython': nopython}

def f(x):
    return np.sum(x, axis=0) + 1
df = DataFrame(np.eye(3))
result = df.rolling(2, method='table', axis=axis, min_periods=0, step=step).apply(f, raw=True, engine_kwargs=engine_kwargs, engine='numba')
expected = df.rolling(2, method='single', axis=axis, min_periods=0, step=step).apply(f, raw=True, engine_kwargs=engine_kwargs, engine='numba')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_numba.py:371 | Complexity: Intermediate | Last updated: 2026-06-02*