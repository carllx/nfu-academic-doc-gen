# How To: Ewm Consistency Series Cov Corr

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test ewm consistency series cov corr

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: series_data, adjust, ignore_na, min_periods, bias
```

## Step-by-Step Guide

### Step 1: Assign com = 3.0

```python
com = 3.0
```

### Step 2: Assign var_x_plus_y = unknown.ewm.var(...)

```python
var_x_plus_y = (series_data + series_data).ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).var(bias=bias)
```

### Step 3: Assign var_x = series_data.ewm.var(...)

```python
var_x = series_data.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).var(bias=bias)
```

### Step 4: Assign var_y = series_data.ewm.var(...)

```python
var_y = series_data.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).var(bias=bias)
```

### Step 5: Assign cov_x_y = series_data.ewm.cov(...)

```python
cov_x_y = series_data.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).cov(series_data, bias=bias)
```

### Step 6: Call tm.assert_equal()

```python
tm.assert_equal(cov_x_y, 0.5 * (var_x_plus_y - var_x - var_y))
```

### Step 7: Assign corr_x_y = series_data.ewm.corr(...)

```python
corr_x_y = series_data.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).corr(series_data)
```

### Step 8: Assign std_x = series_data.ewm.std(...)

```python
std_x = series_data.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).std(bias=bias)
```

### Step 9: Assign std_y = series_data.ewm.std(...)

```python
std_y = series_data.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).std(bias=bias)
```

### Step 10: Call tm.assert_equal()

```python
tm.assert_equal(corr_x_y, cov_x_y / (std_x * std_y))
```

### Step 11: Assign mean_x = series_data.ewm.mean(...)

```python
mean_x = series_data.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).mean()
```

### Step 12: Assign mean_y = series_data.ewm.mean(...)

```python
mean_y = series_data.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).mean()
```

### Step 13: Assign mean_x_times_y = unknown.ewm.mean(...)

```python
mean_x_times_y = (series_data * series_data).ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).mean()
```

### Step 14: Call tm.assert_equal()

```python
tm.assert_equal(cov_x_y, mean_x_times_y - mean_x * mean_y)
```


## Complete Example

```python
# Setup
# Fixtures: series_data, adjust, ignore_na, min_periods, bias

# Workflow
com = 3.0
var_x_plus_y = (series_data + series_data).ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).var(bias=bias)
var_x = series_data.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).var(bias=bias)
var_y = series_data.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).var(bias=bias)
cov_x_y = series_data.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).cov(series_data, bias=bias)
tm.assert_equal(cov_x_y, 0.5 * (var_x_plus_y - var_x - var_y))
corr_x_y = series_data.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).corr(series_data)
std_x = series_data.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).std(bias=bias)
std_y = series_data.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).std(bias=bias)
tm.assert_equal(corr_x_y, cov_x_y / (std_x * std_y))
if bias:
    mean_x = series_data.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).mean()
    mean_y = series_data.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).mean()
    mean_x_times_y = (series_data * series_data).ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).mean()
    tm.assert_equal(cov_x_y, mean_x_times_y - mean_x * mean_y)
```

## Next Steps


---

*Source: test_moments_consistency_ewm.py:193 | Complexity: Advanced | Last updated: 2026-06-02*