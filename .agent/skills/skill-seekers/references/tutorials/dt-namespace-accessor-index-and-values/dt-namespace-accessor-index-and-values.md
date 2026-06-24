# How To: Dt Namespace Accessor Index And Values

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test dt namespace accessor index and values

## Prerequisites

**Required Modules:**
- `calendar`
- `datetime`
- `locale`
- `unicodedata`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs.timezones`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.indexes.accessors`


## Step-by-Step Guide

### Step 1: Assign index = date_range(...)

```python
index = date_range('20130101', periods=3, freq='D')
```

### Step 2: Assign dti = date_range(...)

```python
dti = date_range('20140204', periods=3, freq='s')
```

### Step 3: Assign ser = Series(...)

```python
ser = Series(dti, index=index, name='xxx')
```

### Step 4: Assign exp = Series(...)

```python
exp = Series(np.array([2014, 2014, 2014], dtype='int32'), index=index, name='xxx')
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser.dt.year, exp)
```

### Step 6: Assign exp = Series(...)

```python
exp = Series(np.array([2, 2, 2], dtype='int32'), index=index, name='xxx')
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser.dt.month, exp)
```

### Step 8: Assign exp = Series(...)

```python
exp = Series(np.array([0, 1, 2], dtype='int32'), index=index, name='xxx')
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser.dt.second, exp)
```

### Step 10: Assign exp = Series(...)

```python
exp = Series([ser.iloc[0]] * 3, index=index, name='xxx')
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser.dt.normalize(), exp)
```


## Complete Example

```python
# Workflow
index = date_range('20130101', periods=3, freq='D')
dti = date_range('20140204', periods=3, freq='s')
ser = Series(dti, index=index, name='xxx')
exp = Series(np.array([2014, 2014, 2014], dtype='int32'), index=index, name='xxx')
tm.assert_series_equal(ser.dt.year, exp)
exp = Series(np.array([2, 2, 2], dtype='int32'), index=index, name='xxx')
tm.assert_series_equal(ser.dt.month, exp)
exp = Series(np.array([0, 1, 2], dtype='int32'), index=index, name='xxx')
tm.assert_series_equal(ser.dt.second, exp)
exp = Series([ser.iloc[0]] * 3, index=index, name='xxx')
tm.assert_series_equal(ser.dt.normalize(), exp)
```

## Next Steps


---

*Source: test_dt_accessor.py:231 | Complexity: Advanced | Last updated: 2026-06-02*