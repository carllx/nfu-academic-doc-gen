# How To: Cython Vs Numba

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test cython vs numba

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
# Fixtures: grouper, method, nogil, parallel, nopython, ignore_na, adjust
```

## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame({'B': range(4)})
```

### Step 2: Assign ewm = grouper.ewm(...)

```python
ewm = grouper(df).ewm(com=1.0, adjust=adjust, ignore_na=ignore_na)
```

### Step 3: Assign engine_kwargs = value

```python
engine_kwargs = {'nogil': nogil, 'parallel': parallel, 'nopython': nopython}
```

### Step 4: Assign result = getattr(...)

```python
result = getattr(ewm, method)(engine='numba', engine_kwargs=engine_kwargs)
```

### Step 5: Assign expected = getattr(...)

```python
expected = getattr(ewm, method)(engine='cython')
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign grouper = value

```python
grouper = lambda x: x
```

### Step 8: Assign unknown = value

```python
df['A'] = ['a', 'b', 'a', 'b']
```

### Step 9: Assign grouper = value

```python
grouper = lambda x: x.groupby('A')
```

### Step 10: Assign adjust = True

```python
adjust = True
```


## Complete Example

```python
# Setup
# Fixtures: grouper, method, nogil, parallel, nopython, ignore_na, adjust

# Workflow
df = DataFrame({'B': range(4)})
if grouper == 'None':
    grouper = lambda x: x
else:
    df['A'] = ['a', 'b', 'a', 'b']
    grouper = lambda x: x.groupby('A')
if method == 'sum':
    adjust = True
ewm = grouper(df).ewm(com=1.0, adjust=adjust, ignore_na=ignore_na)
engine_kwargs = {'nogil': nogil, 'parallel': parallel, 'nopython': nopython}
result = getattr(ewm, method)(engine='numba', engine_kwargs=engine_kwargs)
expected = getattr(ewm, method)(engine='cython')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_numba.py:250 | Complexity: Advanced | Last updated: 2026-06-02*