# How To: Tz Localize Ambiguous Compat

**Difficulty**: Intermediate
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test tz localize ambiguous compat

## Prerequisites

**Required Modules:**
- `datetime`
- `re`
- `dateutil.tz`
- `pytest`
- `pytz`
- `pytz.exceptions`
- `pandas._libs.tslibs.dtypes`
- `pandas.errors`
- `pandas`
- `zoneinfo`


## Step-by-Step Guide

### Step 1: Assign naive = Timestamp(...)

```python
naive = Timestamp('2013-10-27 01:00:00')
```

**Verification:**
```python
assert result_pytz._value == result_dateutil._value
```

### Step 2: Assign pytz_zone = 'Europe/London'

```python
pytz_zone = 'Europe/London'
```

**Verification:**
```python
assert result_pytz._value == 1382835600
```

### Step 3: Assign dateutil_zone = 'dateutil/Europe/London'

```python
dateutil_zone = 'dateutil/Europe/London'
```

**Verification:**
```python
assert result_pytz.to_pydatetime().tzname() == 'GMT'
```

### Step 4: Assign result_pytz = naive.tz_localize(...)

```python
result_pytz = naive.tz_localize(pytz_zone, ambiguous=False)
```

**Verification:**
```python
assert result_dateutil.to_pydatetime().tzname() == 'GMT'
```

### Step 5: Assign result_dateutil = naive.tz_localize(...)

```python
result_dateutil = naive.tz_localize(dateutil_zone, ambiguous=False)
```

**Verification:**
```python
assert str(result_pytz) == str(result_dateutil)
```

### Step 6: Assign result_pytz = naive.tz_localize(...)

```python
result_pytz = naive.tz_localize(pytz_zone, ambiguous=True)
```

**Verification:**
```python
assert result_pytz._value == result_dateutil._value
```

### Step 7: Assign result_dateutil = naive.tz_localize(...)

```python
result_dateutil = naive.tz_localize(dateutil_zone, ambiguous=True)
```

**Verification:**
```python
assert result_pytz._value == 1382832000
```


## Complete Example

```python
# Workflow
naive = Timestamp('2013-10-27 01:00:00')
pytz_zone = 'Europe/London'
dateutil_zone = 'dateutil/Europe/London'
result_pytz = naive.tz_localize(pytz_zone, ambiguous=False)
result_dateutil = naive.tz_localize(dateutil_zone, ambiguous=False)
assert result_pytz._value == result_dateutil._value
assert result_pytz._value == 1382835600
assert result_pytz.to_pydatetime().tzname() == 'GMT'
assert result_dateutil.to_pydatetime().tzname() == 'GMT'
assert str(result_pytz) == str(result_dateutil)
result_pytz = naive.tz_localize(pytz_zone, ambiguous=True)
result_dateutil = naive.tz_localize(dateutil_zone, ambiguous=True)
assert result_pytz._value == result_dateutil._value
assert result_pytz._value == 1382832000
assert str(result_pytz) == str(result_dateutil)
assert result_pytz.to_pydatetime().tzname() == result_dateutil.to_pydatetime().tzname()
```

## Next Steps


---

*Source: test_tz_localize.py:206 | Complexity: Intermediate | Last updated: 2026-06-02*