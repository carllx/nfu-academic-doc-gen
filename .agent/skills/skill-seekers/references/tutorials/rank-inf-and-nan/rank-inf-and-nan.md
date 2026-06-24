# How To: Rank Inf And Nan

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test rank inf and nan

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas._libs.algos`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: contents, dtype, frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign dtype_na_map = value

```python
dtype_na_map = {'float64': np.nan, 'float32': np.nan, 'object': None, 'datetime64': np.datetime64('nat')}
```

### Step 2: Assign values = np.array(...)

```python
values = np.array(contents, dtype=dtype)
```

### Step 3: Assign exp_order = value

```python
exp_order = np.array(range(len(values)), dtype='float64') + 1.0
```

### Step 4: Assign random_order = np.random.default_rng.permutation(...)

```python
random_order = np.random.default_rng(2).permutation(len(values))
```

### Step 5: Assign obj = frame_or_series(...)

```python
obj = frame_or_series(values[random_order])
```

### Step 6: Assign expected = frame_or_series(...)

```python
expected = frame_or_series(exp_order[random_order], dtype='float64')
```

### Step 7: Assign result = obj.rank(...)

```python
result = obj.rank()
```

### Step 8: Call tm.assert_equal()

```python
tm.assert_equal(result, expected)
```

### Step 9: Assign na_value = value

```python
na_value = dtype_na_map[dtype]
```

### Step 10: Assign nan_indices = np.random.default_rng.choice(...)

```python
nan_indices = np.random.default_rng(2).choice(range(len(values)), 5)
```

### Step 11: Assign values = np.insert(...)

```python
values = np.insert(values, nan_indices, na_value)
```

### Step 12: Assign exp_order = np.insert(...)

```python
exp_order = np.insert(exp_order, nan_indices, np.nan)
```


## Complete Example

```python
# Setup
# Fixtures: contents, dtype, frame_or_series

# Workflow
dtype_na_map = {'float64': np.nan, 'float32': np.nan, 'object': None, 'datetime64': np.datetime64('nat')}
values = np.array(contents, dtype=dtype)
exp_order = np.array(range(len(values)), dtype='float64') + 1.0
if dtype in dtype_na_map:
    na_value = dtype_na_map[dtype]
    nan_indices = np.random.default_rng(2).choice(range(len(values)), 5)
    values = np.insert(values, nan_indices, na_value)
    exp_order = np.insert(exp_order, nan_indices, np.nan)
random_order = np.random.default_rng(2).permutation(len(values))
obj = frame_or_series(values[random_order])
expected = frame_or_series(exp_order[random_order], dtype='float64')
result = obj.rank()
tm.assert_equal(result, expected)
```

## Next Steps


---

*Source: test_rank.py:393 | Complexity: Advanced | Last updated: 2026-06-02*