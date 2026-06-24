# How To: Value Counts Datetime Tz

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test value counts datetime tz

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: unit
```

## Step-by-Step Guide

### Step 1: Assign values = value

```python
values = [pd.Timestamp('2011-01-01 09:00', tz='US/Eastern'), pd.Timestamp('2011-01-01 10:00', tz='US/Eastern'), pd.Timestamp('2011-01-01 11:00', tz='US/Eastern'), pd.Timestamp('2011-01-01 09:00', tz='US/Eastern'), pd.Timestamp('2011-01-01 09:00', tz='US/Eastern'), pd.Timestamp('2011-01-01 11:00', tz='US/Eastern')]
```

### Step 2: Assign exp_idx = pd.DatetimeIndex.as_unit(...)

```python
exp_idx = pd.DatetimeIndex(['2011-01-01 09:00', '2011-01-01 11:00', '2011-01-01 10:00'], tz='US/Eastern', name='xxx').as_unit(unit)
```

### Step 3: Assign exp = Series(...)

```python
exp = Series([3, 2, 1], index=exp_idx, name='count')
```

### Step 4: Assign ser = Series.dt.as_unit(...)

```python
ser = Series(values, name='xxx').dt.as_unit(unit)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser.value_counts(), exp)
```

### Step 6: Assign idx = pd.DatetimeIndex.as_unit(...)

```python
idx = pd.DatetimeIndex(values, name='xxx').as_unit(unit)
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(idx.value_counts(), exp)
```

### Step 8: Assign exp = Series(...)

```python
exp = Series(np.array([3.0, 2.0, 1]) / 6.0, index=exp_idx, name='proportion')
```

### Step 9: Call tm.assert_series_equal()

```python
tm.assert_series_equal(ser.value_counts(normalize=True), exp)
```

### Step 10: Call tm.assert_series_equal()

```python
tm.assert_series_equal(idx.value_counts(normalize=True), exp)
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
values = [pd.Timestamp('2011-01-01 09:00', tz='US/Eastern'), pd.Timestamp('2011-01-01 10:00', tz='US/Eastern'), pd.Timestamp('2011-01-01 11:00', tz='US/Eastern'), pd.Timestamp('2011-01-01 09:00', tz='US/Eastern'), pd.Timestamp('2011-01-01 09:00', tz='US/Eastern'), pd.Timestamp('2011-01-01 11:00', tz='US/Eastern')]
exp_idx = pd.DatetimeIndex(['2011-01-01 09:00', '2011-01-01 11:00', '2011-01-01 10:00'], tz='US/Eastern', name='xxx').as_unit(unit)
exp = Series([3, 2, 1], index=exp_idx, name='count')
ser = Series(values, name='xxx').dt.as_unit(unit)
tm.assert_series_equal(ser.value_counts(), exp)
idx = pd.DatetimeIndex(values, name='xxx').as_unit(unit)
tm.assert_series_equal(idx.value_counts(), exp)
exp = Series(np.array([3.0, 2.0, 1]) / 6.0, index=exp_idx, name='proportion')
tm.assert_series_equal(ser.value_counts(normalize=True), exp)
tm.assert_series_equal(idx.value_counts(normalize=True), exp)
```

## Next Steps


---

*Source: test_value_counts.py:43 | Complexity: Advanced | Last updated: 2026-06-02*