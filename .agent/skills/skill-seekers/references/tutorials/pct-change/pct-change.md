# How To: Pct Change

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pct change

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: datetime_series
```

## Step-by-Step Guide

### Step 1: Assign msg = "The 'fill_method' keyword being not None and the 'limit' keyword in Series.pct_change are deprecated"

```python
msg = "The 'fill_method' keyword being not None and the 'limit' keyword in Series.pct_change are deprecated"
```

### Step 2: Assign rs = datetime_series.pct_change(...)

```python
rs = datetime_series.pct_change(fill_method=None)
```

### Step 3: Call tm.assert_series_equal()

```python
tm.assert_series_equal(rs, datetime_series / datetime_series.shift(1) - 1)
```

### Step 4: Assign rs = datetime_series.pct_change(...)

```python
rs = datetime_series.pct_change(2)
```

### Step 5: Assign filled = datetime_series.ffill(...)

```python
filled = datetime_series.ffill()
```

### Step 6: Call tm.assert_series_equal()

```python
tm.assert_series_equal(rs, filled / filled.shift(2) - 1)
```

### Step 7: Assign filled = datetime_series.bfill(...)

```python
filled = datetime_series.bfill(limit=1)
```

### Step 8: Call tm.assert_series_equal()

```python
tm.assert_series_equal(rs, filled / filled.shift(1) - 1)
```

### Step 9: Assign rs = datetime_series.pct_change(...)

```python
rs = datetime_series.pct_change(freq='5D')
```

### Step 10: Assign filled = datetime_series.ffill(...)

```python
filled = datetime_series.ffill()
```

### Step 11: Call tm.assert_series_equal()

```python
tm.assert_series_equal(rs, (filled / filled.shift(freq='5D') - 1).reindex_like(filled))
```

### Step 12: Assign rs = datetime_series.pct_change(...)

```python
rs = datetime_series.pct_change(fill_method='bfill', limit=1)
```


## Complete Example

```python
# Setup
# Fixtures: datetime_series

# Workflow
msg = "The 'fill_method' keyword being not None and the 'limit' keyword in Series.pct_change are deprecated"
rs = datetime_series.pct_change(fill_method=None)
tm.assert_series_equal(rs, datetime_series / datetime_series.shift(1) - 1)
rs = datetime_series.pct_change(2)
filled = datetime_series.ffill()
tm.assert_series_equal(rs, filled / filled.shift(2) - 1)
with tm.assert_produces_warning(FutureWarning, match=msg):
    rs = datetime_series.pct_change(fill_method='bfill', limit=1)
filled = datetime_series.bfill(limit=1)
tm.assert_series_equal(rs, filled / filled.shift(1) - 1)
rs = datetime_series.pct_change(freq='5D')
filled = datetime_series.ffill()
tm.assert_series_equal(rs, (filled / filled.shift(freq='5D') - 1).reindex_like(filled))
```

## Next Steps


---

*Source: test_pct_change.py:12 | Complexity: Advanced | Last updated: 2026-06-02*