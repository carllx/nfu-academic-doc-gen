# How To: Names

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test names

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `calendar`
- `datetime`
- `locale`
- `time`
- `unicodedata`
- `dateutil.tz`
- `hypothesis`
- `numpy`
- `pytest`
- `pytz`
- `pytz`
- `pandas._libs.tslibs.dtypes`
- `pandas._libs.tslibs.timezones`
- `pandas.compat`
- `pandas`
- `pandas._testing`
- `pandas.tseries`
- `pandas.tseries.frequencies`

**Setup Required:**
```python
# Fixtures: data, time_locale
```

## Step-by-Step Guide

### Step 1: Assign result_day = data.day_name(...)

```python
result_day = data.day_name(time_locale)
```

**Verification:**
```python
assert result_day == expected_day
```

### Step 2: Assign result_month = data.month_name(...)

```python
result_month = data.month_name(time_locale)
```

**Verification:**
```python
assert result_month == expected_month
```

### Step 3: Assign expected_day = unicodedata.normalize(...)

```python
expected_day = unicodedata.normalize('NFD', expected_day)
```

**Verification:**
```python
assert np.isnan(nan_ts.day_name(time_locale))
```

### Step 4: Assign expected_month = unicodedata.normalize(...)

```python
expected_month = unicodedata.normalize('NFD', expected_month)
```

**Verification:**
```python
assert np.isnan(nan_ts.month_name(time_locale))
```

### Step 5: Assign result_day = unicodedata.normalize(...)

```python
result_day = unicodedata.normalize('NFD', result_day)
```

### Step 6: Assign result_month = unicodedata.normalize(...)

```python
result_month = unicodedata.normalize('NFD', result_month)
```

**Verification:**
```python
assert result_day == expected_day
```

### Step 7: Assign nan_ts = Timestamp(...)

```python
nan_ts = Timestamp(NaT)
```

**Verification:**
```python
assert np.isnan(nan_ts.day_name(time_locale))
```

### Step 8: Assign expected_day = 'Monday'

```python
expected_day = 'Monday'
```

### Step 9: Assign expected_month = 'August'

```python
expected_month = 'August'
```

### Step 10: Assign expected_day = unknown.capitalize(...)

```python
expected_day = calendar.day_name[0].capitalize()
```

### Step 11: Assign expected_month = unknown.capitalize(...)

```python
expected_month = calendar.month_name[8].capitalize()
```


## Complete Example

```python
# Setup
# Fixtures: data, time_locale

# Workflow
if time_locale is None:
    expected_day = 'Monday'
    expected_month = 'August'
else:
    with tm.set_locale(time_locale, locale.LC_TIME):
        expected_day = calendar.day_name[0].capitalize()
        expected_month = calendar.month_name[8].capitalize()
result_day = data.day_name(time_locale)
result_month = data.month_name(time_locale)
expected_day = unicodedata.normalize('NFD', expected_day)
expected_month = unicodedata.normalize('NFD', expected_month)
result_day = unicodedata.normalize('NFD', result_day)
result_month = unicodedata.normalize('NFD', result_month)
assert result_day == expected_day
assert result_month == expected_month
nan_ts = Timestamp(NaT)
assert np.isnan(nan_ts.day_name(time_locale))
assert np.isnan(nan_ts.month_name(time_locale))
```

## Next Steps


---

*Source: test_timestamp.py:129 | Complexity: Advanced | Last updated: 2026-06-02*