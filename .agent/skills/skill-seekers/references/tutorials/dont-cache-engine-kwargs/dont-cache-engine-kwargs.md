# How To: Dont Cache Engine Kwargs

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dont cache engine kwargs

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign nogil = False

```python
nogil = False
```

### Step 2: Assign parallel = True

```python
parallel = True
```

### Step 3: Assign nopython = True

```python
nopython = True
```

### Step 4: Assign engine_kwargs = value

```python
engine_kwargs = {'nopython': nopython, 'nogil': nogil, 'parallel': parallel}
```

### Step 5: Assign df = DataFrame(...)

```python
df = DataFrame({'value': [0, 0, 0]})
```

### Step 6: Assign result = df.rolling.apply(...)

```python
result = df.rolling(1).apply(func, raw=True, engine='numba', engine_kwargs=engine_kwargs)
```

### Step 7: Assign expected = DataFrame(...)

```python
expected = DataFrame({'value': [2.0, 2.0, 2.0]})
```

### Step 8: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 9: Assign parallel = False

```python
parallel = False
```

### Step 10: Assign engine_kwargs = value

```python
engine_kwargs = {'nopython': nopython, 'nogil': nogil, 'parallel': parallel}
```

### Step 11: Assign result = df.rolling.apply(...)

```python
result = df.rolling(1).apply(func, raw=True, engine='numba', engine_kwargs=engine_kwargs)
```

### Step 12: Assign expected = DataFrame(...)

```python
expected = DataFrame({'value': [1.0, 1.0, 1.0]})
```

### Step 13: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
nogil = False
parallel = True
nopython = True

def func(x):
    return nogil + parallel + nopython
engine_kwargs = {'nopython': nopython, 'nogil': nogil, 'parallel': parallel}
df = DataFrame({'value': [0, 0, 0]})
result = df.rolling(1).apply(func, raw=True, engine='numba', engine_kwargs=engine_kwargs)
expected = DataFrame({'value': [2.0, 2.0, 2.0]})
tm.assert_frame_equal(result, expected)
parallel = False
engine_kwargs = {'nopython': nopython, 'nogil': nogil, 'parallel': parallel}
result = df.rolling(1).apply(func, raw=True, engine='numba', engine_kwargs=engine_kwargs)
expected = DataFrame({'value': [1.0, 1.0, 1.0]})
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_numba.py:199 | Complexity: Advanced | Last updated: 2026-06-02*