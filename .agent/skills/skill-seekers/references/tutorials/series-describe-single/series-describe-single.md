# How To: Series Describe Single

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test series describe single

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign ts = Series(...)

```python
ts = Series(np.arange(10, dtype=np.float64), index=date_range('2020-01-01', periods=10))
```

### Step 2: Assign grouped = ts.groupby(...)

```python
grouped = ts.groupby(lambda x: x.month)
```

### Step 3: Assign result = grouped.apply(...)

```python
result = grouped.apply(lambda x: x.describe())
```

### Step 4: Assign expected = grouped.describe.stack(...)

```python
expected = grouped.describe().stack(future_stack=True)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
ts = Series(np.arange(10, dtype=np.float64), index=date_range('2020-01-01', periods=10))
grouped = ts.groupby(lambda x: x.month)
result = grouped.apply(lambda x: x.describe())
expected = grouped.describe().stack(future_stack=True)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_describe.py:32 | Complexity: Intermediate | Last updated: 2026-06-02*