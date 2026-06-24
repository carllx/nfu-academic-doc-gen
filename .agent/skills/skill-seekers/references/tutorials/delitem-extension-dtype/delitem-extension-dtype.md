# How To: Delitem Extension Dtype

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test delitem extension dtype

## Prerequisites

**Required Modules:**
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2016-01-01', periods=3, tz='US/Pacific')
```

**Verification:**
```python
assert ser.dtype == dti.dtype
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(dti)
```

**Verification:**
```python
assert ser.dtype == pi.dtype
```

### Step 3: Assign expected = value

```python
expected = ser[[0, 2]]
```

**Verification:**
```python
assert ser.dtype == dti.dtype
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, expected)
```

### Step 5: Assign pi = dti.tz_localize.to_period(...)

```python
pi = dti.tz_localize(None).to_period('D')
```

### Step 6: Assign ser = Series(...)

```python
ser = Series(pi)
```

### Step 7: Assign expected = value

```python
expected = ser[:2]
```

**Verification:**
```python
assert ser.dtype == pi.dtype
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser, expected)
```


## Complete Example

```python
# Workflow
dti = date_range('2016-01-01', periods=3, tz='US/Pacific')
ser = Series(dti)
expected = ser[[0, 2]]
del ser[1]
assert ser.dtype == dti.dtype
tm.assert_series_equal(ser, expected)
pi = dti.tz_localize(None).to_period('D')
ser = Series(pi)
expected = ser[:2]
del ser[2]
assert ser.dtype == pi.dtype
tm.assert_series_equal(ser, expected)
```

## Next Steps


---

*Source: test_delitem.py:51 | Complexity: Advanced | Last updated: 2026-06-02*