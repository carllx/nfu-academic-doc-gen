# How To: Replace Nat With Tz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test replace nat with tz

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign ts = pd.Timestamp(...)

```python
ts = pd.Timestamp('2015/01/01', tz='UTC')
```

### Step 2: Assign s = pd.Series(...)

```python
s = pd.Series([pd.NaT, pd.Timestamp('2015/01/01', tz='UTC')])
```

### Step 3: Assign result = s.replace(...)

```python
result = s.replace([np.nan, pd.NaT], pd.Timestamp.min)
```

### Step 4: Assign expected = pd.Series(...)

```python
expected = pd.Series([pd.Timestamp.min, ts], dtype=object)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(expected, result)
```


## Complete Example

```python
# Workflow
ts = pd.Timestamp('2015/01/01', tz='UTC')
s = pd.Series([pd.NaT, pd.Timestamp('2015/01/01', tz='UTC')])
result = s.replace([np.nan, pd.NaT], pd.Timestamp.min)
expected = pd.Series([pd.Timestamp.min, ts], dtype=object)
tm.assert_series_equal(expected, result)
```

## Next Steps


---

*Source: test_replace.py:167 | Complexity: Intermediate | Last updated: 2026-06-02*