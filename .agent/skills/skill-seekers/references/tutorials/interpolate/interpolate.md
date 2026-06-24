# How To: Interpolate

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test interpolate

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: datetime_series
```

## Step-by-Step Guide

### Step 1: Assign ts = Series(...)

```python
ts = Series(np.arange(len(datetime_series), dtype=float), datetime_series.index)
```

### Step 2: Assign ts_copy = ts.copy(...)

```python
ts_copy = ts.copy()
```

### Step 3: Assign unknown = value

```python
ts_copy[5:10] = np.nan
```

### Step 4: Assign linear_interp = ts_copy.interpolate(...)

```python
linear_interp = ts_copy.interpolate(method='linear')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(linear_interp, ts)
```

### Step 6: Assign ord_ts = Series.astype(...)

```python
ord_ts = Series([d.toordinal() for d in datetime_series.index], index=datetime_series.index).astype(float)
```

### Step 7: Assign ord_ts_copy = ord_ts.copy(...)

```python
ord_ts_copy = ord_ts.copy()
```

### Step 8: Assign unknown = value

```python
ord_ts_copy[5:10] = np.nan
```

### Step 9: Assign time_interp = ord_ts_copy.interpolate(...)

```python
time_interp = ord_ts_copy.interpolate(method='time')
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(time_interp, ord_ts)
```


## Complete Example

```python
# Setup
# Fixtures: datetime_series

# Workflow
ts = Series(np.arange(len(datetime_series), dtype=float), datetime_series.index)
ts_copy = ts.copy()
ts_copy[5:10] = np.nan
linear_interp = ts_copy.interpolate(method='linear')
tm.assert_series_equal(linear_interp, ts)
ord_ts = Series([d.toordinal() for d in datetime_series.index], index=datetime_series.index).astype(float)
ord_ts_copy = ord_ts.copy()
ord_ts_copy[5:10] = np.nan
time_interp = ord_ts_copy.interpolate(method='time')
tm.assert_series_equal(time_interp, ord_ts)
```

## Next Steps


---

*Source: test_interpolate.py:93 | Complexity: Advanced | Last updated: 2026-06-02*