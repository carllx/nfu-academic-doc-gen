# How To: Multifunc Numba Vs Cython Frame

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test multifunc numba vs cython frame

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
# Fixtures: agg_kwargs
```

## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('numba')
```

### Step 2: Assign data = DataFrame(...)

```python
data = DataFrame({0: ['a', 'a', 'b', 'b', 'a'], 1: [1.0, 2.0, 3.0, 4.0, 5.0], 2: [1, 2, 3, 4, 5]}, columns=[0, 1, 2])
```

### Step 3: Assign grouped = data.groupby(...)

```python
grouped = data.groupby(0)
```

### Step 4: Assign result = grouped.agg(...)

```python
result = grouped.agg(**agg_kwargs, engine='numba')
```

### Step 5: Assign expected = grouped.agg(...)

```python
expected = grouped.agg(**agg_kwargs, engine='cython')
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: agg_kwargs

# Workflow
pytest.importorskip('numba')
data = DataFrame({0: ['a', 'a', 'b', 'b', 'a'], 1: [1.0, 2.0, 3.0, 4.0, 5.0], 2: [1, 2, 3, 4, 5]}, columns=[0, 1, 2])
grouped = data.groupby(0)
result = grouped.agg(**agg_kwargs, engine='numba')
expected = grouped.agg(**agg_kwargs, engine='cython')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_numba.py:161 | Complexity: Intermediate | Last updated: 2026-06-02*