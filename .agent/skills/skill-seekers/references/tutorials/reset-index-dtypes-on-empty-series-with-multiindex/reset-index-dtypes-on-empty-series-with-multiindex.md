# How To: Reset Index Dtypes On Empty Series With Multiindex

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test reset index dtypes on empty series with multiindex

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
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
result = Series(dtype=object, index=idx)[:0].reset_index().dtypes
```

### Step 3: Assign exp = value

```python
exp = 'str' if using_infer_string else object
```

### Step 4: Assign expected = Series(...)

```python
expected = Series({'level_0': np.int64, 'level_1': np.float64, 'level_2': exp if dtype == object else dtype, 0: object})
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: array, dtype, using_infer_string

# Workflow
idx = MultiIndex.from_product([[0, 1], [0.5, 1.0], array])
result = Series(dtype=object, index=idx)[:0].reset_index().dtypes
exp = 'str' if using_infer_string else object
expected = Series({'level_0': np.int64, 'level_1': np.float64, 'level_2': exp if dtype == object else dtype, 0: object})
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_reset_index.py:190 | Complexity: Intermediate | Last updated: 2026-06-02*