# How To: Multifunc Numba Vs Cython Series

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test multifunc numba vs cython series

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

### Step 2: Assign labels = value

```python
labels = ['a', 'a', 'b', 'b', 'a']
```

### Step 3: Assign data = Series(...)

```python
data = Series([1.0, 2.0, 3.0, 4.0, 5.0])
```

### Step 4: Assign grouped = data.groupby(...)

```python
grouped = data.groupby(labels)
```

### Step 5: Assign unknown = 'numba'

```python
agg_kwargs['engine'] = 'numba'
```

### Step 6: Assign result = grouped.agg(...)

```python
result = grouped.agg(**agg_kwargs)
```

### Step 7: Assign unknown = 'cython'

```python
agg_kwargs['engine'] = 'cython'
```

### Step 8: Assign expected = grouped.agg(...)

```python
expected = grouped.agg(**agg_kwargs)
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: agg_kwargs

# Workflow
pytest.importorskip('numba')
labels = ['a', 'a', 'b', 'b', 'a']
data = Series([1.0, 2.0, 3.0, 4.0, 5.0])
grouped = data.groupby(labels)
agg_kwargs['engine'] = 'numba'
result = grouped.agg(**agg_kwargs)
agg_kwargs['engine'] = 'cython'
expected = grouped.agg(**agg_kwargs)
if isinstance(expected, DataFrame):
    tm.assert_frame_equal(result, expected)
else:
    tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_numba.py:218 | Complexity: Advanced | Last updated: 2026-06-02*