# How To: Cache

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test cache

## Prerequisites

- [ ] Setup code must be executed first

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

**Setup Required:**
```python
# Fixtures: jit, pandas_obj, nogil, parallel, nopython
```

## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('numba')
```

### Step 2: Assign data = DataFrame(...)

```python
data = DataFrame({0: ['a', 'a', 'b', 'b', 'a'], 1: [1.0, 2.0, 3.0, 4.0, 5.0]}, columns=[0, 1])
```

### Step 3: Assign engine_kwargs = value

```python
engine_kwargs = {'nogil': nogil, 'parallel': parallel, 'nopython': nopython}
```

### Step 4: Assign grouped = data.groupby(...)

```python
grouped = data.groupby(0)
```

### Step 5: Assign result = grouped.agg(...)

```python
result = grouped.agg(func_1, engine='numba', engine_kwargs=engine_kwargs)
```

### Step 6: Assign expected = grouped.agg(...)

```python
expected = grouped.agg(lambda x: np.mean(x) - 3.4, engine='cython')
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 8: Assign result = grouped.agg(...)

```python
result = grouped.agg(func_2, engine='numba', engine_kwargs=engine_kwargs)
```

### Step 9: Assign expected = grouped.agg(...)

```python
expected = grouped.agg(lambda x: np.mean(x) * 2.7, engine='cython')
```

### Step 10: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 11: Assign result = grouped.agg(...)

```python
result = grouped.agg(func_1, engine='numba', engine_kwargs=engine_kwargs)
```

### Step 12: Assign expected = grouped.agg(...)

```python
expected = grouped.agg(lambda x: np.mean(x) - 3.4, engine='cython')
```

### Step 13: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 14: Assign func_1 = numba.jit(...)

```python
func_1 = numba.jit(func_1)
```

### Step 15: Assign func_2 = numba.jit(...)

```python
func_2 = numba.jit(func_2)
```

### Step 16: Assign grouped = value

```python
grouped = grouped[1]
```


## Complete Example

```python
# Setup
# Fixtures: jit, pandas_obj, nogil, parallel, nopython

# Workflow
pytest.importorskip('numba')

def func_1(values, index):
    return np.mean(values) - 3.4

def func_2(values, index):
    return np.mean(values) * 2.7
if jit:
    import numba
    func_1 = numba.jit(func_1)
    func_2 = numba.jit(func_2)
data = DataFrame({0: ['a', 'a', 'b', 'b', 'a'], 1: [1.0, 2.0, 3.0, 4.0, 5.0]}, columns=[0, 1])
engine_kwargs = {'nogil': nogil, 'parallel': parallel, 'nopython': nopython}
grouped = data.groupby(0)
if pandas_obj == 'Series':
    grouped = grouped[1]
result = grouped.agg(func_1, engine='numba', engine_kwargs=engine_kwargs)
expected = grouped.agg(lambda x: np.mean(x) - 3.4, engine='cython')
tm.assert_equal(result, expected)
result = grouped.agg(func_2, engine='numba', engine_kwargs=engine_kwargs)
expected = grouped.agg(lambda x: np.mean(x) * 2.7, engine='cython')
tm.assert_equal(result, expected)
result = grouped.agg(func_1, engine='numba', engine_kwargs=engine_kwargs)
expected = grouped.agg(lambda x: np.mean(x) - 3.4, engine='cython')
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_numba.py:97 | Complexity: Advanced | Last updated: 2026-06-02*