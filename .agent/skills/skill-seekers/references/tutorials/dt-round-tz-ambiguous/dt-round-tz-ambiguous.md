# How To: Dt Round Tz Ambiguous

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test dt round tz ambiguous

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `calendar`
- `datetime`
- `locale`
- `unicodedata`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs.timezones`
- `pandas.errors`
- `pandas.core.dtypes.common`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`
- `pandas.core.indexes.accessors`

**Setup Required:**
```python
# Fixtures: method
```

## Step-by-Step Guide

### Step 1: Assign df1 = DataFrame(...)

```python
df1 = DataFrame([pd.to_datetime('2017-10-29 02:00:00+02:00', utc=True), pd.to_datetime('2017-10-29 02:00:00+01:00', utc=True), pd.to_datetime('2017-10-29 03:00:00+01:00', utc=True)], columns=['date'])
```

### Step 2: Assign unknown = unknown.dt.tz_convert(...)

```python
df1['date'] = df1['date'].dt.tz_convert('Europe/Madrid')
```

### Step 3: Assign result = getattr(...)

```python
result = getattr(df1.date.dt, method)('h', ambiguous='infer')
```

### Step 4: Assign expected = value

```python
expected = df1['date']
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign result = getattr(...)

```python
result = getattr(df1.date.dt, method)('h', ambiguous=[True, False, False])
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign result = getattr(...)

```python
result = getattr(df1.date.dt, method)('h', ambiguous='NaT')
```

### Step 9: Assign expected = unknown.copy(...)

```python
expected = df1['date'].copy()
```

### Step 10: Assign unknown = value

```python
expected.iloc[0:2] = pd.NaT
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 12: Call getattr()

```python
getattr(df1.date.dt, method)('h', ambiguous='raise')
```


## Complete Example

```python
# Setup
# Fixtures: method

# Workflow
df1 = DataFrame([pd.to_datetime('2017-10-29 02:00:00+02:00', utc=True), pd.to_datetime('2017-10-29 02:00:00+01:00', utc=True), pd.to_datetime('2017-10-29 03:00:00+01:00', utc=True)], columns=['date'])
df1['date'] = df1['date'].dt.tz_convert('Europe/Madrid')
result = getattr(df1.date.dt, method)('h', ambiguous='infer')
expected = df1['date']
tm.assert_series_equal(result, expected)
result = getattr(df1.date.dt, method)('h', ambiguous=[True, False, False])
tm.assert_series_equal(result, expected)
result = getattr(df1.date.dt, method)('h', ambiguous='NaT')
expected = df1['date'].copy()
expected.iloc[0:2] = pd.NaT
tm.assert_series_equal(result, expected)
with tm.external_error_raised(pytz.AmbiguousTimeError):
    getattr(df1.date.dt, method)('h', ambiguous='raise')
```

## Next Steps


---

*Source: test_dt_accessor.py:342 | Complexity: Advanced | Last updated: 2026-06-02*