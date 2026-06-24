# How To: Pct Change Periods Freq

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test pct change periods freq

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: freq, periods, fill_method, limit, datetime_series
```

## Step-by-Step Guide

### Step 1: Assign msg = "The 'fill_method' keyword being not None and the 'limit' keyword in Series.pct_change are deprecated"

```python
msg = "The 'fill_method' keyword being not None and the 'limit' keyword in Series.pct_change are deprecated"
```

### Step 2: Call tm.assert_series_equal()

```python
tm.assert_series_equal(rs_freq, rs_periods)
```

### Step 3: Assign empty_ts = Series(...)

```python
empty_ts = Series(index=datetime_series.index, dtype=object)
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(rs_freq, rs_periods)
```

### Step 5: Assign rs_freq = datetime_series.pct_change(...)

```python
rs_freq = datetime_series.pct_change(freq=freq, fill_method=fill_method, limit=limit)
```

### Step 6: Assign rs_periods = datetime_series.pct_change(...)

```python
rs_periods = datetime_series.pct_change(periods, fill_method=fill_method, limit=limit)
```

### Step 7: Assign rs_freq = empty_ts.pct_change(...)

```python
rs_freq = empty_ts.pct_change(freq=freq, fill_method=fill_method, limit=limit)
```

### Step 8: Assign rs_periods = empty_ts.pct_change(...)

```python
rs_periods = empty_ts.pct_change(periods, fill_method=fill_method, limit=limit)
```


## Complete Example

```python
# Setup
# Fixtures: freq, periods, fill_method, limit, datetime_series

# Workflow
msg = "The 'fill_method' keyword being not None and the 'limit' keyword in Series.pct_change are deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    rs_freq = datetime_series.pct_change(freq=freq, fill_method=fill_method, limit=limit)
with tm.assert_produces_warning(FutureWarning, match=msg):
    rs_periods = datetime_series.pct_change(periods, fill_method=fill_method, limit=limit)
tm.assert_series_equal(rs_freq, rs_periods)
empty_ts = Series(index=datetime_series.index, dtype=object)
with tm.assert_produces_warning(FutureWarning, match=msg):
    rs_freq = empty_ts.pct_change(freq=freq, fill_method=fill_method, limit=limit)
with tm.assert_produces_warning(FutureWarning, match=msg):
    rs_periods = empty_ts.pct_change(periods, fill_method=fill_method, limit=limit)
tm.assert_series_equal(rs_freq, rs_periods)
```

## Next Steps


---

*Source: test_pct_change.py:67 | Complexity: Advanced | Last updated: 2026-06-02*