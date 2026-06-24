# How To: Combine First Period Datetime

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test combine first period datetime

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign didx = date_range(...)

```python
didx = date_range(start='1950-01-31', end='1950-07-31', freq='ME')
```

### Step 2: Assign pidx = period_range(...)

```python
pidx = period_range(start=Period('1950-1'), end=Period('1950-7'), freq='M')
```

### Step 3: Assign a = Series(...)

```python
a = Series([1, np.nan, np.nan, 4, 5, np.nan, 7], index=idx)
```

### Step 4: Assign b = Series(...)

```python
b = Series([9, 9, 9, 9, 9, 9, 9], index=idx)
```

### Step 5: Assign result = a.combine_first(...)

```python
result = a.combine_first(b)
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([1, 9, 9, 4, 5, 9, 7], index=idx, dtype=np.float64)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
didx = date_range(start='1950-01-31', end='1950-07-31', freq='ME')
pidx = period_range(start=Period('1950-1'), end=Period('1950-7'), freq='M')
for idx in [didx, pidx]:
    a = Series([1, np.nan, np.nan, 4, 5, np.nan, 7], index=idx)
    b = Series([9, 9, 9, 9, 9, 9, 9], index=idx)
    result = a.combine_first(b)
    expected = Series([1, 9, 9, 4, 5, 9, 7], index=idx, dtype=np.float64)
    tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_combine_first.py:17 | Complexity: Intermediate | Last updated: 2026-06-02*