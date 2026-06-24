# How To: Replace Gh5319

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test replace gh5319

## Prerequisites

**Required Modules:**
- `re`
- `numpy`
- `pytest`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign ser = pd.Series(...)

```python
ser = pd.Series([0, np.nan, 2, 3, 4])
```

### Step 2: Assign expected = ser.ffill(...)

```python
expected = ser.ffill()
```

### Step 3: Assign msg = "Series.replace without 'value' and with non-dict-like 'to_replace' is deprecated"

```python
msg = "Series.replace without 'value' and with non-dict-like 'to_replace' is deprecated"
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign ser = pd.Series(...)

```python
ser = pd.Series([0, np.nan, 2, 3, 4])
```

### Step 6: Assign expected = ser.ffill(...)

```python
expected = ser.ffill()
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign result = ser.replace(...)

```python
result = ser.replace([np.nan])
```

### Step 9: Assign result = ser.replace(...)

```python
result = ser.replace(np.nan)
```


## Complete Example

```python
# Workflow
ser = pd.Series([0, np.nan, 2, 3, 4])
expected = ser.ffill()
msg = "Series.replace without 'value' and with non-dict-like 'to_replace' is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = ser.replace([np.nan])
tm.assert_series_equal(result, expected)
ser = pd.Series([0, np.nan, 2, 3, 4])
expected = ser.ffill()
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = ser.replace(np.nan)
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_replace.py:138 | Complexity: Advanced | Last updated: 2026-06-02*