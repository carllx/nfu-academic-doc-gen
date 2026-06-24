# How To: Datetimelike Centered Selections

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test datetimelike centered selections

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
# Fixtures: closed, window_selections, arithmetic_win_operators
```

## Step-by-Step Guide

### Step 1: Assign func_name = arithmetic_win_operators

```python
func_name = arithmetic_win_operators
```

### Step 2: Assign df_time = DataFrame(...)

```python
df_time = DataFrame({'A': [0.0, 1.0, 2.0, 3.0, 4.0]}, index=date_range('2020', periods=5))
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'A': [getattr(df_time['A'].iloc[s], func_name)() for s in window_selections]}, index=date_range('2020', periods=5))
```

### Step 4: Assign result = getattr(...)

```python
result = getattr(df_time.rolling('2D', closed=closed, min_periods=1, center=True), func_name)(**kwargs)
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected, check_dtype=False)
```

### Step 6: Assign kwargs = value

```python
kwargs = {'ddof': 0}
```

### Step 7: Assign kwargs = value

```python
kwargs = {}
```


## Complete Example

```python
# Setup
# Fixtures: closed, window_selections, arithmetic_win_operators

# Workflow
func_name = arithmetic_win_operators
df_time = DataFrame({'A': [0.0, 1.0, 2.0, 3.0, 4.0]}, index=date_range('2020', periods=5))
expected = DataFrame({'A': [getattr(df_time['A'].iloc[s], func_name)() for s in window_selections]}, index=date_range('2020', periods=5))
if func_name == 'sem':
    kwargs = {'ddof': 0}
else:
    kwargs = {}
result = getattr(df_time.rolling('2D', closed=closed, min_periods=1, center=True), func_name)(**kwargs)
tm.assert_frame_equal(result, expected, check_dtype=False)
```

## Next Steps


---

*Source: test_rolling.py:217 | Complexity: Intermediate | Last updated: 2026-06-02*