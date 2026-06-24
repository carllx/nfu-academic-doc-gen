# How To: Reindex Tzaware Fill Value

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test reindex tzaware fill value

## Prerequisites

**Required Modules:**
- `datetime`
- `inspect`
- `numpy`
- `pytest`
- `pandas._libs.tslibs.timezones`
- `pandas.compat`
- `pandas.compat.numpy`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.api.types`


## Step-by-Step Guide

### Step 1: Assign df = DataFrame(...)

```python
df = DataFrame([[1]])
```

**Verification:**
```python
assert res.dtypes[1] == pd.DatetimeTZDtype(unit='s', tz='US/Pacific')
```

### Step 2: Assign ts = pd.Timestamp(...)

```python
ts = pd.Timestamp('2023-04-10 17:32', tz='US/Pacific')
```

**Verification:**
```python
assert res.dtypes[1] == pd.PeriodDtype('s')
```

### Step 3: Assign res = df.reindex(...)

```python
res = df.reindex([0, 1], axis=1, fill_value=ts)
```

**Verification:**
```python
assert res.dtypes[1] == pd.IntervalDtype('datetime64[s, US/Pacific]', 'right')
```

### Step 4: Assign expected = DataFrame(...)

```python
expected = DataFrame({0: [1], 1: [ts]})
```

### Step 5: Assign unknown = unknown.astype(...)

```python
expected[1] = expected[1].astype(res.dtypes[1])
```

### Step 6: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expected)
```

### Step 7: Assign per = ts.tz_localize.to_period(...)

```python
per = ts.tz_localize(None).to_period('s')
```

### Step 8: Assign res = df.reindex(...)

```python
res = df.reindex([0, 1], axis=1, fill_value=per)
```

**Verification:**
```python
assert res.dtypes[1] == pd.PeriodDtype('s')
```

### Step 9: Assign expected = DataFrame(...)

```python
expected = DataFrame({0: [1], 1: [per]})
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expected)
```

### Step 11: Assign interval = pd.Interval(...)

```python
interval = pd.Interval(ts, ts + pd.Timedelta(seconds=1))
```

### Step 12: Assign res = df.reindex(...)

```python
res = df.reindex([0, 1], axis=1, fill_value=interval)
```

**Verification:**
```python
assert res.dtypes[1] == pd.IntervalDtype('datetime64[s, US/Pacific]', 'right')
```

### Step 13: Assign expected = DataFrame(...)

```python
expected = DataFrame({0: [1], 1: [interval]})
```

### Step 14: Assign unknown = unknown.astype(...)

```python
expected[1] = expected[1].astype(res.dtypes[1])
```

### Step 15: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(res, expected)
```


## Complete Example

```python
# Workflow
df = DataFrame([[1]])
ts = pd.Timestamp('2023-04-10 17:32', tz='US/Pacific')
res = df.reindex([0, 1], axis=1, fill_value=ts)
assert res.dtypes[1] == pd.DatetimeTZDtype(unit='s', tz='US/Pacific')
expected = DataFrame({0: [1], 1: [ts]})
expected[1] = expected[1].astype(res.dtypes[1])
tm.assert_frame_equal(res, expected)
per = ts.tz_localize(None).to_period('s')
res = df.reindex([0, 1], axis=1, fill_value=per)
assert res.dtypes[1] == pd.PeriodDtype('s')
expected = DataFrame({0: [1], 1: [per]})
tm.assert_frame_equal(res, expected)
interval = pd.Interval(ts, ts + pd.Timedelta(seconds=1))
res = df.reindex([0, 1], axis=1, fill_value=interval)
assert res.dtypes[1] == pd.IntervalDtype('datetime64[s, US/Pacific]', 'right')
expected = DataFrame({0: [1], 1: [interval]})
expected[1] = expected[1].astype(res.dtypes[1])
tm.assert_frame_equal(res, expected)
```

## Next Steps


---

*Source: test_reindex.py:140 | Complexity: Advanced | Last updated: 2026-06-02*