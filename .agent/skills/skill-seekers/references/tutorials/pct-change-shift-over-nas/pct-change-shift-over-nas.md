# How To: Pct Change Shift Over Nas

**Difficulty**: Intermediate
**Estimated Time**: 10 minutes
**Tags**: workflow, integration

## Overview

Workflow: test pct change shift over nas

## Prerequisites

**Required Modules:**
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`


## Step-by-Step Guide

### Step 1: Assign s = Series(...)

```python
s = Series([1.0, 1.5, np.nan, 2.5, 3.0])
```

### Step 2: Assign msg = "The default fill_method='pad' in Series.pct_change is deprecated"

```python
msg = "The default fill_method='pad' in Series.pct_change is deprecated"
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([np.nan, 0.5, 0.0, 2.5 / 1.5 - 1, 0.2])
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(chg, expected)
```

### Step 5: Assign chg = s.pct_change(...)

```python
chg = s.pct_change()
```


## Complete Example

```python
# Workflow
s = Series([1.0, 1.5, np.nan, 2.5, 3.0])
msg = "The default fill_method='pad' in Series.pct_change is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    chg = s.pct_change()
expected = Series([np.nan, 0.5, 0.0, 2.5 / 1.5 - 1, 0.2])
tm.assert_series_equal(chg, expected)
```

## Next Steps


---

*Source: test_pct_change.py:46 | Complexity: Intermediate | Last updated: 2026-06-02*