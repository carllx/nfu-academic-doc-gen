# How To: Min Max Reduce

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test min max reduce

## Prerequisites

**Required Modules:**
- `re`
- `sys`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.api.types`


## Step-by-Step Guide

### Step 1: Assign cat = Categorical(...)

```python
cat = Categorical(['a', 'b', 'c', 'd'], ordered=True)
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame(cat)
```

### Step 3: Assign result_max = df.agg(...)

```python
result_max = df.agg('max')
```

### Step 4: Assign expected_max = Series(...)

```python
expected_max = Series(Categorical(['d'], dtype=cat.dtype))
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result_max, expected_max)
```

### Step 6: Assign result_min = df.agg(...)

```python
result_min = df.agg('min')
```

### Step 7: Assign expected_min = Series(...)

```python
expected_min = Series(Categorical(['a'], dtype=cat.dtype))
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result_min, expected_min)
```


## Complete Example

```python
# Workflow
cat = Categorical(['a', 'b', 'c', 'd'], ordered=True)
df = DataFrame(cat)
result_max = df.agg('max')
expected_max = Series(Categorical(['d'], dtype=cat.dtype))
tm.assert_series_equal(result_max, expected_max)
result_min = df.agg('min')
expected_min = Series(Categorical(['a'], dtype=cat.dtype))
tm.assert_series_equal(result_min, expected_min)
```

## Next Steps


---

*Source: test_analytics.py:60 | Complexity: Advanced | Last updated: 2026-06-02*