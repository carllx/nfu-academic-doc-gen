# How To: To Datetime Monotonic Increasing Index

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test to datetime monotonic increasing index

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `calendar`
- `collections`
- `datetime`
- `decimal`
- `locale`
- `dateutil.parser`
- `dateutil.tz.tz`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs`
- `pandas._libs.tslibs`
- `pandas.compat`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.tools`
- `pandas.core.tools.datetimes`
- `pandas.tests.indexes.datetimes.test_timezones`

**Setup Required:**
```python
# Fixtures: cache
```

## Step-by-Step Guide

### Step 1: Assign cstart = start_caching_at

```python
cstart = start_caching_at
```

### Step 2: Assign times = date_range(...)

```python
times = date_range(Timestamp('1980'), periods=cstart, freq='YS')
```

### Step 3: Assign times = times.to_frame.sample(...)

```python
times = times.to_frame(index=False, name='DT').sample(n=cstart, random_state=1)
```

### Step 4: Assign times.index = value

```python
times.index = times.index.to_series().astype(float) / 1000
```

### Step 5: Assign result = to_datetime(...)

```python
result = to_datetime(times.iloc[:, 0], cache=cache)
```

### Step 6: Assign expected = value

```python
expected = times.iloc[:, 0]
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: cache

# Workflow
cstart = start_caching_at
times = date_range(Timestamp('1980'), periods=cstart, freq='YS')
times = times.to_frame(index=False, name='DT').sample(n=cstart, random_state=1)
times.index = times.index.to_series().astype(float) / 1000
result = to_datetime(times.iloc[:, 0], cache=cache)
expected = times.iloc[:, 0]
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_to_datetime.py:3638 | Complexity: Intermediate | Last updated: 2026-06-02*