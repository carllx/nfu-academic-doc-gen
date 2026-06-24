# How To: Multifunc Numba Kwarg Propagation

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test multifunc numba kwarg propagation

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
# Fixtures: data, agg_kwargs
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

### Step 3: Assign grouped = data.groupby(...)

```python
grouped = data.groupby(labels)
```

### Step 4: Assign result = grouped.agg(...)

```python
result = grouped.agg(**agg_kwargs, engine='numba', engine_kwargs={'parallel': True})
```

### Step 5: Assign expected = grouped.agg(...)

```python
expected = grouped.agg(**agg_kwargs, engine='numba')
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: data, agg_kwargs

# Workflow
pytest.importorskip('numba')
labels = ['a', 'a', 'b', 'b', 'a']
grouped = data.groupby(labels)
result = grouped.agg(**agg_kwargs, engine='numba', engine_kwargs={'parallel': True})
expected = grouped.agg(**agg_kwargs, engine='numba')
if isinstance(expected, DataFrame):
    tm.assert_frame_equal(result, expected)
else:
    tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_numba.py:265 | Complexity: Intermediate | Last updated: 2026-06-02*