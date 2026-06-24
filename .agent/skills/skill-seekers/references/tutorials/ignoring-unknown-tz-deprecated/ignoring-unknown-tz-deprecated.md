# How To: Ignoring Unknown Tz Deprecated

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test ignoring unknown tz deprecated

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

### Step 1: Assign dtstr = '2014 Jan 9 05:15 FAKE'

```python
dtstr = '2014 Jan 9 05:15 FAKE'
```

**Verification:**
```python
assert res == Timestamp(dtstr[:-5])
```

### Step 2: Assign msg = 'un-recognized timezone "FAKE". Dropping unrecognized timezones is deprecated'

```python
msg = 'un-recognized timezone "FAKE". Dropping unrecognized timezones is deprecated'
```

**Verification:**
```python
assert res == to_datetime(dtstr[:-5])
```

### Step 3: Call tm.assert_index_equal()

```python
tm.assert_index_equal(res, to_datetime([dtstr[:-5]]))
```

### Step 4: Assign res = Timestamp(...)

```python
res = Timestamp(dtstr)
```

### Step 5: Assign res = to_datetime(...)

```python
res = to_datetime(dtstr)
```

### Step 6: Assign res = to_datetime(...)

```python
res = to_datetime([dtstr])
```


## Complete Example

```python
# Workflow
dtstr = '2014 Jan 9 05:15 FAKE'
msg = 'un-recognized timezone "FAKE". Dropping unrecognized timezones is deprecated'
with tm.assert_produces_warning(FutureWarning, match=msg):
    res = Timestamp(dtstr)
assert res == Timestamp(dtstr[:-5])
with tm.assert_produces_warning(FutureWarning):
    res = to_datetime(dtstr)
assert res == to_datetime(dtstr[:-5])
with tm.assert_produces_warning(FutureWarning):
    res = to_datetime([dtstr])
tm.assert_index_equal(res, to_datetime([dtstr[:-5]]))
```

## Next Steps


---

*Source: test_to_datetime.py:3742 | Complexity: Intermediate | Last updated: 2026-06-02*