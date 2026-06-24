# How To: Quantile Empty Float64

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test quantile empty float64

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.datetimes`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([], dtype='float64')
```

**Verification:**
```python
assert np.isnan(res)
```

### Step 2: Assign res = ser.quantile(...)

```python
res = ser.quantile(0.5)
```

**Verification:**
```python
assert np.isnan(res)
```

### Step 3: Assign res = ser.quantile(...)

```python
res = ser.quantile([0.5])
```

### Step 4: Assign exp = Series(...)

```python
exp = Series([np.nan], index=[0.5])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```


## Complete Example

```python
# Workflow
ser = Series([], dtype='float64')
res = ser.quantile(0.5)
assert np.isnan(res)
res = ser.quantile([0.5])
exp = Series([np.nan], index=[0.5])
tm.assert_series_equal(res, exp)
```

## Next Steps


---

*Source: test_quantile.py:193 | Complexity: Intermediate | Last updated: 2026-06-02*