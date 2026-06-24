# How To: Numba Vs Cython

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test numba vs cython

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
# Fixtures: jit, pandas_obj, nogil, parallel, nopython, as_index
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
grouped = data.groupby(0, as_index=as_index)
```

### Step 5: Assign result = grouped.agg(...)

```python
result = grouped.agg(func_numba, engine='numba', engine_kwargs=engine_kwargs)
```

### Step 6: Assign expected = grouped.agg(...)

```python
expected = grouped.agg(lambda x: np.mean(x) * 2.7, engine='cython')
```

### Step 7: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 8: Assign func_numba = numba.jit(...)

```python
func_numba = numba.jit(func_numba)
```

### Step 9: Assign grouped = value

```python
grouped = grouped[1]
```


## Complete Example

```python
# Setup
# Fixtures: jit, pandas_obj, nogil, parallel, nopython, as_index

# Workflow
pytest.importorskip('numba')

def func_numba(values, index):
    return np.mean(values) * 2.7
if jit:
    import numba
    func_numba = numba.jit(func_numba)
data = DataFrame({0: ['a', 'a', 'b', 'b', 'a'], 1: [1.0, 2.0, 3.0, 4.0, 5.0]}, columns=[0, 1])
engine_kwargs = {'nogil': nogil, 'parallel': parallel, 'nopython': nopython}
grouped = data.groupby(0, as_index=as_index)
if pandas_obj == 'Series':
    grouped = grouped[1]
result = grouped.agg(func_numba, engine='numba', engine_kwargs=engine_kwargs)
expected = grouped.agg(lambda x: np.mean(x) * 2.7, engine='cython')
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_numba.py:67 | Complexity: Advanced | Last updated: 2026-06-02*