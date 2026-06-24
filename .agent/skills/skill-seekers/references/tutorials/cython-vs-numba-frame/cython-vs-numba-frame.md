# How To: Cython Vs Numba Frame

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cython vs numba frame

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.util.version`

**Setup Required:**
```python
# Fixtures: sort, nogil, parallel, nopython, numba_supported_reductions
```

## Step-by-Step Guide

### Step 1: Assign unknown = numba_supported_reductions

```python
func, kwargs = numba_supported_reductions
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'a': [3, 2, 3, 2], 'b': range(4), 'c': range(1, 5)})
```

### Step 3: Assign engine_kwargs = value

```python
engine_kwargs = {'nogil': nogil, 'parallel': parallel, 'nopython': nopython}
```

### Step 4: Assign gb = df.groupby(...)

```python
gb = df.groupby('a', sort=sort)
```

### Step 5: Assign result = getattr(...)

```python
result = getattr(gb, func)(engine='numba', engine_kwargs=engine_kwargs, **kwargs)
```

### Step 6: Assign expected = getattr(...)

```python
expected = getattr(gb, func)(**kwargs)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: sort, nogil, parallel, nopython, numba_supported_reductions

# Workflow
func, kwargs = numba_supported_reductions
df = DataFrame({'a': [3, 2, 3, 2], 'b': range(4), 'c': range(1, 5)})
engine_kwargs = {'nogil': nogil, 'parallel': parallel, 'nopython': nopython}
gb = df.groupby('a', sort=sort)
result = getattr(gb, func)(engine='numba', engine_kwargs=engine_kwargs, **kwargs)
expected = getattr(gb, func)(**kwargs)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_numba.py:27 | Complexity: Intermediate | Last updated: 2026-06-02*