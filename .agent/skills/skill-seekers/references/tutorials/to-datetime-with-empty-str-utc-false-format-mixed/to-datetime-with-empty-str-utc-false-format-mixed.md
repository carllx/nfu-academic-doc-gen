# How To: To Datetime With Empty Str Utc False Format Mixed

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to datetime with empty str utc false format mixed

## Prerequisites

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


## Step-by-Step Guide

### Step 1: Assign vals = value

```python
vals = ['2020-01-01 00:00+00:00', '']
```

### Step 2: Assign result = to_datetime(...)

```python
result = to_datetime(vals, format='mixed')
```

### Step 3: Assign expected = Index(...)

```python
expected = Index([Timestamp('2020-01-01 00:00+00:00'), 'NaT'], dtype='M8[ns, UTC]')
```

### Step 4: Call tm.assert_index_equal()

```python
tm.assert_index_equal(result, expected)
```

### Step 5: Assign alt = to_datetime(...)

```python
alt = to_datetime(vals)
```

### Step 6: Call tm.assert_index_equal()

```python
tm.assert_index_equal(alt, expected)
```

### Step 7: Assign alt2 = DatetimeIndex(...)

```python
alt2 = DatetimeIndex(vals)
```

### Step 8: Call tm.assert_index_equal()

```python
tm.assert_index_equal(alt2, expected)
```


## Complete Example

```python
# Workflow
vals = ['2020-01-01 00:00+00:00', '']
result = to_datetime(vals, format='mixed')
expected = Index([Timestamp('2020-01-01 00:00+00:00'), 'NaT'], dtype='M8[ns, UTC]')
tm.assert_index_equal(result, expected)
alt = to_datetime(vals)
tm.assert_index_equal(alt, expected)
alt2 = DatetimeIndex(vals)
tm.assert_index_equal(alt2, expected)
```

## Next Steps


---

*Source: test_to_datetime.py:3767 | Complexity: Advanced | Last updated: 2026-06-02*