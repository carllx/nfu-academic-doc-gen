# How To: Multiindex One Key

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test multiindex one key

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
# Fixtures: nogil, parallel, nopython
```

## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('numba')
```

### Step 2: Assign df = DataFrame.set_index(...)

```python
df = DataFrame([{'A': 1, 'B': 2, 'C': 3}]).set_index(['A', 'B'])
```

### Step 3: Assign engine_kwargs = value

```python
engine_kwargs = {'nopython': nopython, 'nogil': nogil, 'parallel': parallel}
```

### Step 4: Assign result = df.groupby.agg(...)

```python
result = df.groupby('A').agg(numba_func, engine='numba', engine_kwargs=engine_kwargs)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame([1.0], index=Index([1], name='A'), columns=['C'])
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: nogil, parallel, nopython

# Workflow
pytest.importorskip('numba')

def numba_func(values, index):
    return 1
df = DataFrame([{'A': 1, 'B': 2, 'C': 3}]).set_index(['A', 'B'])
engine_kwargs = {'nopython': nopython, 'nogil': nogil, 'parallel': parallel}
result = df.groupby('A').agg(numba_func, engine='numba', engine_kwargs=engine_kwargs)
expected = DataFrame([1.0], index=Index([1], name='A'), columns=['C'])
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_numba.py:339 | Complexity: Intermediate | Last updated: 2026-06-02*