# How To: Cummin Cummax Datetimelike

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test cummin cummax datetimelike

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: ts, method, skipna, exp_tdi
```

## Step-by-Step Guide

### Step 1: Assign tdi = pd.to_timedelta(...)

```python
tdi = pd.to_timedelta(['NaT', '2 days', 'NaT', '1 days', 'NaT', '3 days'])
```

### Step 2: Assign ser = pd.Series(...)

```python
ser = pd.Series(tdi + ts)
```

### Step 3: Assign exp_tdi = pd.to_timedelta(...)

```python
exp_tdi = pd.to_timedelta(exp_tdi)
```

### Step 4: Assign expected = pd.Series(...)

```python
expected = pd.Series(exp_tdi + ts)
```

### Step 5: Assign result = getattr(...)

```python
result = getattr(ser, method)(skipna=skipna)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, result)
```


## Complete Example

```python
# Setup
# Fixtures: ts, method, skipna, exp_tdi

# Workflow
tdi = pd.to_timedelta(['NaT', '2 days', 'NaT', '1 days', 'NaT', '3 days'])
ser = pd.Series(tdi + ts)
exp_tdi = pd.to_timedelta(exp_tdi)
expected = pd.Series(exp_tdi + ts)
result = getattr(ser, method)(skipna=skipna)
tm.assert_series_equal(expected, result)
```

## Next Steps


---

*Source: test_cumulative.py:84 | Complexity: Intermediate | Last updated: 2026-06-02*