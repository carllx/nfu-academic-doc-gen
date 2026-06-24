# How To: Closed Fixed

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test closed fixed

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.api.indexers`
- `pandas.core.indexers.objects`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: closed, arithmetic_win_operators
```

## Step-by-Step Guide

### Step 1: Assign func_name = arithmetic_win_operators

```python
func_name = arithmetic_win_operators
```

### Step 2: Assign df_fixed = DataFrame(...)

```python
df_fixed = DataFrame({'A': [0, 1, 2, 3, 4]})
```

### Step 3: Assign df_time = DataFrame(...)

```python
df_time = DataFrame({'A': [0, 1, 2, 3, 4]}, index=date_range('2020', periods=5))
```

### Step 4: Assign result = getattr(...)

```python
result = getattr(df_fixed.rolling(2, closed=closed, min_periods=1), func_name)()
```

### Step 5: Assign expected = getattr.reset_index(...)

```python
expected = getattr(df_time.rolling('2D', closed=closed, min_periods=1), func_name)().reset_index(drop=True)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: closed, arithmetic_win_operators

# Workflow
func_name = arithmetic_win_operators
df_fixed = DataFrame({'A': [0, 1, 2, 3, 4]})
df_time = DataFrame({'A': [0, 1, 2, 3, 4]}, index=date_range('2020', periods=5))
result = getattr(df_fixed.rolling(2, closed=closed, min_periods=1), func_name)()
expected = getattr(df_time.rolling('2D', closed=closed, min_periods=1), func_name)().reset_index(drop=True)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_rolling.py:154 | Complexity: Intermediate | Last updated: 2026-06-02*