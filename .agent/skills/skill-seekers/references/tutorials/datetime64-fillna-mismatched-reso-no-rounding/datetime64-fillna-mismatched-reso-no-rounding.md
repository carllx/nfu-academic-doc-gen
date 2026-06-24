# How To: Datetime64 Fillna Mismatched Reso No Rounding

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test datetime64 fillna mismatched reso no rounding

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`

**Setup Required:**
```python
# Fixtures: tz, scalar
```

## Step-by-Step Guide

### Step 1: Assign dti = date_range(...)

```python
dti = date_range('2016-01-01', periods=3, unit='s', tz=tz)
```

### Step 2: Assign item = Timestamp(...)

```python
item = Timestamp('2016-02-03 04:05:06.789', tz=tz)
```

### Step 3: Assign vec = date_range(...)

```python
vec = date_range(item, periods=3, unit='ms')
```

### Step 4: Assign exp_dtype = value

```python
exp_dtype = 'M8[ms]' if tz is None else 'M8[ms, UTC]'
```

### Step 5: Assign expected = Series(...)

```python
expected = Series([item, dti[1], dti[2]], dtype=exp_dtype)
```

### Step 6: Assign ser = Series(...)

```python
ser = Series(dti)
```

### Step 7: Assign unknown = NaT

```python
ser[0] = NaT
```

### Step 8: Assign ser2 = ser.copy(...)

```python
ser2 = ser.copy()
```

### Step 9: Assign res = ser.fillna(...)

```python
res = ser.fillna(item)
```

### Step 10: Assign res2 = ser2.fillna(...)

```python
res2 = ser2.fillna(Series(vec))
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```

### Step 12: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res2, expected)
```


## Complete Example

```python
# Setup
# Fixtures: tz, scalar

# Workflow
dti = date_range('2016-01-01', periods=3, unit='s', tz=tz)
item = Timestamp('2016-02-03 04:05:06.789', tz=tz)
vec = date_range(item, periods=3, unit='ms')
exp_dtype = 'M8[ms]' if tz is None else 'M8[ms, UTC]'
expected = Series([item, dti[1], dti[2]], dtype=exp_dtype)
ser = Series(dti)
ser[0] = NaT
ser2 = ser.copy()
res = ser.fillna(item)
res2 = ser2.fillna(Series(vec))
if scalar:
    tm.assert_series_equal(res, expected)
else:
    tm.assert_series_equal(res2, expected)
```

## Next Steps


---

*Source: test_fillna.py:397 | Complexity: Advanced | Last updated: 2026-06-02*