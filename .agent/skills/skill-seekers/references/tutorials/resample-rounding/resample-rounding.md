# How To: Resample Rounding

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test resample rounding

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `functools`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas._typing`
- `pandas.compat`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.groupby.grouper`
- `pandas.core.indexes.datetimes`
- `pandas.core.indexes.period`
- `pandas.core.resample`
- `pandas.tseries`
- `pandas.tseries.offsets`

**Setup Required:**
```python
# Fixtures: unit
```

## Step-by-Step Guide

### Step 1: Assign ts = value

```python
ts = ['2014-11-08 00:00:01', '2014-11-08 00:00:02', '2014-11-08 00:00:02', '2014-11-08 00:00:03', '2014-11-08 00:00:07', '2014-11-08 00:00:07', '2014-11-08 00:00:08', '2014-11-08 00:00:08', '2014-11-08 00:00:08', '2014-11-08 00:00:09', '2014-11-08 00:00:10', '2014-11-08 00:00:11', '2014-11-08 00:00:11', '2014-11-08 00:00:13', '2014-11-08 00:00:14', '2014-11-08 00:00:15', '2014-11-08 00:00:17', '2014-11-08 00:00:20', '2014-11-08 00:00:21']
```

### Step 2: Assign df = DataFrame(...)

```python
df = DataFrame({'value': [1] * 19}, index=pd.to_datetime(ts))
```

### Step 3: Assign df.index = df.index.as_unit(...)

```python
df.index = df.index.as_unit(unit)
```

### Step 4: Assign result = df.resample.sum(...)

```python
result = df.resample('6s').sum()
```

### Step 5: Assign expected = DataFrame(...)

```python
expected = DataFrame({'value': [4, 9, 4, 2]}, index=date_range('2014-11-08', freq='6s', periods=4).as_unit(unit))
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 7: Assign result = df.resample.sum(...)

```python
result = df.resample('7s').sum()
```

### Step 8: Assign expected = DataFrame(...)

```python
expected = DataFrame({'value': [4, 10, 4, 1]}, index=date_range('2014-11-08', freq='7s', periods=4).as_unit(unit))
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Assign result = df.resample.sum(...)

```python
result = df.resample('11s').sum()
```

### Step 11: Assign expected = DataFrame(...)

```python
expected = DataFrame({'value': [11, 8]}, index=date_range('2014-11-08', freq='11s', periods=2).as_unit(unit))
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 13: Assign result = df.resample.sum(...)

```python
result = df.resample('13s').sum()
```

### Step 14: Assign expected = DataFrame(...)

```python
expected = DataFrame({'value': [13, 6]}, index=date_range('2014-11-08', freq='13s', periods=2).as_unit(unit))
```

### Step 15: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 16: Assign result = df.resample.sum(...)

```python
result = df.resample('17s').sum()
```

### Step 17: Assign expected = DataFrame(...)

```python
expected = DataFrame({'value': [16, 3]}, index=date_range('2014-11-08', freq='17s', periods=2).as_unit(unit))
```

### Step 18: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: unit

# Workflow
ts = ['2014-11-08 00:00:01', '2014-11-08 00:00:02', '2014-11-08 00:00:02', '2014-11-08 00:00:03', '2014-11-08 00:00:07', '2014-11-08 00:00:07', '2014-11-08 00:00:08', '2014-11-08 00:00:08', '2014-11-08 00:00:08', '2014-11-08 00:00:09', '2014-11-08 00:00:10', '2014-11-08 00:00:11', '2014-11-08 00:00:11', '2014-11-08 00:00:13', '2014-11-08 00:00:14', '2014-11-08 00:00:15', '2014-11-08 00:00:17', '2014-11-08 00:00:20', '2014-11-08 00:00:21']
df = DataFrame({'value': [1] * 19}, index=pd.to_datetime(ts))
df.index = df.index.as_unit(unit)
result = df.resample('6s').sum()
expected = DataFrame({'value': [4, 9, 4, 2]}, index=date_range('2014-11-08', freq='6s', periods=4).as_unit(unit))
tm.assert_frame_equal(result, expected)
result = df.resample('7s').sum()
expected = DataFrame({'value': [4, 10, 4, 1]}, index=date_range('2014-11-08', freq='7s', periods=4).as_unit(unit))
tm.assert_frame_equal(result, expected)
result = df.resample('11s').sum()
expected = DataFrame({'value': [11, 8]}, index=date_range('2014-11-08', freq='11s', periods=2).as_unit(unit))
tm.assert_frame_equal(result, expected)
result = df.resample('13s').sum()
expected = DataFrame({'value': [13, 6]}, index=date_range('2014-11-08', freq='13s', periods=2).as_unit(unit))
tm.assert_frame_equal(result, expected)
result = df.resample('17s').sum()
expected = DataFrame({'value': [16, 3]}, index=date_range('2014-11-08', freq='17s', periods=2).as_unit(unit))
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_datetime_index.py:285 | Complexity: Advanced | Last updated: 2026-06-02*