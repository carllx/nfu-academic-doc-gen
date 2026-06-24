# How To: Pct Change Numeric

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pct change numeric

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign pnl = DataFrame.astype(...)

```python
pnl = DataFrame([np.arange(0, 40, 10), np.arange(0, 40, 10), np.arange(0, 40, 10)]).astype(np.float64)
```

### Step 2: Assign unknown = value

```python
pnl.iat[1, 0] = np.nan
```

### Step 3: Assign unknown = value

```python
pnl.iat[1, 1] = np.nan
```

### Step 4: Assign unknown = 60

```python
pnl.iat[2, 3] = 60
```

### Step 5: Assign msg = "The 'fill_method' keyword being not None and the 'limit' keyword in DataFrame.pct_change are deprecated"

```python
msg = "The 'fill_method' keyword being not None and the 'limit' keyword in DataFrame.pct_change are deprecated"
```

### Step 6: Assign expected = value

```python
expected = pnl.ffill(axis=axis) / pnl.ffill(axis=axis).shift(axis=axis) - 1
```

### Step 7: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 8: Assign result = pnl.pct_change(...)

```python
result = pnl.pct_change(axis=axis, fill_method='pad')
```


## Complete Example

```python
# Workflow
pnl = DataFrame([np.arange(0, 40, 10), np.arange(0, 40, 10), np.arange(0, 40, 10)]).astype(np.float64)
pnl.iat[1, 0] = np.nan
pnl.iat[1, 1] = np.nan
pnl.iat[2, 3] = 60
msg = "The 'fill_method' keyword being not None and the 'limit' keyword in DataFrame.pct_change are deprecated"
for axis in range(2):
    expected = pnl.ffill(axis=axis) / pnl.ffill(axis=axis).shift(axis=axis) - 1
    with tm.assert_produces_warning(FutureWarning, match=msg):
        result = pnl.pct_change(axis=axis, fill_method='pad')
    tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_pct_change.py:39 | Complexity: Advanced | Last updated: 2026-06-02*