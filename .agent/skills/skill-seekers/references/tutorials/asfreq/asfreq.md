# How To: Asfreq

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test asfreq

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
# Fixtures: series_and_frame, freq, kind
```

## Step-by-Step Guide

### Step 1: Assign obj = series_and_frame

```python
obj = series_and_frame
```

### Step 2: Assign msg = "The 'kind' keyword in (Series|DataFrame).resample is deprecated"

```python
msg = "The 'kind' keyword in (Series|DataFrame).resample is deprecated"
```

### Step 3: Call tm.assert_almost_equal()

```python
tm.assert_almost_equal(result, expected)
```

### Step 4: Assign expected = obj.to_timestamp.resample.asfreq(...)

```python
expected = obj.to_timestamp().resample(freq).asfreq()
```

### Step 5: Assign start = unknown.to_timestamp(...)

```python
start = obj.index[0].to_timestamp(how='start')
```

### Step 6: Assign end = unknown.to_timestamp(...)

```python
end = (obj.index[-1] + obj.index.freq).to_timestamp(how='start')
```

### Step 7: Assign new_index = date_range(...)

```python
new_index = date_range(start=start, end=end, freq=freq, inclusive='left')
```

### Step 8: Assign expected = obj.to_timestamp.reindex.to_period(...)

```python
expected = obj.to_timestamp().reindex(new_index).to_period(freq)
```

### Step 9: Assign result = obj.resample.asfreq(...)

```python
result = obj.resample(freq, kind=kind).asfreq()
```


## Complete Example

```python
# Setup
# Fixtures: series_and_frame, freq, kind

# Workflow
obj = series_and_frame
if kind == 'timestamp':
    expected = obj.to_timestamp().resample(freq).asfreq()
else:
    start = obj.index[0].to_timestamp(how='start')
    end = (obj.index[-1] + obj.index.freq).to_timestamp(how='start')
    new_index = date_range(start=start, end=end, freq=freq, inclusive='left')
    expected = obj.to_timestamp().reindex(new_index).to_period(freq)
msg = "The 'kind' keyword in (Series|DataFrame).resample is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = obj.resample(freq, kind=kind).asfreq()
tm.assert_almost_equal(result, expected)
```

## Next Steps


---

*Source: test_period_index.py:68 | Complexity: Advanced | Last updated: 2026-06-02*