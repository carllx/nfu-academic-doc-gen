# How To: Closed Empty

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test closed empty

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

### Step 2: Assign ser = Series(...)

```python
ser = Series(data=np.arange(5), index=date_range('2000', periods=5, freq='2D'))
```

### Step 3: Assign roll = ser.rolling(...)

```python
roll = ser.rolling('1D', closed=closed)
```

### Step 4: Assign result = getattr(...)

```python
result = getattr(roll, func_name)()
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([np.nan] * 5, index=ser.index)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: closed, arithmetic_win_operators

# Workflow
func_name = arithmetic_win_operators
ser = Series(data=np.arange(5), index=date_range('2000', periods=5, freq='2D'))
roll = ser.rolling('1D', closed=closed)
result = getattr(roll, func_name)()
expected = Series([np.nan] * 5, index=ser.index)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_rolling.py:418 | Complexity: Intermediate | Last updated: 2026-06-02*