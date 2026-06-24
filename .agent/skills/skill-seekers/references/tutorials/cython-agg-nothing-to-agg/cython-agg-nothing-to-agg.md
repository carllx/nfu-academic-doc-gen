# How To: Cython Agg Nothing To Agg

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test cython agg nothing to agg

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
frame = DataFrame({'a': np.random.default_rng(2).integers(0, 5, 50), 'b': ['foo', 'bar'] * 25})
```

### Step 2: Assign msg = 'Cannot use numeric_only=True with SeriesGroupBy.mean and non-numeric dtypes'

```python
msg = 'Cannot use numeric_only=True with SeriesGroupBy.mean and non-numeric dtypes'
```

### Step 3: Assign frame = DataFrame(...)

```python
frame = DataFrame({'a': np.random.default_rng(2).integers(0, 5, 50), 'b': ['foo', 'bar'] * 25})
```

### Step 4: Assign result = unknown.groupby.mean(...)

```python
result = frame[['b']].groupby(frame['a']).mean(numeric_only=True)
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame([], index=frame['a'].sort_values().drop_duplicates(), columns=Index([], dtype='str'))
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Call unknown.mean()

```python
frame.groupby('a')['b'].mean(numeric_only=True)
```


## Complete Example

```python
# Workflow
frame = DataFrame({'a': np.random.default_rng(2).integers(0, 5, 50), 'b': ['foo', 'bar'] * 25})
msg = 'Cannot use numeric_only=True with SeriesGroupBy.mean and non-numeric dtypes'
with pytest.raises(TypeError, match=msg):
    frame.groupby('a')['b'].mean(numeric_only=True)
frame = DataFrame({'a': np.random.default_rng(2).integers(0, 5, 50), 'b': ['foo', 'bar'] * 25})
result = frame[['b']].groupby(frame['a']).mean(numeric_only=True)
expected = DataFrame([], index=frame['a'].sort_values().drop_duplicates(), columns=Index([], dtype='str'))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_cython.py:96 | Complexity: Intermediate | Last updated: 2026-06-02*