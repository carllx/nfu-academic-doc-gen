# How To: To Datetime Format Yyyymm With Nat

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to datetime format YYYYMM with nat

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

### Step 1: Assign ser = Series(...)

```python
ser = Series([198012, 198012] + [198101] * 5, dtype='float')
```

### Step 2: Assign expected = Series(...)

```python
expected = Series([Timestamp('19801201'), Timestamp('19801201')] + [Timestamp('19810101')] * 5)
```

### Step 3: Assign unknown = value

```python
expected[2] = np.nan
```

### Step 4: Assign unknown = value

```python
ser[2] = np.nan
```

### Step 5: Assign result = to_datetime(...)

```python
result = to_datetime(ser, format='%Y%m', cache=cache)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: cache

# Workflow
ser = Series([198012, 198012] + [198101] * 5, dtype='float')
expected = Series([Timestamp('19801201'), Timestamp('19801201')] + [Timestamp('19810101')] * 5)
expected[2] = np.nan
ser[2] = np.nan
result = to_datetime(ser, format='%Y%m', cache=cache)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_to_datetime.py:167 | Complexity: Intermediate | Last updated: 2026-06-02*