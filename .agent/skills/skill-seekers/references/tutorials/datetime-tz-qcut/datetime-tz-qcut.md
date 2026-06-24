# How To: Datetime Tz Qcut

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test datetime tz qcut

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `os`
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: bins
```

## Step-by-Step Guide

### Step 1: Assign tz = 'US/Eastern'

```python
tz = 'US/Eastern'
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(date_range('20130101', periods=3, tz=tz))
```

### Step 3: Assign result = qcut(...)

```python
result = qcut(ser, bins)
```

### Step 4: Assign expected = Series.astype(...)

```python
expected = Series(IntervalIndex([Interval(Timestamp('2012-12-31 23:59:59.999999999', tz=tz), Timestamp('2013-01-01 16:00:00', tz=tz)), Interval(Timestamp('2013-01-01 16:00:00', tz=tz), Timestamp('2013-01-02 08:00:00', tz=tz)), Interval(Timestamp('2013-01-02 08:00:00', tz=tz), Timestamp('2013-01-03 00:00:00', tz=tz))])).astype(CategoricalDtype(ordered=True))
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: bins

# Workflow
tz = 'US/Eastern'
ser = Series(date_range('20130101', periods=3, tz=tz))
result = qcut(ser, bins)
expected = Series(IntervalIndex([Interval(Timestamp('2012-12-31 23:59:59.999999999', tz=tz), Timestamp('2013-01-01 16:00:00', tz=tz)), Interval(Timestamp('2013-01-01 16:00:00', tz=tz), Timestamp('2013-01-02 08:00:00', tz=tz)), Interval(Timestamp('2013-01-02 08:00:00', tz=tz), Timestamp('2013-01-03 00:00:00', tz=tz))])).astype(CategoricalDtype(ordered=True))
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_qcut.py:232 | Complexity: Intermediate | Last updated: 2026-06-02*