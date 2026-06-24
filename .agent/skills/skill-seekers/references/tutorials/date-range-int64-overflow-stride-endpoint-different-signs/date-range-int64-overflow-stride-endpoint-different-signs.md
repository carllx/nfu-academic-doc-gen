# How To: Date Range Int64 Overflow Stride Endpoint Different Signs

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test date range int64 overflow stride endpoint different signs

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
# Fixtures: s_ts, e_ts
```

## Step-by-Step Guide

### Step 1: Assign start = Timestamp(...)

```python
start = Timestamp(s_ts)
```

**Verification:**
```python
assert expected[0] == start
```

### Step 2: Assign end = Timestamp(...)

```python
end = Timestamp(e_ts)
```

**Verification:**
```python
assert expected[-1] == end
```

### Step 3: Assign expected = date_range(...)

```python
expected = date_range(start=start, end=end, freq='-1h')
```

**Verification:**
```python
assert expected[0] == start
```

### Step 4: Assign dti = date_range(...)

```python
dti = date_range(end=end, periods=len(expected), freq='-1h')
```

### Step 5: Call tm.assert_index_equal()

```python
tm.assert_index_equal(dti, expected)
```


## Complete Example

```python
# Setup
# Fixtures: s_ts, e_ts

# Workflow
start = Timestamp(s_ts)
end = Timestamp(e_ts)
expected = date_range(start=start, end=end, freq='-1h')
assert expected[0] == start
assert expected[-1] == end
dti = date_range(end=end, periods=len(expected), freq='-1h')
tm.assert_index_equal(dti, expected)
```

## Next Steps


---

*Source: test_date_range.py:267 | Complexity: Intermediate | Last updated: 2026-06-02*