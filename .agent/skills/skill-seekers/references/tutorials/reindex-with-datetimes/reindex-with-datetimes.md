# How To: Reindex With Datetimes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test reindex with datetimes

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign rng = date_range(...)

```python
rng = date_range('1/1/2000', periods=20)
```

### Step 2: Assign ts = Series(...)

```python
ts = Series(np.random.default_rng(2).standard_normal(20), index=rng)
```

### Step 3: Assign result = ts.reindex(...)

```python
result = ts.reindex(list(ts.index[5:10]))
```

### Step 4: Assign expected = value

```python
expected = ts[5:10]
```

### Step 5: Assign expected.index = expected.index._with_freq(...)

```python
expected.index = expected.index._with_freq(None)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign result = value

```python
result = ts[list(ts.index[5:10])]
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
rng = date_range('1/1/2000', periods=20)
ts = Series(np.random.default_rng(2).standard_normal(20), index=rng)
result = ts.reindex(list(ts.index[5:10]))
expected = ts[5:10]
expected.index = expected.index._with_freq(None)
tm.assert_series_equal(result, expected)
result = ts[list(ts.index[5:10])]
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_reindex.py:83 | Complexity: Advanced | Last updated: 2026-06-02*