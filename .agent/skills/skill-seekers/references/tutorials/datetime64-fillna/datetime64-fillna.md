# How To: Datetime64 Fillna

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test datetime64 fillna

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([Timestamp('20130101'), Timestamp('20130101'), Timestamp('20130102'), Timestamp('20130103 9:01:01')])
```

### Step 2: Assign unknown = value

```python
ser[2] = np.nan
```

### Step 3: Assign result = ser.ffill(...)

```python
result = ser.ffill()
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([Timestamp('20130101'), Timestamp('20130101'), Timestamp('20130101'), Timestamp('20130103 9:01:01')])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign result = ser.bfill(...)

```python
result = ser.bfill()
```

### Step 7: Assign expected = Series(...)

```python
expected = Series([Timestamp('20130101'), Timestamp('20130101'), Timestamp('20130103 9:01:01'), Timestamp('20130103 9:01:01')])
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
ser = Series([Timestamp('20130101'), Timestamp('20130101'), Timestamp('20130102'), Timestamp('20130103 9:01:01')])
ser[2] = np.nan
result = ser.ffill()
expected = Series([Timestamp('20130101'), Timestamp('20130101'), Timestamp('20130101'), Timestamp('20130103 9:01:01')])
tm.assert_series_equal(result, expected)
result = ser.bfill()
expected = Series([Timestamp('20130101'), Timestamp('20130101'), Timestamp('20130103 9:01:01'), Timestamp('20130103 9:01:01')])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_fillna.py:349 | Complexity: Advanced | Last updated: 2026-06-02*