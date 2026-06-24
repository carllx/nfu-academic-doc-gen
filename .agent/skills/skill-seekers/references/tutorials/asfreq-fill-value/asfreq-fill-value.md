# How To: Asfreq Fill Value

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test asfreq fill value

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `datetime`
- `warnings`
- `dateutil`
- `numpy`
- `pytest`
- `pytz`
- `pandas._libs.tslibs.ccalendar`
- `pandas._libs.tslibs.period`
- `pandas.errors`
- `pandas`
- `pandas`
- `pandas._testing`
- `pandas.core.indexes.datetimes`
- `pandas.core.indexes.period`
- `pandas.core.resample`
- `pandas.tseries`

**Setup Required:**
```python
# Fixtures: series
```

## Step-by-Step Guide

### Step 1: Assign s = series

```python
s = series
```

### Step 2: Assign new_index = date_range(...)

```python
new_index = date_range(s.index[0].to_timestamp(how='start'), s.index[-1].to_timestamp(how='start'), freq='1h')
```

### Step 3: Assign expected = s.to_timestamp.reindex(...)

```python
expected = s.to_timestamp().reindex(new_index, fill_value=4.0)
```

### Step 4: Assign msg = "The 'kind' keyword in Series.resample is deprecated"

```python
msg = "The 'kind' keyword in Series.resample is deprecated"
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign frame = s.to_frame(...)

```python
frame = s.to_frame('value')
```

### Step 7: Assign new_index = date_range(...)

```python
new_index = date_range(frame.index[0].to_timestamp(how='start'), frame.index[-1].to_timestamp(how='start'), freq='1h')
```

### Step 8: Assign expected = frame.to_timestamp.reindex(...)

```python
expected = frame.to_timestamp().reindex(new_index, fill_value=3.0)
```

### Step 9: Assign msg = "The 'kind' keyword in DataFrame.resample is deprecated"

```python
msg = "The 'kind' keyword in DataFrame.resample is deprecated"
```

### Step 10: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 11: Assign result = s.resample.asfreq(...)

```python
result = s.resample('1h', kind='timestamp').asfreq(fill_value=4.0)
```

### Step 12: Assign result = frame.resample.asfreq(...)

```python
result = frame.resample('1h', kind='timestamp').asfreq(fill_value=3.0)
```


## Complete Example

```python
# Setup
# Fixtures: series

# Workflow
s = series
new_index = date_range(s.index[0].to_timestamp(how='start'), s.index[-1].to_timestamp(how='start'), freq='1h')
expected = s.to_timestamp().reindex(new_index, fill_value=4.0)
msg = "The 'kind' keyword in Series.resample is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = s.resample('1h', kind='timestamp').asfreq(fill_value=4.0)
tm.assert_series_equal(result, expected)
frame = s.to_frame('value')
new_index = date_range(frame.index[0].to_timestamp(how='start'), frame.index[-1].to_timestamp(how='start'), freq='1h')
expected = frame.to_timestamp().reindex(new_index, fill_value=3.0)
msg = "The 'kind' keyword in DataFrame.resample is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = frame.resample('1h', kind='timestamp').asfreq(fill_value=3.0)
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_period_index.py:85 | Complexity: Advanced | Last updated: 2026-06-02*