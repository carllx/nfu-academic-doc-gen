# How To: Pct Change With Duplicated Indices

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test pct change with duplicated indices

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: fill_method
```

## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series([np.nan, 1, 2, 3, 9, 18], index=['a', 'b'] * 3)
```

### Step 2: Assign warn = value

```python
warn = None if fill_method is None else FutureWarning
```

### Step 3: Assign msg = "The 'fill_method' keyword being not None and the 'limit' keyword in Series.pct_change are deprecated"

```python
msg = "The 'fill_method' keyword being not None and the 'limit' keyword in Series.pct_change are deprecated"
```

### Step 4: Assign expected = Series(...)

```python
expected = Series([np.nan, np.nan, 1.0, 0.5, 2.0, 1.0], index=['a', 'b'] * 3)
```

### Step 5: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 6: Assign result = s.pct_change(...)

```python
result = s.pct_change(fill_method=fill_method)
```


## Complete Example

```python
# Setup
# Fixtures: fill_method

# Workflow
s = Series([np.nan, 1, 2, 3, 9, 18], index=['a', 'b'] * 3)
warn = None if fill_method is None else FutureWarning
msg = "The 'fill_method' keyword being not None and the 'limit' keyword in Series.pct_change are deprecated"
with tm.assert_produces_warning(warn, match=msg):
    result = s.pct_change(fill_method=fill_method)
expected = Series([np.nan, np.nan, 1.0, 0.5, 2.0, 1.0], index=['a', 'b'] * 3)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_pct_change.py:99 | Complexity: Intermediate | Last updated: 2026-06-02*