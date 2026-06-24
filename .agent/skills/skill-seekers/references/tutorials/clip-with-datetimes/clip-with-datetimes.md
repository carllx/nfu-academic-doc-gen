# How To: Clip With Datetimes

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test clip with datetimes

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign t = Timestamp(...)

```python
t = Timestamp('2015-12-01 09:30:30')
```

### Step 2: Assign s = Series(...)

```python
s = Series([Timestamp('2015-12-01 09:30:00'), Timestamp('2015-12-01 09:31:00')])
```

### Step 3: Assign result = s.clip(...)

```python
result = s.clip(upper=t)
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([Timestamp('2015-12-01 09:30:00'), Timestamp('2015-12-01 09:30:30')])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign t = Timestamp(...)

```python
t = Timestamp('2015-12-01 09:30:30', tz='US/Eastern')
```

### Step 7: Assign s = Series(...)

```python
s = Series([Timestamp('2015-12-01 09:30:00', tz='US/Eastern'), Timestamp('2015-12-01 09:31:00', tz='US/Eastern')])
```

### Step 8: Assign result = s.clip(...)

```python
result = s.clip(upper=t)
```

### Step 9: Assign expected = Series(...)

```python
expected = Series([Timestamp('2015-12-01 09:30:00', tz='US/Eastern'), Timestamp('2015-12-01 09:30:30', tz='US/Eastern')])
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Workflow
t = Timestamp('2015-12-01 09:30:30')
s = Series([Timestamp('2015-12-01 09:30:00'), Timestamp('2015-12-01 09:31:00')])
result = s.clip(upper=t)
expected = Series([Timestamp('2015-12-01 09:30:00'), Timestamp('2015-12-01 09:30:30')])
tm.assert_series_equal(result, expected)
t = Timestamp('2015-12-01 09:30:30', tz='US/Eastern')
s = Series([Timestamp('2015-12-01 09:30:00', tz='US/Eastern'), Timestamp('2015-12-01 09:31:00', tz='US/Eastern')])
result = s.clip(upper=t)
expected = Series([Timestamp('2015-12-01 09:30:00', tz='US/Eastern'), Timestamp('2015-12-01 09:30:30', tz='US/Eastern')])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_clip.py:110 | Complexity: Advanced | Last updated: 2026-06-02*