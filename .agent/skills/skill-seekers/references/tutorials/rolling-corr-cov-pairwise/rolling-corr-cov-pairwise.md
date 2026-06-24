# How To: Rolling Corr Cov Pairwise

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test rolling corr cov pairwise

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.api.indexers`
- `pandas.core.groupby.groupby`

**Setup Required:**
```python
# Fixtures: f, roll_frame
```

## Step-by-Step Guide

### Step 1: Assign g = roll_frame.groupby(...)

```python
g = roll_frame.groupby('A')
```

### Step 2: Assign r = g.rolling(...)

```python
r = g.rolling(window=4)
```

### Step 3: Assign result = getattr(...)

```python
result = getattr(r.B, f)(pairwise=True)
```

### Step 4: Assign msg = 'DataFrameGroupBy.apply operated on the grouping columns'

```python
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign expected = g.apply(...)

```python
expected = g.apply(func)
```


## Complete Example

```python
# Setup
# Fixtures: f, roll_frame

# Workflow
g = roll_frame.groupby('A')
r = g.rolling(window=4)
result = getattr(r.B, f)(pairwise=True)

def func(x):
    return getattr(x.B.rolling(4), f)(pairwise=True)
msg = 'DataFrameGroupBy.apply operated on the grouping columns'
with tm.assert_produces_warning(FutureWarning, match=msg):
    expected = g.apply(func)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_groupby.py:193 | Complexity: Intermediate | Last updated: 2026-06-02*