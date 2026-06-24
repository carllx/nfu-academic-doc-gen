# How To: Quantile Empty Dt64

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test quantile empty dt64

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
ser = Series([], dtype='datetime64[ns]')
```

**Verification:**
```python
assert res is pd.NaT
```

### Step 2: Assign res = ser.quantile(...)

```python
res = ser.quantile(0.5)
```

**Verification:**
```python
assert res is pd.NaT
```

### Step 3: Assign res = ser.quantile(...)

```python
res = ser.quantile([0.5])
```

### Step 4: Assign exp = Series(...)

```python
exp = Series([pd.NaT], index=[0.5], dtype=ser.dtype)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```


## Complete Example

```python
# Workflow
ser = Series([], dtype='datetime64[ns]')
res = ser.quantile(0.5)
assert res is pd.NaT
res = ser.quantile([0.5])
exp = Series([pd.NaT], index=[0.5], dtype=ser.dtype)
tm.assert_series_equal(res, exp)
```

## Next Steps


---

*Source: test_quantile.py:215 | Complexity: Intermediate | Last updated: 2026-06-02*