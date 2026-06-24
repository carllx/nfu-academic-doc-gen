# How To: Cython Agg Boolean

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cython agg boolean

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.common`


## Step-by-Step Guide

### Step 1: Assign frame = DataFrame(...)

```python
frame = DataFrame({'a': np.random.default_rng(2).integers(0, 5, 50), 'b': np.random.default_rng(2).integers(0, 2, 50).astype('bool')})
```

### Step 2: Assign result = unknown.mean(...)

```python
result = frame.groupby('a')['b'].mean()
```

### Step 3: Assign msg = 'using SeriesGroupBy.mean'

```python
msg = 'using SeriesGroupBy.mean'
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign expected = unknown.agg(...)

```python
expected = frame.groupby('a')['b'].agg(np.mean)
```


## Complete Example

```python
# Workflow
frame = DataFrame({'a': np.random.default_rng(2).integers(0, 5, 50), 'b': np.random.default_rng(2).integers(0, 2, 50).astype('bool')})
result = frame.groupby('a')['b'].mean()
msg = 'using SeriesGroupBy.mean'
with tm.assert_produces_warning(FutureWarning, match=msg):
    expected = frame.groupby('a')['b'].agg(np.mean)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_cython.py:80 | Complexity: Intermediate | Last updated: 2026-06-02*