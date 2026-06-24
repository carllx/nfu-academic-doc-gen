# How To: Rank Tie Methods On Infs Nans

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test rank tie methods on infs nans

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `itertools`
- `operator`
- `numpy`
- `pytest`
- `pandas._libs.algos`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.api.types`

**Setup Required:**
```python
# Fixtures: method, na_option, ascending, dtype, na_value, pos_inf, neg_inf
```

## Step-by-Step Guide

### Step 1: Call pytest.importorskip()

```python
pytest.importorskip('scipy')
```

### Step 2: Assign chunk = 3

```python
chunk = 3
```

### Step 3: Assign in_arr = value

```python
in_arr = [neg_inf] * chunk + [na_value] * chunk + [pos_inf] * chunk
```

### Step 4: Assign iseries = Series(...)

```python
iseries = Series(in_arr, dtype=dtype)
```

### Step 5: Assign exp_ranks = value

```python
exp_ranks = {'average': ([2, 2, 2], [5, 5, 5], [8, 8, 8]), 'min': ([1, 1, 1], [4, 4, 4], [7, 7, 7]), 'max': ([3, 3, 3], [6, 6, 6], [9, 9, 9]), 'first': ([1, 2, 3], [4, 5, 6], [7, 8, 9]), 'dense': ([1, 1, 1], [2, 2, 2], [3, 3, 3])}
```

### Step 6: Assign ranks = value

```python
ranks = exp_ranks[method]
```

### Step 7: Assign expected = value

```python
expected = order if ascending else order[::-1]
```

### Step 8: Assign expected = list(...)

```python
expected = list(chain.from_iterable(expected))
```

### Step 9: Assign result = iseries.rank(...)

```python
result = iseries.rank(method=method, na_option=na_option, ascending=ascending)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, Series(expected, dtype=exp_dtype))
```

### Step 11: Assign exp_dtype = 'float64'

```python
exp_dtype = 'float64'
```

### Step 12: Assign order = value

```python
order = [ranks[1], ranks[0], ranks[2]]
```

### Step 13: Assign exp_dtype = 'float64[pyarrow]'

```python
exp_dtype = 'float64[pyarrow]'
```

### Step 14: Assign exp_dtype = 'uint64[pyarrow]'

```python
exp_dtype = 'uint64[pyarrow]'
```

### Step 15: Assign order = value

```python
order = [ranks[0], ranks[2], ranks[1]]
```

### Step 16: Assign order = value

```python
order = [ranks[0], [np.nan] * chunk, ranks[1]]
```


## Complete Example

```python
# Setup
# Fixtures: method, na_option, ascending, dtype, na_value, pos_inf, neg_inf

# Workflow
pytest.importorskip('scipy')
if dtype == 'float64[pyarrow]':
    if method == 'average':
        exp_dtype = 'float64[pyarrow]'
    else:
        exp_dtype = 'uint64[pyarrow]'
else:
    exp_dtype = 'float64'
chunk = 3
in_arr = [neg_inf] * chunk + [na_value] * chunk + [pos_inf] * chunk
iseries = Series(in_arr, dtype=dtype)
exp_ranks = {'average': ([2, 2, 2], [5, 5, 5], [8, 8, 8]), 'min': ([1, 1, 1], [4, 4, 4], [7, 7, 7]), 'max': ([3, 3, 3], [6, 6, 6], [9, 9, 9]), 'first': ([1, 2, 3], [4, 5, 6], [7, 8, 9]), 'dense': ([1, 1, 1], [2, 2, 2], [3, 3, 3])}
ranks = exp_ranks[method]
if na_option == 'top':
    order = [ranks[1], ranks[0], ranks[2]]
elif na_option == 'bottom':
    order = [ranks[0], ranks[2], ranks[1]]
else:
    order = [ranks[0], [np.nan] * chunk, ranks[1]]
expected = order if ascending else order[::-1]
expected = list(chain.from_iterable(expected))
result = iseries.rank(method=method, na_option=na_option, ascending=ascending)
tm.assert_series_equal(result, Series(expected, dtype=exp_dtype))
```

## Next Steps


---

*Source: test_rank.py:293 | Complexity: Advanced | Last updated: 2026-06-02*