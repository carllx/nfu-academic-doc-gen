# How To: Pct Change With Nas

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: pytest, workflow, integration

## Overview

Workflow: test pct change with nas

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`

**Setup Required:**
```python
# Fixtures: periods, fill_method, limit, exp, frame_or_series
```

## Step-by-Step Guide

### Step 1: Assign vals = value

```python
vals = [np.nan, np.nan, 1, 2, 4, 10, np.nan, np.nan]
```

### Step 2: Assign obj = frame_or_series(...)

```python
obj = frame_or_series(vals)
```

### Step 3: Assign msg = value

```python
msg = f"The 'fill_method' keyword being not None and the 'limit' keyword in {type(obj).__name__}.pct_change are deprecated"
```

### Step 4: Call tm.assert_equal()

```python
tm.assert_equal(res, frame_or_series(exp))
```

### Step 5: Assign res = obj.pct_change(...)

```python
res = obj.pct_change(periods=periods, fill_method=fill_method, limit=limit)
```


## Complete Example

```python
# Setup
# Fixtures: periods, fill_method, limit, exp, frame_or_series

# Workflow
vals = [np.nan, np.nan, 1, 2, 4, 10, np.nan, np.nan]
obj = frame_or_series(vals)
msg = f"The 'fill_method' keyword being not None and the 'limit' keyword in {type(obj).__name__}.pct_change are deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    res = obj.pct_change(periods=periods, fill_method=fill_method, limit=limit)
tm.assert_equal(res, frame_or_series(exp))
```

## Next Steps


---

*Source: test_pct_change.py:25 | Complexity: Intermediate | Last updated: 2026-06-02*