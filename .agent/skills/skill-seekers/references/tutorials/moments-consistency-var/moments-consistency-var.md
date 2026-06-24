# How To: Moments Consistency Var

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test moments consistency var

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: all_data, adjust, ignore_na, min_periods, bias
```

## Step-by-Step Guide

### Step 1: Assign com = 3.0

```python
com = 3.0
```

**Verification:**
```python
assert not (var_x < 0).any().any()
```

### Step 2: Assign mean_x = all_data.ewm.mean(...)

```python
mean_x = all_data.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).mean()
```

### Step 3: Assign var_x = all_data.ewm.var(...)

```python
var_x = all_data.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).var(bias=bias)
```

**Verification:**
```python
assert not (var_x < 0).any().any()
```

### Step 4: Assign mean_x2 = unknown.ewm.mean(...)

```python
mean_x2 = (all_data * all_data).ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).mean()
```

### Step 5: Call tm.assert_equal()

```python
tm.assert_equal(var_x, mean_x2 - mean_x * mean_x)
```


## Complete Example

```python
# Setup
# Fixtures: all_data, adjust, ignore_na, min_periods, bias

# Workflow
com = 3.0
mean_x = all_data.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).mean()
var_x = all_data.ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).var(bias=bias)
assert not (var_x < 0).any().any()
if bias:
    mean_x2 = (all_data * all_data).ewm(com=com, min_periods=min_periods, adjust=adjust, ignore_na=ignore_na).mean()
    tm.assert_equal(var_x, mean_x2 - mean_x * mean_x)
```

## Next Steps


---

*Source: test_moments_consistency_ewm.py:127 | Complexity: Intermediate | Last updated: 2026-06-02*