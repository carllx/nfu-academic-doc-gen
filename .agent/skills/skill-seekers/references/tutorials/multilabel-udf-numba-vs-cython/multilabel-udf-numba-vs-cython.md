# How To: Multilabel Udf Numba Vs Cython

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test multilabel udf numba vs cython

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

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'], 'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'], 'C': np.random.default_rng(2).standard_normal(8), 'D': np.random.default_rng(2).standard_normal(8)})
```

### Step 3: Assign gb = df.groupby(...)

```python
gb = df.groupby(['A', 'B'])
```

### Step 4: Assign result = gb.transform(...)

```python
result = gb.transform(lambda values, index: (values - values.min()) / (values.max() - values.min()), engine='numba')
```

### Step 5: Assign expected = gb.transform(...)

```python
expected = gb.transform(lambda x: (x - x.min()) / (x.max() - x.min()), engine='cython')
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Workflow
pytest.importorskip('numba')
df = DataFrame({'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'], 'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'], 'C': np.random.default_rng(2).standard_normal(8), 'D': np.random.default_rng(2).standard_normal(8)})
gb = df.groupby(['A', 'B'])
result = gb.transform(lambda values, index: (values - values.min()) / (values.max() - values.min()), engine='numba')
expected = gb.transform(lambda x: (x - x.min()) / (x.max() - x.min()), engine='cython')
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_numba.py:276 | Complexity: Intermediate | Last updated: 2026-06-02*