# How To: Timedelta64 Fillna Mismatched Reso No Rounding

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test timedelta64 fillna mismatched reso no rounding

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
# Fixtures: scalar
```

## Step-by-Step Guide

### Step 1: Assign tdi = value

```python
tdi = date_range('2016-01-01', periods=3, unit='s') - Timestamp('1970-01-01')
```

### Step 2: Assign item = value

```python
item = Timestamp('2016-02-03 04:05:06.789') - Timestamp('1970-01-01')
```

### Step 3: Assign vec = timedelta_range(...)

```python
vec = timedelta_range(item, periods=3, unit='ms')
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([item, tdi[1], tdi[2]], dtype='m8[ms]')
```

### Step 5: Assign ser = Series(...)

```python
ser = Series(tdi)
```

### Step 6: Assign unknown = NaT

```python
ser[0] = NaT
```

### Step 7: Assign ser2 = ser.copy(...)

```python
ser2 = ser.copy()
```

### Step 8: Assign res = ser.fillna(...)

```python
res = ser.fillna(item)
```

### Step 9: Assign res2 = ser2.fillna(...)

```python
res2 = ser2.fillna(Series(vec))
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, expected)
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res2, expected)
```


## Complete Example

```python
# Setup
# Fixtures: scalar

# Workflow
tdi = date_range('2016-01-01', periods=3, unit='s') - Timestamp('1970-01-01')
item = Timestamp('2016-02-03 04:05:06.789') - Timestamp('1970-01-01')
vec = timedelta_range(item, periods=3, unit='ms')
expected = Series([item, tdi[1], tdi[2]], dtype='m8[ms]')
ser = Series(tdi)
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

*Source: test_fillna.py:430 | Complexity: Advanced | Last updated: 2026-06-02*