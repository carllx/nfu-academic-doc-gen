# How To: Engine Kwargs Not Cached

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test engine kwargs not cached

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas.errors`
- `pandas`
- `pandas._testing`
- `pandas.util.version`
- `numba`
- `numba`


## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('numba')
```

### Step 2: Assign nogil = True

```python
nogil = True
```

### Step 3: Assign parallel = False

```python
parallel = False
```

### Step 4: Assign nopython = True

```python
nopython = True
```

### Step 5: Assign engine_kwargs = value

```python
engine_kwargs = {'nopython': nopython, 'nogil': nogil, 'parallel': parallel}
```

### Step 6: Assign df = DataFrame(...)

```python
df = DataFrame({'value': [0, 0, 0]})
```

### Step 7: Assign result = df.groupby.aggregate(...)

```python
result = df.groupby(level=0).aggregate(func_kwargs, engine='numba', engine_kwargs=engine_kwargs)
```

### Step 8: Assign expected = DataFrame(...)

```python
expected = DataFrame({'value': [2.0, 2.0, 2.0]})
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Assign nogil = False

```python
nogil = False
```

### Step 11: Assign engine_kwargs = value

```python
engine_kwargs = {'nopython': nopython, 'nogil': nogil, 'parallel': parallel}
```

### Step 12: Assign result = df.groupby.aggregate(...)

```python
result = df.groupby(level=0).aggregate(func_kwargs, engine='numba', engine_kwargs=engine_kwargs)
```

### Step 13: Assign expected = DataFrame(...)

```python
expected = DataFrame({'value': [1.0, 1.0, 1.0]})
```

### Step 14: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
pytest.importorskip('numba')
nogil = True
parallel = False
nopython = True

def func_kwargs(values, index):
    return nogil + parallel + nopython
engine_kwargs = {'nopython': nopython, 'nogil': nogil, 'parallel': parallel}
df = DataFrame({'value': [0, 0, 0]})
result = df.groupby(level=0).aggregate(func_kwargs, engine='numba', engine_kwargs=engine_kwargs)
expected = DataFrame({'value': [2.0, 2.0, 2.0]})
tm.assert_frame_equal(result, expected)
nogil = False
engine_kwargs = {'nopython': nopython, 'nogil': nogil, 'parallel': parallel}
result = df.groupby(level=0).aggregate(func_kwargs, engine='numba', engine_kwargs=engine_kwargs)
expected = DataFrame({'value': [1.0, 1.0, 1.0]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_numba.py:310 | Complexity: Advanced | Last updated: 2026-06-02*