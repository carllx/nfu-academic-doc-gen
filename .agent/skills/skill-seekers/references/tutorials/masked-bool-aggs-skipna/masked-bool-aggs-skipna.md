# How To: Masked Bool Aggs Skipna

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test masked bool aggs skipna

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `builtins`
- `datetime`
- `string`
- `numpy`
- `pytest`
- `pandas._libs.tslibs`
- `pandas.core.dtypes.common`
- `pandas.core.dtypes.missing`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.groupby`
- `pandas.util`
- `scipy.stats`

**Setup Required:**
```python
# Fixtures: bool_agg_func, dtype, skipna, frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign obj = frame_or_series(...)

```python
obj = frame_or_series([pd.NA, 1], dtype=dtype)
```

### Step 2: Assign expected_res = True

```python
expected_res = True
```

### Step 3: Assign expected = frame_or_series(...)

```python
expected = frame_or_series([expected_res], index=np.array([1]), dtype='boolean')
```

### Step 4: Assign result = obj.groupby.agg(...)

```python
result = obj.groupby([1, 1]).agg(bool_agg_func, skipna=skipna)
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 6: Assign expected_res = value

```python
expected_res = pd.NA
```


## Complete Example

```python
# Setup
# Fixtures: bool_agg_func, dtype, skipna, frame_or_series

# Workflow
obj = frame_or_series([pd.NA, 1], dtype=dtype)
expected_res = True
if not skipna and bool_agg_func == 'all':
    expected_res = pd.NA
expected = frame_or_series([expected_res], index=np.array([1]), dtype='boolean')
result = obj.groupby([1, 1]).agg(bool_agg_func, skipna=skipna)
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_reductions.py:155 | Complexity: Intermediate | Last updated: 2026-06-02*