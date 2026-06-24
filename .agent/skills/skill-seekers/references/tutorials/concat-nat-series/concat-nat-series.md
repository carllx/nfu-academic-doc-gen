# How To: Concat Nat Series

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat NaT series

## Prerequisites

**Required Modules:**
- `datetime`
- `datetime`
- `dateutil`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign x = Series(...)

```python
x = Series(date_range('20151124 08:00', '20151124 09:00', freq='1h', tz='US/Eastern'))
```

### Step 2: Assign y = Series(...)

```python
y = Series(pd.NaT, index=[0, 1], dtype='datetime64[ns, US/Eastern]')
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([x[0], x[1], pd.NaT, pd.NaT])
```

### Step 4: Assign result = concat(...)

```python
result = concat([x, y], ignore_index=True)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign expected = Series(...)

```python
expected = Series(pd.NaT, index=range(4), dtype='datetime64[ns, US/Eastern]')
```

### Step 7: Assign result = concat(...)

```python
result = concat([y, y], ignore_index=True)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
x = Series(date_range('20151124 08:00', '20151124 09:00', freq='1h', tz='US/Eastern'))
y = Series(pd.NaT, index=[0, 1], dtype='datetime64[ns, US/Eastern]')
expected = Series([x[0], x[1], pd.NaT, pd.NaT])
result = concat([x, y], ignore_index=True)
tm.assert_series_equal(result, expected)
expected = Series(pd.NaT, index=range(4), dtype='datetime64[ns, US/Eastern]')
result = concat([y, y], ignore_index=True)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_datetimes.py:160 | Complexity: Advanced | Last updated: 2026-06-02*