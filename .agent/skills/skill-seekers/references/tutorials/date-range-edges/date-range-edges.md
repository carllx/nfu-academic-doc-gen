# How To: Date Range Edges

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test date range edges

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `re`
- `numpy`
- `pytest`
- `pytz`
- `pytz`
- `pandas._libs.tslibs`
- `pandas._libs.tslibs.offsets`
- `pandas.errors`
- `pandas.util._test_decorators`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays.datetimes`
- `pandas.tests.indexes.datetimes.test_timezones`
- `pandas.tseries.holiday`
- `pandas._libs.tslibs.timezones`
- `pandas._libs.tslibs.timezones`

**Setup Required:**
```python
# Fixtures: freq
```

## Step-by-Step Guide

### Step 1: Assign td = Timedelta(...)

```python
td = Timedelta(f'1{freq}')
```

### Step 2: Assign ts = Timestamp(...)

```python
ts = Timestamp('1970-01-01')
```

### Step 3: Assign idx = date_range(...)

```python
idx = date_range(start=ts + td, end=ts + 4 * td, freq=freq)
```

### Step 4: Assign exp = DatetimeIndex(...)

```python
exp = DatetimeIndex([ts + n * td for n in range(1, 5)], dtype='M8[ns]', freq=freq)
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, exp)
```

### Step 6: Assign idx = date_range(...)

```python
idx = date_range(start=ts + 4 * td, end=ts + td, freq=freq)
```

### Step 7: Assign exp = DatetimeIndex(...)

```python
exp = DatetimeIndex([], dtype='M8[ns]', freq=freq)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, exp)
```

### Step 9: Assign idx = date_range(...)

```python
idx = date_range(start=ts + td, end=ts + td, freq=freq)
```

### Step 10: Assign exp = DatetimeIndex(...)

```python
exp = DatetimeIndex([ts + td], dtype='M8[ns]', freq=freq)
```

### Step 11: Call tm.assert_index_equal()

```python
tm.assert_index_equal(idx, exp)
```


## Complete Example

```python
# Setup
# Fixtures: freq

# Workflow
td = Timedelta(f'1{freq}')
ts = Timestamp('1970-01-01')
idx = date_range(start=ts + td, end=ts + 4 * td, freq=freq)
exp = DatetimeIndex([ts + n * td for n in range(1, 5)], dtype='M8[ns]', freq=freq)
tm.assert_index_equal(idx, exp)
idx = date_range(start=ts + 4 * td, end=ts + td, freq=freq)
exp = DatetimeIndex([], dtype='M8[ns]', freq=freq)
tm.assert_index_equal(idx, exp)
idx = date_range(start=ts + td, end=ts + td, freq=freq)
exp = DatetimeIndex([ts + td], dtype='M8[ns]', freq=freq)
tm.assert_index_equal(idx, exp)
```

## Next Steps


---

*Source: test_date_range.py:175 | Complexity: Advanced | Last updated: 2026-06-02*