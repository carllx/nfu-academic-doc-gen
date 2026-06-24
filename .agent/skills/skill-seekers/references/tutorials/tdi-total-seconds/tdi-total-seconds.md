# How To: Tdi Total Seconds

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tdi total seconds

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas._libs.tslibs.offsets`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign rng = timedelta_range(...)

```python
rng = timedelta_range('1 days, 10:11:12.100123456', periods=2, freq='s')
```

### Step 2: Assign expt = value

```python
expt = [1 * 86400 + 10 * 3600 + 11 * 60 + 12 + 100123456.0 / 1000000000.0, 1 * 86400 + 10 * 3600 + 11 * 60 + 13 + 100123456.0 / 1000000000.0]
```

### Step 3: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(rng.total_seconds(), Index(expt))
```

### Step 4: Assign ser = Series(...)

```python
ser = Series(rng)
```

### Step 5: Assign s_expt = Series(...)

```python
s_expt = Series(expt, index=[0, 1])
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser.dt.total_seconds(), s_expt)
```

### Step 7: Assign unknown = value

```python
ser[1] = np.nan
```

### Step 8: Assign s_expt = Series(...)

```python
s_expt = Series([1 * 86400 + 10 * 3600 + 11 * 60 + 12 + 100123456.0 / 1000000000.0, np.nan], index=[0, 1])
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser.dt.total_seconds(), s_expt)
```


## Complete Example

```python
# Workflow
rng = timedelta_range('1 days, 10:11:12.100123456', periods=2, freq='s')
expt = [1 * 86400 + 10 * 3600 + 11 * 60 + 12 + 100123456.0 / 1000000000.0, 1 * 86400 + 10 * 3600 + 11 * 60 + 13 + 100123456.0 / 1000000000.0]
tm.assert_almost_equal(rng.total_seconds(), Index(expt))
ser = Series(rng)
s_expt = Series(expt, index=[0, 1])
tm.assert_series_equal(ser.dt.total_seconds(), s_expt)
ser[1] = np.nan
s_expt = Series([1 * 86400 + 10 * 3600 + 11 * 60 + 12 + 100123456.0 / 1000000000.0, np.nan], index=[0, 1])
tm.assert_series_equal(ser.dt.total_seconds(), s_expt)
```

## Next Steps


---

*Source: test_scalar_compat.py:21 | Complexity: Advanced | Last updated: 2026-06-02*