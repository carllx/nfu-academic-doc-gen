# How To: Constructor Timedelta Window And Minperiods

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test constructor timedelta window and minperiods

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
# Fixtures: window, raw
```

## Step-by-Step Guide

### Step 1: Assign n = 10

```python
n = 10
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'value': np.arange(n)}, index=date_range('2017-08-08', periods=n, freq='D'))
```

### Step 3: Assign expected = DataFrame(...)

```python
expected = DataFrame({'value': np.append([np.nan, 1.0], np.arange(3.0, 27.0, 3))}, index=date_range('2017-08-08', periods=n, freq='D'))
```

### Step 4: Assign result_roll_sum = df.rolling.sum(...)

```python
result_roll_sum = df.rolling(window=window, min_periods=2).sum()
```

### Step 5: Assign result_roll_generic = df.rolling.apply(...)

```python
result_roll_generic = df.rolling(window=window, min_periods=2).apply(sum, raw=raw)
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result_roll_sum, expected)
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result_roll_generic, expected)
```


## Complete Example

```python
# Setup
# Fixtures: window, raw

# Workflow
n = 10
df = DataFrame({'value': np.arange(n)}, index=date_range('2017-08-08', periods=n, freq='D'))
expected = DataFrame({'value': np.append([np.nan, 1.0], np.arange(3.0, 27.0, 3))}, index=date_range('2017-08-08', periods=n, freq='D'))
result_roll_sum = df.rolling(window=window, min_periods=2).sum()
result_roll_generic = df.rolling(window=window, min_periods=2).apply(sum, raw=raw)
tm.assert_frame_equal(result_roll_sum, expected)
tm.assert_frame_equal(result_roll_generic, expected)
```

## Next Steps


---

*Source: test_rolling.py:137 | Complexity: Intermediate | Last updated: 2026-06-02*