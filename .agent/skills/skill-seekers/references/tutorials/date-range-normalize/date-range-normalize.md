# How To: Date Range Normalize

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test date range normalize

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign snap = datetime.today(...)

```python
snap = datetime.today()
```

**Verification:**
```python
assert val.time() == the_time
```

### Step 2: Assign n = 50

```python
n = 50
```

### Step 3: Assign rng = date_range(...)

```python
rng = date_range(snap, periods=n, normalize=False, freq='2D')
```

### Step 4: Assign offset = timedelta(...)

```python
offset = timedelta(2)
```

### Step 5: Assign expected = DatetimeIndex(...)

```python
expected = DatetimeIndex([snap + i * offset for i in range(n)], dtype='M8[ns]', freq=offset)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(rng, expected)
```

### Step 7: Assign rng = date_range(...)

```python
rng = date_range('1/1/2000 08:15', periods=n, normalize=False, freq='B')
```

### Step 8: Assign the_time = time(...)

```python
the_time = time(8, 15)
```

**Verification:**
```python
assert val.time() == the_time
```


## Complete Example

```python
# Workflow
snap = datetime.today()
n = 50
rng = date_range(snap, periods=n, normalize=False, freq='2D')
offset = timedelta(2)
expected = DatetimeIndex([snap + i * offset for i in range(n)], dtype='M8[ns]', freq=offset)
tm.assert_index_equal(rng, expected)
rng = date_range('1/1/2000 08:15', periods=n, normalize=False, freq='B')
the_time = time(8, 15)
for val in rng:
    assert val.time() == the_time
```

## Next Steps


---

*Source: test_date_range.py:294 | Complexity: Advanced | Last updated: 2026-06-02*