# How To: Reset Index Dtypes On Empty Frame With Multiindex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test reset index dtypes on empty frame with multiindex

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `itertools`
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: array, dtype, using_infer_string
```

## Step-by-Step Guide

### Step 1: Assign idx = MultiIndex.from_product(...)

```python
idx = MultiIndex.from_product([[0, 1], [0.5, 1.0], array])
```

### Step 2: Assign result = value

```python
result = DataFrame(index=idx)[:0].reset_index().dtypes
```

### Step 3: Assign expected = Series(...)

```python
expected = Series({'level_0': np.int64, 'level_1': np.float64, 'level_2': dtype})
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign dtype = pd.StringDtype(...)

```python
dtype = pd.StringDtype(na_value=np.nan)
```


## Complete Example

```python
# Setup
# Fixtures: array, dtype, using_infer_string

# Workflow
idx = MultiIndex.from_product([[0, 1], [0.5, 1.0], array])
result = DataFrame(index=idx)[:0].reset_index().dtypes
if using_infer_string and dtype == object:
    dtype = pd.StringDtype(na_value=np.nan)
expected = Series({'level_0': np.int64, 'level_1': np.float64, 'level_2': dtype})
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_reset_index.py:657 | Complexity: Intermediate | Last updated: 2026-06-02*