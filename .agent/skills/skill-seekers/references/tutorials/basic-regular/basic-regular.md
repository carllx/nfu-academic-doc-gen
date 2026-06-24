# How To: Basic Regular

**Difficulty**: Advanced
**Estimated Time**: 20 minutes
**Tags**: workflow, integration

## Overview

Workflow: test basic regular

## Prerequisites

- [ ] Setup code must be executed first

**Required Modules:**
- `numpy`
- `pytest`
- `pandas.util._test_decorators`
- `pandas`
- `pandas._testing`
- `pandas.tseries`

**Setup Required:**
```python
# Fixtures: regular
```

## Step-by-Step Guide

### Step 1: Assign df = regular.copy(...)

```python
df = regular.copy()
```

### Step 2: Assign df.index = date_range(...)

```python
df.index = date_range('20130101', periods=5, freq='D')
```

### Step 3: Assign expected = df.rolling.sum(...)

```python
expected = df.rolling(window=1, min_periods=1).sum()
```

### Step 4: Assign result = df.rolling.sum(...)

```python
result = df.rolling(window='1D').sum()
```

### Step 5: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 6: Assign df.index = date_range(...)

```python
df.index = date_range('20130101', periods=5, freq='2D')
```

### Step 7: Assign expected = df.rolling.sum(...)

```python
expected = df.rolling(window=1, min_periods=1).sum()
```

### Step 8: Assign result = df.rolling.sum(...)

```python
result = df.rolling(window='2D', min_periods=1).sum()
```

### Step 9: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 10: Assign expected = df.rolling.sum(...)

```python
expected = df.rolling(window=1, min_periods=1).sum()
```

### Step 11: Assign result = df.rolling.sum(...)

```python
result = df.rolling(window='2D', min_periods=1).sum()
```

### Step 12: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```

### Step 13: Assign expected = df.rolling.sum(...)

```python
expected = df.rolling(window=1).sum()
```

### Step 14: Assign result = df.rolling.sum(...)

```python
result = df.rolling(window='2D').sum()
```

### Step 15: Call tm.assert_frame_equal()

```python
tm.assert_frame_equal(result, expected)
```


## Complete Example

```python
# Setup
# Fixtures: regular

# Workflow
df = regular.copy()
df.index = date_range('20130101', periods=5, freq='D')
expected = df.rolling(window=1, min_periods=1).sum()
result = df.rolling(window='1D').sum()
tm.assert_frame_equal(result, expected)
df.index = date_range('20130101', periods=5, freq='2D')
expected = df.rolling(window=1, min_periods=1).sum()
result = df.rolling(window='2D', min_periods=1).sum()
tm.assert_frame_equal(result, expected)
expected = df.rolling(window=1, min_periods=1).sum()
result = df.rolling(window='2D', min_periods=1).sum()
tm.assert_frame_equal(result, expected)
expected = df.rolling(window=1).sum()
result = df.rolling(window='2D').sum()
tm.assert_frame_equal(result, expected)
```

## Next Steps


---

*Source: test_timeseries_window.py:221 | Complexity: Advanced | Last updated: 2026-06-02*