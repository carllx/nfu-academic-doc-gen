# How To: Concat Nat Series2

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test concat NaT series2

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
x = Series(date_range('20151124 08:00', '20151124 09:00', freq='1h'))
```

### Step 2: Assign y = Series(...)

```python
y = Series(date_range('20151124 10:00', '20151124 11:00', freq='1h'))
```

### Step 3: Assign unknown = value

```python
y[:] = pd.NaT
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([x[0], x[1], pd.NaT, pd.NaT])
```

### Step 5: Assign result = concat(...)

```python
result = concat([x, y], ignore_index=True)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign unknown = value

```python
x[:] = pd.NaT
```

### Step 8: Assign expected = Series(...)

```python
expected = Series(pd.NaT, index=range(4), dtype='datetime64[ns]')
```

### Step 9: Assign result = concat(...)

```python
result = concat([x, y], ignore_index=True)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
x = Series(date_range('20151124 08:00', '20151124 09:00', freq='1h'))
y = Series(date_range('20151124 10:00', '20151124 11:00', freq='1h'))
y[:] = pd.NaT
expected = Series([x[0], x[1], pd.NaT, pd.NaT])
result = concat([x, y], ignore_index=True)
tm.assert_series_equal(result, expected)
x[:] = pd.NaT
expected = Series(pd.NaT, index=range(4), dtype='datetime64[ns]')
result = concat([x, y], ignore_index=True)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_datetimes.py:177 | Complexity: Advanced | Last updated: 2026-06-02*