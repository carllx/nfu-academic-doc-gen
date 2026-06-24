# How To: Combine First Dt Tz Values

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test combine first dt tz values

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `numpy`
- `pandas`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: tz_naive_fixture
```

## Step-by-Step Guide

### Step 1: Assign ser1 = Series(...)

```python
ser1 = Series(pd.DatetimeIndex(['20150101', '20150102', '20150103'], tz=tz_naive_fixture), name='ser1')
```

### Step 2: Assign ser2 = Series(...)

```python
ser2 = Series(pd.DatetimeIndex(['20160514', '20160515', '20160516'], tz=tz_naive_fixture), index=[2, 3, 4], name='ser2')
```

### Step 3: Assign result = ser1.combine_first(...)

```python
result = ser1.combine_first(ser2)
```

### Step 4: Assign exp_vals = pd.DatetimeIndex(...)

```python
exp_vals = pd.DatetimeIndex(['20150101', '20150102', '20150103', '20160515', '20160516'], tz=tz_naive_fixture)
```

### Step 5: Assign exp = Series(...)

```python
exp = Series(exp_vals, name='ser1')
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(exp, result)
```


## Complete Example

```python
# Setup
# Fixtures: tz_naive_fixture

# Workflow
ser1 = Series(pd.DatetimeIndex(['20150101', '20150102', '20150103'], tz=tz_naive_fixture), name='ser1')
ser2 = Series(pd.DatetimeIndex(['20160514', '20160515', '20160516'], tz=tz_naive_fixture), index=[2, 3, 4], name='ser2')
result = ser1.combine_first(ser2)
exp_vals = pd.DatetimeIndex(['20150101', '20150102', '20150103', '20160515', '20160516'], tz=tz_naive_fixture)
exp = Series(exp_vals, name='ser1')
tm.assert_series_equal(exp, result)
```

## Next Steps


---

*Source: test_combine_first.py:88 | Complexity: Intermediate | Last updated: 2026-06-02*