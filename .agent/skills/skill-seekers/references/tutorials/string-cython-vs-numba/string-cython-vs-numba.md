# How To: String Cython Vs Numba

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test string cython vs numba

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
# Fixtures: agg_func, numba_supported_reductions
```

## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('numba')
```

### Step 2: Assign unknown = numba_supported_reductions

```python
agg_func, kwargs = numba_supported_reductions
```

### Step 3: Assign data = DataFrame(...)

```python
data = DataFrame({0: ['a', 'a', 'b', 'b', 'a'], 1: [1.0, 2.0, 3.0, 4.0, 5.0]}, columns=[0, 1])
```

### Step 4: Assign grouped = data.groupby(...)

```python
grouped = data.groupby(0)
```

### Step 5: Assign result = grouped.transform(...)

```python
result = grouped.transform(agg_func, engine='numba', **kwargs)
```

### Step 6: Assign expected = grouped.transform(...)

```python
expected = grouped.transform(agg_func, engine='cython', **kwargs)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = unknown.transform(...)

```python
result = grouped[1].transform(agg_func, engine='numba', **kwargs)
```

### Step 9: Assign expected = unknown.transform(...)

```python
expected = grouped[1].transform(agg_func, engine='cython', **kwargs)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: agg_func, numba_supported_reductions

# Workflow
pytest.importorskip('numba')
agg_func, kwargs = numba_supported_reductions
data = DataFrame({0: ['a', 'a', 'b', 'b', 'a'], 1: [1.0, 2.0, 3.0, 4.0, 5.0]}, columns=[0, 1])
grouped = data.groupby(0)
result = grouped.transform(agg_func, engine='numba', **kwargs)
expected = grouped.transform(agg_func, engine='cython', **kwargs)
tm.assert_frame_equal(result, expected)
result = grouped[1].transform(agg_func, engine='numba', **kwargs)
expected = grouped[1].transform(agg_func, engine='cython', **kwargs)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_numba.py:153 | Complexity: Advanced | Last updated: 2026-06-02*