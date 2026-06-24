# How To: Qcut Return Intervals

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test qcut return intervals

## Prerequisites

**Required Modules:**
- `os`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.tseries.offsets`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([0, 1, 2, 3, 4, 5, 6, 7, 8])
```

### Step 2: Assign res = qcut(...)

```python
res = qcut(ser, [0, 0.333, 0.666, 1])
```

### Step 3: Assign exp_levels = np.array(...)

```python
exp_levels = np.array([Interval(-0.001, 2.664), Interval(2.664, 5.328), Interval(5.328, 8)])
```

### Step 4: Assign exp = Series.astype(...)

```python
exp = Series(exp_levels.take([0, 0, 0, 1, 1, 1, 2, 2, 2])).astype(CategoricalDtype(ordered=True))
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```


## Complete Example

```python
# Workflow
ser = Series([0, 1, 2, 3, 4, 5, 6, 7, 8])
res = qcut(ser, [0, 0.333, 0.666, 1])
exp_levels = np.array([Interval(-0.001, 2.664), Interval(2.664, 5.328), Interval(5.328, 8)])
exp = Series(exp_levels.take([0, 0, 0, 1, 1, 1, 2, 2, 2])).astype(CategoricalDtype(ordered=True))
tm.assert_series_equal(res, exp)
```

## Next Steps


---

*Source: test_qcut.py:123 | Complexity: Intermediate | Last updated: 2026-06-02*