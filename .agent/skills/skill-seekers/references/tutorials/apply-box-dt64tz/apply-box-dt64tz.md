# How To: Apply Box Dt64Tz

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test apply box dt64tz

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.tests.apply.common`


## Step-by-Step Guide

### Step 1: Assign vals = value

```python
vals = [pd.Timestamp('2011-01-01', tz='US/Eastern'), pd.Timestamp('2011-01-02', tz='US/Eastern')]
```

**Verification:**
```python
assert ser.dtype == 'datetime64[ns, US/Eastern]'
```

### Step 2: Assign ser = Series(...)

```python
ser = Series(vals, dtype='M8[ns, US/Eastern]')
```

**Verification:**
```python
assert ser.dtype == 'datetime64[ns, US/Eastern]'
```

### Step 3: Assign res = ser.apply(...)

```python
res = ser.apply(lambda x: f'{type(x).__name__}_{x.day}_{x.tz}', by_row='compat')
```

### Step 4: Assign exp = Series(...)

```python
exp = Series(['Timestamp_1_US/Eastern', 'Timestamp_2_US/Eastern'])
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(res, exp)
```


## Complete Example

```python
# Workflow
vals = [pd.Timestamp('2011-01-01', tz='US/Eastern'), pd.Timestamp('2011-01-02', tz='US/Eastern')]
ser = Series(vals, dtype='M8[ns, US/Eastern]')
assert ser.dtype == 'datetime64[ns, US/Eastern]'
res = ser.apply(lambda x: f'{type(x).__name__}_{x.day}_{x.tz}', by_row='compat')
exp = Series(['Timestamp_1_US/Eastern', 'Timestamp_2_US/Eastern'])
tm.assert_series_equal(res, exp)
```

## Next Steps


---

*Source: test_series_apply.py:165 | Complexity: Intermediate | Last updated: 2026-06-02*