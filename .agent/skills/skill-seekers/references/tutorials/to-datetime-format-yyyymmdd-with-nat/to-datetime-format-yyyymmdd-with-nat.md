# How To: To Datetime Format Yyyymmdd With Nat

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test to datetime format YYYYMMDD with nat

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
ser = Series([19801222, 19801222] + [19810105] * 5, dtype='float')
```

### Step 2: Assign expected = Series(...)

```python
expected = Series([Timestamp('19801222'), Timestamp('19801222')] + [Timestamp('19810105')] * 5)
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
result = to_datetime(ser, format='%Y%m%d', cache=cache)
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 7: Assign ser2 = ser.apply(...)

```python
ser2 = ser.apply(str)
```

### Step 8: Assign unknown = 'nat'

```python
ser2[2] = 'nat'
```

### Step 9: Call to_datetime()

```python
to_datetime(ser2, format='%Y%m%d', cache=cache)
```


## Complete Example

```python
# Setup
# Fixtures: cache

# Workflow
ser = Series([19801222, 19801222] + [19810105] * 5, dtype='float')
expected = Series([Timestamp('19801222'), Timestamp('19801222')] + [Timestamp('19810105')] * 5)
expected[2] = np.nan
ser[2] = np.nan
result = to_datetime(ser, format='%Y%m%d', cache=cache)
tm.assert_series_equal(result, expected)
ser2 = ser.apply(str)
ser2[2] = 'nat'
with pytest.raises(ValueError, match='unconverted data remains when parsing with format "%Y%m%d": ".0", at position 0'):
    to_datetime(ser2, format='%Y%m%d', cache=cache)
```

## Next Steps


---

*Source: test_to_datetime.py:141 | Complexity: Advanced | Last updated: 2026-06-02*