# How To: Multilabel Numba Vs Cython

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multilabel numba vs cython

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
# Fixtures: numba_supported_reductions
```

## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('numba')
```

### Step 2: Assign unknown = numba_supported_reductions

```python
reduction, kwargs = numba_supported_reductions
```

### Step 3: Assign df = DataFrame(...)

```python
df = DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'], 'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'], 'C': np.random.default_rng(2).standard_normal(8), 'D': np.random.default_rng(2).standard_normal(8)})
```

### Step 4: Assign gb = df.groupby(...)

```python
gb = df.groupby(['A', 'B'])
```

### Step 5: Assign res_agg = gb.transform(...)

```python
res_agg = gb.transform(reduction, engine='numba', **kwargs)
```

### Step 6: Assign expected_agg = gb.transform(...)

```python
expected_agg = gb.transform(reduction, engine='cython', **kwargs)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res_agg, expected_agg)
```


## Complete Example

```python
# Setup
# Fixtures: numba_supported_reductions

# Workflow
pytest.importorskip('numba')
reduction, kwargs = numba_supported_reductions
df = DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'], 'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'], 'C': np.random.default_rng(2).standard_normal(8), 'D': np.random.default_rng(2).standard_normal(8)})
gb = df.groupby(['A', 'B'])
res_agg = gb.transform(reduction, engine='numba', **kwargs)
expected_agg = gb.transform(reduction, engine='cython', **kwargs)
tm.assert_frame_equal(res_agg, expected_agg)
```

## Next Steps


---

*Source: test_numba.py:259 | Complexity: Intermediate | Last updated: 2026-06-02*