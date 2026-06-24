# How To: Args Not Cached

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test args not cached

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
df = DataFrame({'id': [0, 0, 1, 1], 'x': [1, 1, 1, 1]})
```

### Step 3: Assign grouped_x = value

```python
grouped_x = df.groupby('id')['x']
```

### Step 4: Assign result = grouped_x.agg(...)

```python
result = grouped_x.agg(sum_last, 1, engine='numba')
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([1.0] * 2, name='x', index=Index([0, 1], name='id'))
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign result = grouped_x.agg(...)

```python
result = grouped_x.agg(sum_last, 2, engine='numba')
```

### Step 8: Assign expected = Series(...)

```python
expected = Series([2.0] * 2, name='x', index=Index([0, 1], name='id'))
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
pytest.importorskip('numba')

def sum_last(values, index, n):
    return values[-n:].sum()
df = DataFrame({'id': [0, 0, 1, 1], 'x': [1, 1, 1, 1]})
grouped_x = df.groupby('id')['x']
result = grouped_x.agg(sum_last, 1, engine='numba')
expected = Series([1.0] * 2, name='x', index=Index([0, 1], name='id'))
tm.assert_series_equal(result, expected)
result = grouped_x.agg(sum_last, 2, engine='numba')
expected = Series([2.0] * 2, name='x', index=Index([0, 1], name='id'))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_numba.py:277 | Complexity: Advanced | Last updated: 2026-06-02*