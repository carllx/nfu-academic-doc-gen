# How To: Fillna Downcast

**Difficulty**: Advanced
**Estimated Time**: 15 minutes
**Tags**: workflow, integration

## Overview

Workflow: test fillna downcast

## Prerequisites

**Required Modules:**
- `datetime`
- `numpy`
- `pytest`
- `pytz`
- `pandas`
- `pandas._testing`
- `pandas.core.arrays`


## Step-by-Step Guide

### Step 1: Assign ser = Series(...)

```python
ser = Series([1.0, np.nan])
```

### Step 2: Assign msg = "The 'downcast' keyword in fillna is deprecated"

```python
msg = "The 'downcast' keyword in fillna is deprecated"
```

### Step 3: Assign expected = Series(...)

```python
expected = Series([1, 0])
```

### Step 4: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 5: Assign ser = Series(...)

```python
ser = Series([1.0, np.nan])
```

### Step 6: Assign expected = Series(...)

```python
expected = Series([1, 0])
```

### Step 7: Call tm.assert_series_equal()

```python
tm.assert_series_equal(result, expected)
```

### Step 8: Assign result = ser.fillna(...)

```python
result = ser.fillna(0, downcast='infer')
```

### Step 9: Assign result = ser.fillna(...)

```python
result = ser.fillna({1: 0}, downcast='infer')
```


## Complete Example

```python
# Workflow
ser = Series([1.0, np.nan])
msg = "The 'downcast' keyword in fillna is deprecated"
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = ser.fillna(0, downcast='infer')
expected = Series([1, 0])
tm.assert_series_equal(result, expected)
ser = Series([1.0, np.nan])
with tm.assert_produces_warning(FutureWarning, match=msg):
    result = ser.fillna({1: 0}, downcast='infer')
expected = Series([1, 0])
tm.assert_series_equal(result, expected)
```

## Next Steps


---

*Source: test_fillna.py:178 | Complexity: Advanced | Last updated: 2026-06-02*